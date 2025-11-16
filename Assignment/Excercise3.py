#Exercise 3 : Student Marks Processor

marks.txt
[regno exam_mark coursework_mark]
1001     90          100
1002     77          100
1003     50          60
1004     67          70   
...................................

def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

students = []

try:
    with open("marks.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                regno = parts[0]
                exam = float(parts[1])
                coursework = float(parts[2])
                overall = (exam * 0.6) + (coursework * 0.4)
                grade = calculate_grade(overall)
                students.append([regno, exam, coursework, overall, grade])
            else:
                print("Skipping invalid line:", line)

    # Sort by overall mark (highest first)
    students.sort(key=lambda x: x[3], reverse=True)

    # Write to output file
    with open("results.txt", "w") as out:
        out.write("RegNo Exam Coursework Overall Grade\n")
        for s in students:
            out.write(f"{s[0]} {s[1]} {s[2]} {s[3]:.2f} {s[4]}\n")

    # Grade stats
    grades = [s[4] for s in students]
    print("Grade distribution:")
    for g in ["A", "B", "C", "D", "F"]:
        print(f"{g}: {grades.count(g)}")

    print("\nDone! Check 'results.txt' for the sorted list.")

except FileNotFoundError:
    print("marks.txt not found!")
except Exception as e:
    print("Something went wrong:", e)
