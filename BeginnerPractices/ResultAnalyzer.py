# 2. Student Result Analyzer
# Features: Calculate average of 5 subjects, Find topper, Rank students, Show pass/fail
# Concepts: Lists, Sorting, Functions, Dictionaries
# Challenge: Handle ties in ranks

# Defining Variables
students = []
# This function adds a student and their marks to the students list.
def AddStudent(name, marks):
    student = {"name": name, "marks": marks}
    students.append(student)
    print(f"{name} has been added with marks {marks}.")
# This function calculates the average marks of a student.
def CalculateAverage(totalmarks):
    average = totalmarks / 5
    return average 
# This function finds the topper among the students.
def FindTopper():
    if not students:
        print("No students added yet.")
        return None
    topper = max(students, key=lambda s: sum(s["marks"]))
    return topper
# This function ranks the students based on their total marks.
def RankStudents():
    ranked_students = sorted(students, key=lambda s: sum(s["marks"]), reverse=True)
    return ranked_students
# This function shows whether a student has passed or failed based on their average marks.
def ShowPassFail(student):
    average = CalculateAverage(sum(student["marks"]))
    
    if average >= 40:
        return "Pass"
    else:
        return "Fail"
# Main Program Loop
while True:
    print("\nStudent Result Analyzer")
    print("1. Student Registry")
    print("2. Find Topper")
    print("3. Rank Students")
    print("4. Show Pass/Fail")
    print("5. Average Marks of a Student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = []
        for i in range(5):
            mark = float(input(f"Enter marks for each subjects {i+1}: "))
            marks.append(mark)
        AddStudent(name, marks)
    
    elif choice == "2":
        topper = FindTopper()
        if topper:
            print(f"Topper: {topper['name']} with total marks {sum(topper['marks'])}")
    
    elif choice == "3":
        ranked_students = RankStudents()
        print("Ranked Students:")
        for idx, student in enumerate(ranked_students, start=1):
            print(f"{idx}. {student['name']} - Total Marks: {sum(student['marks'])}")
    
    elif choice == "4":
        name = input("Enter student name to check pass/fail: ")
        student = next((s for s in students if s["name"].lower() == name.lower()), None)
        if student:
            result = ShowPassFail(student)
            print(f"{student['name']} has {result}.")
        else:
            print("Student not found.")
    
    elif choice == "5":
        name = input("Enter student name to check average marks: ")
        student = next((s for s in students if s["name"].lower() == name.lower()), None)
        if student:
            average = CalculateAverage(sum(student["marks"]))
            print(f"{student['name']} has an average of {average:.2f}.")
        else:
            print("Student not found.")
    
    elif choice == "6":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")