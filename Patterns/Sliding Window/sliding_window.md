# Sliding Window

## Naive Way (Brute Force)
For each possible window of size ```k```, compute the sum and track the max. ```(O(n*k))```
```
array = [2,1,5,1,3,2]
window_size = 3
max_sum = float('-inf')

# Only go till len(array) - window_size + 1
for i in range(len(array) - window_size + 1):
    temp = sum(array[i:i+window_size])
    max_sum = max(max_sum, temp)

print(max_sum)  # Output: 9
```


## Key Insights for Sliding Window Problems:

1. **Valid window positions:** For an array of length ```n``` and window size ```k```, valid starting positions are from index ```0``` to ```n-k``` (inclusive). This gives you ```n-k+1``` windows total.

2. **Visualize the windows:**
```
Array: [2, 1, 5, 1, 3, 2]
Window 1: [2, 1, 5] → sum = 8
Window 2:    [1, 5, 1] → sum = 7
Window 3:       [5, 1, 3] → sum = 9
Window 4:          [1, 3, 2] → sum = 6
```

3. **Optimized sliding window technique:** Instead of recalculating the entire sum each time, you can:
```
# More efficient approach
array = [2, 1, 5, 1, 3, 2]
window_size = 3

# Calculate first window sum
window_sum = sum(array[:window_size])
max_sum = window_sum

# Slide the window
for i in range(window_size, len(array)):
    # Remove leftmost element of previous window, add rightmost of new window
    window_sum = window_sum - array[i-window_size] + array[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)  # Output: 9 
```

## Mental Model for Future Problems:
When you see sliding window problems:
1. **Ask yourself: Is it a fixed-size window or variable size window?**
    - Fixed size ⇒ Use rolling sum technique (like above).
    - Variable size (e.g., "smallest subarray with sum ≥ X") ⇒ Use two pointers and adjust window.
2. **Avoid recomputation.**
    Always see if you can reuse previous computations instead of recalculating (saves time!).
3. **Loop Range Control.**
    If window size is ``k``, only run loop till ```len(array) - k```.
3. **Think about what happens as the window moves:**
    - **Leftmost element goes out** → subtract it.
    - **Next element comes in on right** → add it.
4. **Consider optimization:** Can you update the result incrementally instead of recalculating everything?

Remember: The key is to ensure your loop bounds prevent accessing indices outside the array. Always think: "If I start my window at position ```i```, can I safely access all elements up to ```i + window_size - 1```?"


## 💡How to Think About Variable-Window Problems
1. **Identify the core property:**
- Fixed-size sliding window = max/min sum of size k
- Variable-size = usually involves prefix sums, remainders, or two pointers.
2. **Avoid nested recomputation:**
- If you find yourself manually summing subarrays in O(n²), think:
```
    "Can I reuse a previous sum (prefix sum)?"
    "Can I use a hash map to track frequency?"
```
3. Pattern recognition:
- "Subarray sum equals k" ✅ prefix sums + hashmap of counts.
- "Subarray divisible by k" ✅ prefix sum % k remainders + hashmap.
- "Longest subarray with condition" ✅ two pointers / sliding boundaries. 

4. Whenever you see **"subarray sum"** problems:
- Think **prefix sums**.
- If divisibility/modulo is involved, think **store remainders in hashmap**.
- If exact sums are involved, think **store prefix_sum - target in hashmap**.

## Common Optimization Techniques:
1. **Prefix/Suffix Arrays:** Pre-compute cumulative values
2. **Hash Maps:** Track frequency of values/remainders
3. **Two Pointers:** For problems with monotonic properties
4. **Sliding Window with Hash Map:** For substring problems with conditions


## Key Takeaway
When you see "all subarrays" and face ``TLE`` with ```O(n²)``` or ```O(n³)``` solutions, think:
1. Can I avoid recalculating from scratch?
2. What information can I reuse?
3. Is there a mathematical relationship I can exploit?