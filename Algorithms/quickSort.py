
def QuickSort(numbers: list[int]):

    print(f'Starting point: - {numbers}')

    if len(numbers) == 1:
        print("Terminative case")
        return
    print("After Returning it came here...")
    
    pivot = 0
    j = len(numbers)-1

    print(f"Pivot element: {numbers[pivot]}")
    print(f"Comparison element: {numbers[j]}")

    leftFlag = 0

    while pivot != j:
        
        # print(f"Element : {numbers[j]}")
        
        if (numbers[pivot] > numbers[j] and leftFlag == 0) or (numbers[pivot] < numbers[j] and leftFlag == 1) :
            
            # print("Swipping needed")
            # print(f"Left Flag: {leftFlag}")
            
            temp = numbers[pivot]
            numbers[pivot] = numbers[j]
            numbers[j] = temp
            
            # print(f"After swapping numbers: {numbers}")
            
            temp = pivot
            pivot = j 
            j = temp
            
            # print(f"After swapping pivot: {pivot}, comparison index at: {j}")
        
        if pivot > j:
            
            # print('Now j will be incremented')
            
            j += 1
            leftFlag = 1
        else:
            j -= 1
            leftFlag = 0
    
    # print(pivot)
    print(f"After swapping: {numbers}")
    
    print(f"Previous: {numbers[0:pivot]}")
    numbers[0:pivot] = QuickSort(numbers=numbers[0:pivot])
    numbers[pivot+1:len(numbers)] = QuickSort(numbers=numbers[pivot+1:len(numbers)])
    
    print(f"After Divide and Conquer: {numbers}\n")
    
    return numbers

def main():
    numbers = [3,0,1,8,7,2,5,4,9,6]
    numbers = QuickSort(numbers=numbers)

    # numbers[0:3] = [0,1,2]
    print(numbers)

if __name__ == "__main__":
    main()