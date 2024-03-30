

def binarySearch(arr, n, start, end):
    print(start,  end)
    if start > end:
        return -1
    mid = int((start+end)/2)
    if n == arr[mid]:
        return mid
    elif n < arr[mid]:
        return binarySearch(arr, n, start=start, end=mid-1)
    elif n > arr[mid]:
        return binarySearch(arr=arr, n=n, start=mid+1, end=end)

def main():
    arr = [5, 7, 9, 13, 32, 33, 42, 54, 56, 88]
    val = binarySearch(arr=arr, n=-1, start=0, end=len(arr)-1)
    print(val)


if __name__ == "__main__":
    main()

