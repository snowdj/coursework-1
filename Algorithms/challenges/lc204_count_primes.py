"""
Time: O(n*sqrt(n))
Space: O(n)

Description:

Count the number of prime numbers less than a non-negative number, n

click to show more hints.

References:
How Many Primes Are There?
https://primes.utm.edu/howmany.html

Sieve of Eratosthenes
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


# Sieve of Eratosthenes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[:2] = [False, False]
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(range(i*i, n, i))
        return sum(primes)
