# Function to add a new student record
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    score = input("Enter student score: ")

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{score}\n")
    print("Student record added successfully.")

# Function to display all student records
def display_students():
    try:
        with open("students.txt", "r") as file:
            print("Student Records:")
            for line in file:
                student_id, name, score = line.strip().split(',')
                print(f"ID: {student_id}, Name: {name}, Score: {score}")
    except FileNotFoundError:
        print("No student records found.")

# Function to update a student record
def update_student():
    student_id = input("Enter the student ID to update: ")
    new_score = input("Enter the new score: ")

    updated_records = []
    try:
        with open("students.txt", "r") as file:
            found = False
            for line in file:
                s_id, name, score = line.strip().split(',')
                if s_id == student_id:
                    found = True
                    updated_records.append(f"{s_id},{name},{new_score}\n")
                else:
                    updated_records.append(line)

            if found:
                with open("students.txt", "w") as file:
                    file.writelines(updated_records)
                print("Student record updated successfully.")
            else:
                print("Student ID not found.")
    except FileNotFoundError:
        print("No student records found.")

# Function to delete a student record
def delete_student():
    student_id = input("Enter the student ID to delete: ")

    updated_records = []
    try:
        with open("students.txt", "r") as file:
            found = False
            for line in file:
                s_id, name, score = line.strip().split(',')
                if s_id == student_id:
                    found = True
                else:
                    updated_records.append(line)

            if found:
                with open("students.txt", "w") as file:
                    file.writelines(updated_records)
                print("Student record deleted successfully.")
            else:
                print("Student ID not found.")
    except FileNotFoundError:
        print("No student records found.")

# Menu for student management
while True:
    print("\nStudent Management Menu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
