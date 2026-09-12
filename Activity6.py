# Dictionary of students (id -> details)
students = {
    "s1": {"name": "Aarav", "class": "VI", "subject_integration": "english, science, maths"},
    "s2": {"name": "Meera", "class": "VI", "subject_integration": "english, science, maths"},
    "s3": {"name": "Aarav", "class": "VI", "subject_integration": "english, science, maths"},  # duplicate of s1
    "s4": {"name": "Rohan", "class": "VI", "subject_integration": "english, science, maths"},
}

unique_students = {}
checked_values = []  # using a list instead of set

for student_id, information in students.items():
    unique_key = (
        information["name"],
        information["class"],
        information["subject_integration"]
    )

    if unique_key not in checked_values:
        checked_values.append(unique_key)
        unique_students[student_id] = information

# Print output line by line
for student_id, details in unique_students.items():
    print(student_id, ":", details)
