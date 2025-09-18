## With thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(2)
    print(f"Number: {number}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(print_numbers, numbers)


### With Process Pool Executor
from concurrent.futures import ProcessPoolExecutor

def square(n):
    time.sleep(2)
    return n * n

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square, numbers))
        print(results)