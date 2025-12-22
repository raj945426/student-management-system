# Student Management System
# Beginner Python Project

students = []


def add_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        while True:
            try:
                mark = int(input(f"Enter mark {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks should be between 0 and 100")
            except ValueError:
                print("❌ Please enter a valid number")

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("✅ Student added successfully\n")


def calculate_average(marks):
    return sum(marks) / len(marks)


def display_students():
    if not students:
        print("❌ No students found\n")
        return

    print("\n--- Student List ---")
    for student in students:
        avg = calculate_average(student["marks"])
        print(f"Name: {student['name']} | Marks: {student['marks']} | Average: {avg:.2f}")
    print()


def find_topper():
    if not students:
        print("❌ No students found\n")
        return

    topper = students[0]
    highest_avg = calculate_average(topper["marks"])

    for student in students:
        avg = calculate_average(student["marks"])
        if avg > highest_avg:
            highest_avg = avg
            topper = student

    print(f"🏆 Topper: {topper['name']} with average {highest_avg:.2f}\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Find Topper")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            find_topper()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# Program starts here
menu()
