import multiprocessing
import time
import sys
import math


sys.set_int_max_str_digits(1000000)

def factorial(n):
    print(f"Calculating factorial of {n}")
    result = math.factorial(n)
    print(f"Finished calculating factorial of {n}")
    return result

if __name__ == "__main__":
    numbers = [1000, 2000, 3000, 4000, 5000]
    
    start_time = time.time()
    
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(factorial, numbers)
    
    end_time = time.time()
    
    print(f"Factorials calculated: {[len(str(res)) for res in results]} digits")
    print(f"Time taken: {end_time - start_time} seconds")
