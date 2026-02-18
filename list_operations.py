# list_operations.py

# Create list of 10 numbers
numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Largest and smallest
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

# Sum of elements
print("Sum of numbers:", sum(numbers))

# Remove duplicates
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

# Sort list
unique_numbers.sort()
print("Sorted List (Ascending):", unique_numbers)
