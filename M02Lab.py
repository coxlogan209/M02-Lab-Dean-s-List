#Logan Cox M02Lab.py This app requires a student's first name, last name, and gpa. It will then determine if they are on the Dean's list or honor roll.
# lastName is the student's last name
# firstName is the student's first name
# GPA is the student's gpa

lastName = input("Enter students last name or 'ZZZ' to quit: ")
while lastName != 'ZZZ':
    firstName = input("Enter student's first name: ")
    GPA = float(input("Enter student's GPA: "))
    if GPA < 3.25:
        print("This student has not achieved Dean's List OR Honor Roll.")
    elif GPA < 3.5:
        print(firstName, lastName, "has achieved Honor Roll")
    else:
        print(firstName, lastName, "has achieved Dean's List")
    lastName = input("Enter students last name or 'ZZZ' to quit: ")
