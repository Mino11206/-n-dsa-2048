def countPrimes(n):
    """Return the number of prime numbers less than or equal to n."""
    if n < 2:
        return 0

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sum(sieve)