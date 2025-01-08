hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
midd_int = int(input("enter number:"))
hat_list.remove(hat_list[len(hat_list)-1])
hat_list.insert(2,midd_int)

# Step 2: write a line of code that removes the last element from the list.
hat_list.pop()
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)
