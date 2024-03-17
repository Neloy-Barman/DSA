
def fibonacciIterative(n: int) -> int:
    seq = [0,1]
    i = 2
    while i <= n:
        seq.append(seq[i-1]+seq[i-2])
        i += 1
    return seq[n] 

# Mine
def fibonacciRecursive(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    n -= 1
    return fibonacciRecursive(n)+fibonacciRecursive(n-1)

# From video
# def fibonacciRecursive(n: int) -> int:
#     if n < 2:
#         return n
#     return fibonacciRecursive(n-2)+fibonacciRecursive(n-1)

def main():
    
    out = fibonacciIterative(10)
    print(out)

    out = fibonacciRecursive(40)
    print(out)


if __name__ == "__main__":
    main()