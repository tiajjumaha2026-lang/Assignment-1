# student_marks.py

# Accept marks of 5 subjects
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / 5

# Display results
print("\nTotal Marks:", total)
print("Average Marks:", average)

# Grade calculation
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Result: Fail")
