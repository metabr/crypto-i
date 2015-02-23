#!/usr/bin/env python

import gmpy2
from gmpy2 import mpz

N = mpz('72006226374735042527956443552558373833808445147399984182665305798191\
        63556901883377904234086641876639384851752649940178970835240791356868\
        77441155132015188279331812309091996246361896836573643119174094961348\
        52463970788523879939683923036467667022162701835329944324119217381272\
        9276147530748597302192751375739387929')

A = gmpy2.isqrt(24 * N) + 1
print "A = %d" % A

x = gmpy2.isqrt((A ** 2) - (24 * N))
print "x = %d" % x

p = gmpy2.div(A + x, 4)
q = gmpy2.div(A - x, 6)


if (p * q) == N:
    print "p = %d" % p
    print "q = %d" % q
