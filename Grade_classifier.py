# Collect learner information

name = input("Enter learner's name: ")

mark1 = float(input("Enter Subject 1 mark: "))
mark2 = float(input("Enter Subject 2 mark: "))
mark3 = float(input("Enter Subject 3 mark: "))

# Calculate the average

average = (mark1 + mark2 + mark3) / 3

# Assign letter grade

if average >= 80: 
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass or fail status

if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Display report

print(f"Student Report Card")
print(f"Learner Name : {name}")
print(f"Subject 1 : {mark1}")

if mark1 < 40:
    print("   -> Needs Intervention")
print(f"Subject 2 : {mark2}")
if mark2 < 40:
    print("   -> Needs Intervention")
print(f"Subject 3 : {mark3}")
if mark3 < 40:
    print("   -> Needs Intervention")

print(f"Average : {average:.2f}")
print(f"Grade : {grade}")
print(f"Status : {status}")
