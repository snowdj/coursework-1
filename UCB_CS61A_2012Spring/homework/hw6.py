"""Submission for CS61A Homework 6.

Name:
Login:
Collaborators:
"""

# Q1 (and part of Q2).

class Bank:
    """A Bank capable of creating accounts."""

    "*** YOUR CODE HERE ***"
    def __init__(self):
        self._total_deposit = 0

    def make_account(self, amount):
        acnt = Account(self, amount)
        self._total_deposit += amount
        return acnt

    def make_secure_account(self, amount, passphrase):
        acnt = SecureAccount(self, amount, passphrase)
        self._total_deposit += amount
        return acnt        

    def total_deposits(self):
        return self._total_deposit


class Account:
    """ An account in a particular bank.

    >>> third_national = Bank()
    >>> second_federal = Bank()
    >>> acct0 = third_national.make_account(1000)
    >>> acct0.withdraw(100)
    >>> acct1 = third_national.make_account(2000)
    >>> third_national.total_deposits()
    2900
    >>> second_federal.total_deposits()
    0
    >>> acct1.total_deposits()
    Traceback (most recent call last):
       ...
    AttributeError: 'Account' object has no attribute 'total_deposits'
    >>> acct1.bank().total_deposits()
    2900
    """

    "*** YOUR CODE HERE ***"
    def __init__(self, bank, amount):
        self._balance = amount
        self._bank = bank

    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            self._bank._total_deposit += amount
        else:
            raise ValueError("Deposit amount has to be more than 0!")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._bank._total_deposit -= amount
        else:
            raise ValueError("Withdrawal amount has to be less than balance!")

    def bank(self):
        return self._bank


# Q2

class SecurityError(BaseException):
    """Exception to raise if there is an attempted security violation."""
    pass

class SecureAccount(Account):
    """An account that provides password security.
    >>> third_national = Bank()
    >>> acct3 = third_national.make_secure_account(1000, "The magic woid")
    >>> acct3.deposit(1000, 'The magic woid')
    >>> acct3.balance('The magic woid')
    2000
    >>> acct3.balance('Foobar')
    Traceback (most recent call last):
       ...
    hw6.SecurityError: wrong passphrase or account
    >>> acct3.balance()
    Traceback (most recent call last):
       ...
    hw6.SecurityError: passphrase missing
    """


    "*** YOUR CODE HERE ***"
    def __init__(self, bank, amount, passphrase):
        self._balance = amount
        self._bank = bank
        self._passphrase = passphrase

    def balance(self, *phrase):
        if len(phrase) == 0:
            raise SecurityError("passphrase missing")
        elif phrase[0] == self._passphrase:
            return Account.balance(self)
        else:
            raise SecurityError("wrong passphrase or account")

    def deposit(self, amount, *phrase):
        if len(phrase) == 0:
            raise SecurityError("passphrase missing")
        elif phrase[0] == self._passphrase:
            return Account.deposit(self, amount)
        else:
            raise SecurityError("wrong passphrase or account")

    def withdraw(self, amount, *phrase):
        if len(phrase) == 0:
            raise SecurityError("passphrase missing")
        elif phrase[0] == self._passphrase:
            return Account.withdraw(self, amount)
        else:
            raise SecurityError("wrong passphrase or account")

    

# Q3 and Q4

"*** YOUR CODE HERE ***"
    

class rlist:
    """A recursive list consisting of a first element and the rest.
    
    >>> s = rlist(1, rlist(2, rlist(3)))
    >>> len(s)
    3
    >>> s[0]
    1
    >>> s[1]
    2
    >>> s[2]
    3
    >>> for x in s:
    ...     print(x)
    1
    2
    3
    """

    def __repr__(self):
        """A printed representation of self that resembles a Python
        expression that reproduces the same list.  The builtin function
        repr(x) calls x.__repr__().  The Python interpreter uses __repr__
        to print the values of non-null expressions it evaluates."""
        f = repr(self.first())
        if self.rest() is rlist.empty():
            return 'rlist({0})'.format(f)
        else:
            return 'rlist({0}, {1})'.format(f, repr(self.rest()))

    "*** YOUR CODE HERE ***"

    class _EmptyRlist:
        def __repr__(self):
            return 'rlist.empty()'

        def first(self):
            return None

        def rest(self):
            return None

        def __len__(self):
            return 0

    _empty_rlist = _EmptyRlist()

    @classmethod
    def empty(cls):
        return rlist._empty_rlist

    def __init__(self, *arg):
        if len(arg) == 1:
            self._rlist = (arg[0], rlist.empty())
        elif len(arg) == 2:
            self._rlist = (arg[0], arg[1])
        else:
            raise TypeError('rlist only takes 1 or 2 arguments!')

    def first(self):
        return self._rlist[0]

    def rest(self):
        return self._rlist[1]

    def __len__(self):
        return 1 + self.rest().__len__()

    def __getitem__(self, k):
        if k < 0 or k >= self.__len__():
            raise IndexError('Index out of rlist range!')
        elif k == 0:
            return self.first()
        else:
            return self.rest().__getitem__(k-1)

    class _RlistIterator:
        def __init__(self, rl):
            self.rl = rl
            pass

        def __next__(self):
            if self.rl is rlist.empty():
                raise StopIteration
            else:
                f1  = self.rl.first()
                self.rl = self.rl.rest()
                return f1

    def __iter__(self):
        return rlist._RlistIterator(self)
        

