numbers = [6, 3, 11, 4, 8, 2, 12, 9]

print("Original List :", numbers)

# Variable to store the sum of the list
total = 0

# Finding the sum
for value in numbers:
    total += value

# Calculate average
mean = total / len(numbers)

print("Sum =", total)
print("Average =", mean)

# Sorting the elements of the list
numbers.sort()

# Printing the first element
print("Smallest element is:", numbers[0])

# Printing the last element
print("Largest element is:", numbers[-1])
