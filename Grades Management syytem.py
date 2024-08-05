 #Step 1: Create a list of Students and their grades as well as their grade
students = [
    ["Alice", 85, 90, 88 ],
    ["Bob", 78, 85, 80],
    ["Charlie", 78, 85, 80],
    ["Diana", 88, 87, 89],
    ["Eve", 76, 80, 79]
]

#def display_all():
    #print("\nStudents")
    #print(f'{"Name":<10} {"Assignment Mark":<16 } {"Test Mark":<10} {"Exam Mark":<10}')
    #print("="*46)
def display_all():
    print("\nStudents:")
    print(f"{"Name":<10} {'Assignment Mark':<16} {'Test Mark':<10} {'Exam Mark':<10}")
    print("="*48)
    for student in students:
        (name, assignment, test, exam) = student
        print(f"{name:<10} {assignment:<16} {test:<10} {exam:<10}")

#display_all()

def add_student():
    name = input("Enter name: ")
    assignment = int(input("Enter assignment mark: "))
    test = int(input("Enter test mark: "))
    exam = int(input("Enter exam mark: "))
    students.append([name, assignment, test, exam])
    print("Student has been added.")
    display_all()

add_student()