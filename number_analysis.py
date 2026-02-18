# number_analysis.py

# Accept number from user
num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# Positive or Negative
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# Multiplication table
print("\nMultiplication Table:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
