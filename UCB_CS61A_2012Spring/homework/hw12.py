"""Submission for CS61A Homework 12.

Name:
Login:
Collaborators:
"""


#import sys
from threading import Lock, Thread, Condition
from time import time, sleep


# Q1.
class Sem(object):
    """Sem is a semaphore, like threading.Semaphore, implemented with locks."""
    def __init__(self, n):
        "*** YOUR CODE HERE ***"
        self.counter = n
        self._condition = Condition()

    def acquire(self):
        """Acquire the semaphore."""
        "*** YOUR CODE HERE ***"
        with self._condition:
            while self.counter <= 0:
                self._condition.wait()
            self.counter -= 1

    def release(self):
        """Release the semaphore."""
        "*** YOUR CODE HERE ***"
        with self._condition:
            self.counter += 1
            self._condition.notify()


class Tester(Thread):
    """A thread that acquires and then releases the semaphore."""
    def __init__(self, sem):
        Thread.__init__(self)
        self.sem = sem

    def run(self):
        self.sem.acquire()
        print('acquired!')
        sleep(0.1)
        print('released!')
        self.sem.release()


def sem_test():
    """Test the semaphore implementation.

    >>> sem_test()
    acquired!
    acquired!
    released!
    acquired!
    released!
    released!
    """
    sem = Sem(2)
    testers = [Tester(sem) for _ in range(3)]
    for t in testers:
        sleep(0.01)
        t.start()
    for t in testers:
        t.join()


# Q2.
class Table:
    """A table full of chopsticks, represented as locks."""
    def __init__(self, seats):
        self.seats = seats
        self.chopsticks = [Lock() for _ in range(seats)]

    def pick_left(self, seat):
        self.chopsticks[seat].acquire()

    def pick_right(self, seat):
        self.chopsticks[(seat+1) % self.seats].acquire()

    def replace_left(self, seat):
        self.chopsticks[seat].release()

    def replace_right(self, seat):
        self.chopsticks[(seat+1) % self.seats].release()


class Philosopher(Thread):
    """A philosopher who dines."""
    def __init__(self, seat, table, waiter):
        Thread.__init__(self)
        self.seat = seat
        self.table = table
        self.waiter = waiter

        self.left_in_hand = False
        self.right_in_hand = False
        self.last_eaten = time()
        self.dine = True

    def run(self):
        """Proceed to eat as long as self.dine is True.

        Don't violate abstractions! Only call methods on self and self.waiter.
        """
        while self.dine:
            self.think()
            "*** YOUR CODE HERE ***"
            self.waiter.may_I_eat()
            self.pick_left()
            self.pick_right()
            self.eat()
            # print('Philosopher {0} is eating.'.format(self.seat))
            self.replace_left()
            self.replace_right()
            self.waiter.I_am_done()

    def pick_left(self):
        self.table.pick_left(self.seat)
        self.left_in_hand = True

    def pick_right(self):
        self.table.pick_right(self.seat)
        self.right_in_hand = True

    def replace_left(self):
        self.left_in_hand = False
        self.table.replace_left(self.seat)

    def replace_right(self):
        self.right_in_hand = False
        self.table.replace_right(self.seat)

    def eat(self):
        assert self.left_in_hand and self.right_in_hand, 'Chopsticks required!'
        self.last_eaten = time()

    def think(self):
        sleep(0.0001)


class Waiter(object):
    def __init__(self, seats):
        "*** YOUR CODE HERE ***"
        self.chopsticks = Sem(seats)

    def may_I_eat(self):
        "*** YOUR CODE HERE ***"
        self.chopsticks.acquire()
        self.chopsticks.acquire()

    def I_am_done(self):
        "*** YOUR CODE HERE ***"
        self.chopsticks.release()
        self.chopsticks.release()


class Doctor(Thread):
    """The doctor makes sure that nobody appears to be starving.
    
    philosophers -- the philosophers to be checked
    interval -- how often (in seconds) to check whether they're eating
    finished -- how long (in seconds) dinner lasts
    """
    def __init__(self, philosophers, interval=.05, finished=0.5):
        Thread.__init__(self)
        self.philosophers = philosophers
        self.interval = interval
        self.finished = finished

    def run(self):
        start = time()
        while time() < start + self.finished:
            t = time()
            sleep(self.interval)
            for p in self.philosophers:
                if p.last_eaten < t:
                    print('Philosopher {0} is starving!'.format(p.seat))
        print('Dinner is over.')
        for p in self.philosophers:
            p.dine = False


def dine(n):
    """Dine until the doctor says that dinner is over.
    
    >>> dine(5)
    Dinner is over.
    >>> dine(2)
    Dinner is over.
    >>> dine(10)
    Dinner is over.
    """
    table = Table(n)
    waiter = Waiter(n)
    philosophers = [Philosopher(seat, table, waiter) for seat in range(n)]
    for p in philosophers:
        p.start()
    Doctor(philosophers).start()
    for p in philosophers:
        p.join()


# Q3.
class Stream(object):
    """A lazily computed recursive list."""

    def __init__(self, first, compute_rest, empty=False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

    def prepend(self, x):
        """The stream resulting from prepending X in front of SELF."""
        r = Stream(x, None)
        r._rest = self
        r._computed = True
        return r

    def __str__(self):
        if self.empty:
            return '<empty stream>'
        return '[{0}, ...]'.format(self.first)

empty_stream = Stream(None, None, True)


def list_to_stream(L):
    """The finite stream containing the elements of L."""
    r = empty_stream
    for i in range(-1, -len(L)-1, -1):
        r = r.prepend(L[i])
    return r


def filter_stream(fn, s):
    """Return a stream of the elements of s for which fn is true."""
    if s.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    return compute_rest()


def truncate_stream(s, k):
    """Return a stream over the first k elements of stream s."""
    if s.empty or k == 0:
        return empty_stream

    def compute_rest():
        return truncate_stream(s.rest, k-1)
    return Stream(s.first, compute_rest)


def stream_to_list(s, lim=-1):
    """Return a list containing the elements of stream S. If LIM>=0,
    returns at most the first LIM elements of S."""
    r = []
    while not s.empty and lim != 0:
        r.append(s.first)
        s = s.rest
        lim -= 1
    return r


def uniq(s):
    """A stream consisting of the unique items in S (that is, with all but
    the first occurrence of any value removed from S.
    >>> 
    >>> stream_to_list(uniq(list_to_stream([1, 2, 2, 1, 0, 4, 2, 3, 1, 9, 0])))
    [1, 2, 0, 4, 3, 9]
    """
    "*** YOUR CODE HERE ***"


# Q4.  [Extra for experts]

class FairLock:
    """A lock that is fair in the sense that, if any acquire of this lock
    is eventually matched with a release, then if a process waits on
    this lock, it will eventually be released."""


    """Maximum value of ID argument to acquire."""
    MAXID = 100

    def __init__(self):
        "*** YOUR CODE HERE ***"

    def acquire(self, id):
        """Acquire this lock, assuming that I am thread number #ID (>=0)."""
        "*** YOUR CODE HERE ***"

    def release(self):
        "*** YOUR CODE HERE ***"

