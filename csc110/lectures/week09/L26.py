"""CSC110 Lecture 26 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
import math
import random


####################################################################################################
# Exercise 1
####################################################################################################
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that
    gcd(a, b) == p * a + b * q.

    >>> extended_gcd(10, 3)
    (1, 1, -3)
    >>> extended_gcd(3, 10)
    (1, -3, 1)
    """
    x, y = a, b

    # Initialize px, qx, py, and qy
    px, qx = 1, 0
    py, qy = 0, 1

    while y != 0:
        # Loop invariant (we use naive_gcd to check that the gcd are correct)
        assert math.gcd(x, y) == math.gcd(a, b)
        assert x == px * a + qx * b
        assert y == py * a + qy * b

        q, r = divmod(x, y)  # quotient and remainder when a is divided by b

        x, y = y, r

        # Update px, qx, py, and qy
        px, qx, py, qy = py, qy, px - q * py, qx - q * qy

    return x, px, qx


def modular_inverse(a: int, n: int) -> int:
    """Return an inverse of a (mod n).

    The inverse returned should be between 0 and n-1, inclusive.

    Preconditions:
        - math.gcd(a, n) == 1

    >>> modular_inverse(10, 3)
    1
    >>> modular_inverse(3, 10)
    7
    """
    _, p, _ = extended_gcd(a, n)

    if p > 0:
        return p
    else:
        return n + p


def rsa_generate_key(p: int, q: int) -> \
        tuple[tuple[int, int, int], tuple[int, int]]:
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. The first tuple is the private key, containing (p, q, d).
      2. The second tuple is the public key, containing (n, e).

    Preconditions:
        - p and q are prime
        - p != q

    Hints:
        - If you choose a random number e between 2 and $\varphi(n)$, there isn't a guarantee that
        $gcd(e, \varphi(n)) = 1$. You can use the following pattern to keep picking random numbers
        until you get one that is coprime to $\varphi(n)$.

            e = ... # Pick an initial choice
            while math.gcd(e, ___) > 1:
                e = ... # Pick another random choice

        - You can re-use the functions we developed last week to compute the modular inverse.
    """
    phi_n = (p - 1) * (q - 1)

    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) > 1:
        e = random.randint(2, phi_n - 1)

    d = modular_inverse(e, phi_n)

    return((p, q, d), (p * q, e))


def rsa_encrypt(public_key: tuple[int, int], plaintext: int) -> int:
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. The first tuple is the private key, containing (p, q, d).
      2. The second tuple is the public key, containing (n, e).

    Preconditions:
        - is_prime(p)
        - is_prime(q)
        - p != q
    """
    n, e = public_key

    encrypted = (plaintext ** e) % n

    return encrypted


def rsa_decrypt(private_key: tuple[int, int, int], public_key: tuple[int, int],
                ciphertext: int) -> int:
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (p, q, d)
        - 0 < ciphertext < private_key[0] * private_key[1]
    """
    _, _, d = private_key
    n, _ = public_key

    decrypted = (ciphertext ** d) % n

    return decrypted


####################################################################################################
# Exercise 2
####################################################################################################
def my_pow(x: int, y: int) -> int:
    """Return x raised to the yth power."""
    power = 1
    if y >= 0:
        for _ in range(0, y):
            power = power * x
    else:
        for _ in range(y, 0):
            power = power / x

    return power


def modular_exponentiation(base: int, exponent: int, modulus: int):
    """Return base ** exponent mod modulus.

    Precondition:
        - base >= 1
        - exponent >= 1
        - modulus > 1
    """
    c = 1

    for _ in range(exponent):
        c = (c * base) % modulus

    return c