# Q5.

class Monitor:
    """A general-purpose wrapper class that counts the number of times each
    attribute of a monitored object is accessed.

    >>> B = Bank()
    >>> acct = B.make_account(1000)
    >>> mon_acct = Monitor(acct)
    >>> mon_acct.balance()
    1000
    >>> for i in range(10): mon_acct.deposit(100)
    >>> mon_acct.withdraw(20)
    >>> mon_acct.balance()
    1980
    >>> mon_acct.access_count('balance')
    2
    >>> mon_acct.access_count('deposit')
    10
    >>> mon_acct.access_count('withdraw')
    1
    >>> mon_acct.access_count('clear')
    0
    >>> L = list(mon_acct.attributes_accessed())
    >>> L.sort()
    >>> L
    ['balance', 'deposit', 'withdraw']
    """

    "*** YOUR CODE HERE ***"

    def __init__(self, obj):               
        self.obj = obj
        self.attributes_dict = {}

    def __getattr__(self, attr):
        if hasattr(self.obj, attr):
            if attr in self.attributes_dict:
                self.attributes_dict[attr] += 1
            else:
                self.attributes_dict[attr] = 1
            return getattr(self.obj, attr)
        else:
            raise AttributeError('No such attribute!')

    def attributes_accessed(self):
        return self.attributes_dict

    def access_count(self, attribute):
        try:
            return self.attributes_dict[attribute]
        except KeyError:
            return 0

    
            

# Q6.

class Abbrev:
    """An abbreviation map."""

    def __init__(self, full_names):
        """Initialize self to handle abbreviations for the words
        in the sequence of strings full_names.  It is an error if
        a name appears twice in full_names."""
        "*** YOUR CODE HERE ***"
        self._full_names = full_names

    def complete(self, cmnd):
        """The member of my word list that the string cmnd
        abbreviates, if it exists and is unique.  cmnd abbreviates
        a string S in my word list if cmnd == S, or cmnd is a
        prefix of S and of no other command in my word list.
        Raises ValueError if there is no such S.
        >>> a = Abbrev(['continue', 'catch', 'next', 
        ...             'st', 'step', 'command'])
        >>> a.complete('ne')
        'next'
        >>> a.complete('co')
        Traceback (most recent call last):
           ...
        ValueError: not unique: 'co'
        >>> a.complete('st')
        'st'
        >>> a.complete('foo')
        Traceback (most recent call last):
           ...
        ValueError: unknown command: 'foo'
        """
        "*** YOUR CODE HERE ***"
        candidates = [name for name in self._full_names if name.startswith(cmnd)]
        if len(candidates) == 1:
            print(candidates[0].__repr__())
        elif len(candidates) == 0:
            raise ValueError('unknown command: {0}'.format(cmnd.__repr__()))
        elif len(candidates) > 1:
            full_names = [name for name in candidates if name == cmnd]
            if not full_names:
                raise ValueError('not unique: {0}'.format(cmnd.__repr__()))
            else:
                print(cmnd.__repr__())


    def minimal_abbreviation(self, cmnd):
        """The string, S, of shortest length such that
        self.complete(S) == cmnd.  
        >>> a = Abbrev(['continue', 'catch', 'next', 
        ...             'st', 'step', 'command'])
        >>> a.minimal_abbreviation('continue')
        'con'
        >>> a.minimal_abbreviation('next')
        'n'
        >>> a.minimal_abbreviation('step')
        'ste'
        >>> a.minimal_abbreviation('ste')
        Traceback (most recent call last):
           ...
        ValueError: unknown command: 'ste'
        """
        "*** YOUR CODE HERE ***"
        if cmnd not in self._full_names:
            raise ValueError('unknown command: {0}'.format(cmnd.__repr__()))
        for l in range(len(cmnd)):
            abbrv = cmnd[0:l+1]
            candidates = [name for name in self._full_names if name.startswith(abbrv)]
            if len(candidates) == 1:
                return abbrv


# Q7 Extra for Experts.

class ArgumentMonitor:
    """A general-purpose wrapper class that counts the number of times each
    method of a monitored object is called with each unique argument list.

    >>> B = Bank()
    >>> acct = B.make_account(1000)
    >>> mon_acct = ArgumentMonitor(acct, ['balance', 'withdraw', 'deposit'])
    >>> mon_acct.balance()
    1000
    >>> for i in range(10): mon_acct.deposit(100)
    >>> mon_acct.withdraw(20)
    >>> mon_acct.withdraw(10)
    >>> mon_acct.balance()
    1970
    >>> d = mon_acct.argument_counts('balance')
    >>> d[()]
    2
    >>> d = mon_acct.argument_counts('deposit')
    >>> list(d.items())
    [((100,), 10)]
    >>> d = mon_acct.argument_counts('withdraw')
    >>> d[(10,)]
    1
    >>> d[(20,)]
    1
    """

    def __init__(self, obj, operations):
        """An ArgumentMonitor that monitors the methods named in
        operations for obj."""
        "*** YOUR CODE HERE ***"

    "*** YOUR CODE HERE ***"


