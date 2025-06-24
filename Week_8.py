students = [
    {"name": "Alex", "grade": 85},
    {"name": "Maya", "grade": 72},
    {"name": "Chandu", "grade": 90},
    {"name": "Diya", "grade": 68},
    {"name": "Ram", "grade": 78}
]

print("Students with grade > 75:")
for student in students:
    if student["grade"] > 75:
        print(student["name"])