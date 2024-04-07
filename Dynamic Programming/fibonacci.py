import time

# Using normal approach 
# Time complexity: O(2^n)
# Space complexity: O(1)
calculations = 0
def fibonacci(n: int)  -> int:
    global calculations
    calculations +=1
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

start = time.time() 
number = fibonacci(40)
end = time.time()
total = end - start
print("Normal approach: ")
print(f"Total steps: {calculations}, time: {total}, Number: {number}")


# Using Dynamic programming approach
# Time complexity: O(n)
# Space complexity: O(n)
# Top - Down approach
calculations = 0
def memoizedFibonacci(n: int) -> int:
    cache = {}
    
    def fibonacci(n: int) -> int:
        global calculations
        calculations += 1
        if cache.get(n):
            return cache[n]
        else:
            if n < 2:
                cache[n] = n
                return cache[n]
            cache[n] = fibonacci(n-1)+fibonacci(n-2)
            return cache[n]
    return fibonacci(n)

start = time.time() 
number = memoizedFibonacci(40)
end = time.time()
total = end - start
print("Dynamic programming: ")
print("Top-Down approach: ")
print(f"Total steps: {calculations}, time: {total}, Number: {number}")


# Bottom - Up approach
calculations = 0
def memoizedFibonacci2(n: int) -> int:
    global calculations
    answer = [0,1]
    for i in range(2, n+1):
        calculations += 1
        answer.append(answer[i-1]+answer[i-2])
    return answer.pop()

start = time.time() 
number = memoizedFibonacci2(40)
end = time.time()
total = end - start
print("Bottom-Up approach: ")
print(f"Total steps: {calculations}, time: {total}, Number: {number}")