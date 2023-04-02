#Logan Cox M02Lab.py This app requires a student's first name, last name, and gpa. It will then determine if they are on the Dean's list or honor roll.
# last_name is the student's last name
# first_name is the student's first name
# gpa is the student's gpa

while True:
    last_name = input("Enter student's last name (or ZZZ to quit): ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} made the Honor Roll!")
