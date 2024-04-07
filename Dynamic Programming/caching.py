

def memoizedAddTo80(n):
    cache = {}
    def add():
        if cache.get(n):
            return cache[n]
        else:
            print("Long time")
            cache[n] = n + 80
            return cache[n]
    return add()

ca = {
    "a": 5
}
print(ca.get("a"))


print(f"1, {memoizedAddTo80(5)}")
print(f"2, {memoizedAddTo80(5)}")