#Task 4: File Handling

#4.1 Create a text file named ai_students.txt.
#4.2 Write details of at least 5 students (name, marks, grade). 
students = [
    {"name": "Sriram", "marks": 85, "grade": "B"},
    {"name": "Krishna", "marks": 92, "grade": "A"},
    {"name": "Sai", "marks": 68, "grade": "C"},
    {"name": "Arun", "marks": 77, "grade": "B"},
    {"name": "Sneha", "marks": 95, "grade": "A"}
]

with open("ai_students.txt", "w") as f:
    for s in students:
        f.write(f"{s['name']},{s['marks']},{s['grade']}\n")
        
#4.3 Read the file and display students who scored above 75 marks.
print("Students Scored above 75")
with open("ai_students.txt", "r") as f:
    for line in f:
        name, marks, grade = line.strip().split(",")
        if int(marks) > 75:
            print(f"{name} - Marks: {marks}, Grade: {grade}")
