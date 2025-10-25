def sortArray(arr):
    """
    Sorts an array of integers in ascending order using the bubble sort algorithm.

    Parameters:
    arr (list): A list of integers to be sorted.

    Returns:
    list: A new list containing the sorted integers.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
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
