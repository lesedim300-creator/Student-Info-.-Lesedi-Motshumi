# List of student dictionaries

students = [ 
{"name": "Lesedi", "maths": 85, "english": 78, "science": 90}, 
{"name": "Thabo", "maths": 65, "english": 70, "science": 68}, 
{"name": "Vanessa", "maths": 45, "english": 55, "science": 50}, 
{"name": "Ofentse", "maths": 92, "english": 88, "science": 95},
{"name": "Bella", "maths": 35, "english": 40, "science": 38}
]

results = []
total_average = 0
highest = 0
lowest = 100

# Process each student

for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

# Assign grade

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

# Assign status

if average >= 50: 
    grade = "Pass"
else:
    grade = "Fail"

# Save results

status = "Pass" if average >= 50 else "Fail"

results.append({
    "name": student ["name"],
    "average": round(average, 2),
    "grade": grade,
    "status": status
})

total_average += average

if average > highest:
    highest = average

if average < lowest:
    lowest = average

# Class statistics

class_average = total_average / len(results)

# Display report

print("Class Report")
for result in results:
    print(f"Name : {result['name']}")
    print(f"Average : {result['average']}")
    print(f"Grade : {result['grade']}")
    print(f"Status : {result['status']}")

print("___")

print(f"Class average : {class_average:.2f}")
print(f"Lowest Mark : {lowest:.2f}")

# Search for students

while True:
    search = input("Enter a student name to search (or 'exit' to quit): ")

    if search.lower() == "exit":
        print("Goodbye!")
        break

    found = False

    for result in results: 
        if result["name"].lower() == search.lower():
            print("Student Found")
            print(f"Name : {result['name']}")
            print(f"Average : {result['average']}")
            print(f"Grade : {result['grade']}")
            print(f"Status : {result['status']}")
            found = True
            break
    if not found:
        print("Student not found.")