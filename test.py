import time

TARGET = 25646546541654650
MAX_NUMBER = 99999999999999999


def binary_search():
    low, high = 1, MAX_NUMBER
    attempts = 0
    start = time.perf_counter()

    while low <= high:
        attempts += 1
        mid = (low + high) // 2

        if mid == TARGET:
            elapsed = time.perf_counter() - start
            print(f"[Binary Search] Found: {mid}")
            print(f"[Binary Search] Attempts: {attempts}")
            print(f"[Binary Search] Time: {elapsed:.8f} seconds")
            return
        elif mid < TARGET:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == "__main__":
    binary_search()