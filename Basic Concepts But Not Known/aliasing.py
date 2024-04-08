# Creating a list with random real numbers
nums = [1,2,3]

# Keeping the list in another variable
temp = nums

# Appending new element to the new variable list
temp.append(5)

print(f"List: {nums}")
# We can see that the main list is also changed

"""
    When we keep a list in another variable, then we are creating another referece to that list.
    but not creating a new list same to that one. So, if we make change into the list using one variable,
    then both of the variables referencing the list will show the same changes. This thing is called aliasing.
"""

# We can create a new list in a new variable using these.
temp = [item for item in nums]
temp.append(7)
print(f"List 1: {nums}")
print(f"List 2: {temp}")



