"""9. You have been asked to create a class which models a student. The first name,
last name, and course for the student need to be set on creation of the object. The
university need to store the following information about the student:

• first name
• last name
• student ID - which is generated from the first letter of the forename and the surname
(e.g. for Bob Smith the ID would be bsmith)
• email address - which follows the format studentID@university.ac.uk (e.g. Bob Smith 
would be bsmith@university.ac.uk)
• course
• fees payment status
• whether the student is active (i.e. if they are still considered a student)

The university administrators will need to be able to change the student’s course,
record their fees as paid (the amount is not required to be stored), withdraw them as a
student (i.e. make them inactive), re-activate the student, print all the information
they hold on the student.
"""


class Student:
    def __init__(self, first_name, last_name, course):
        self.first_name = first_name
        self.last_name = last_name
        self.student_ID = (first_name[:1] + last_name).lower()
        self.email = self.student_ID + "@university.ac.uk"
        self.course = course
        self.fees_paid = False
        self.active = True

    def change_course(self, new_course):
        if new_course == self.course:
            print("Student is already on that course")
        else:
            self.course = new_course
            print("Student's course changed to", new_course)

    def fees_status(self, status):
        if status == self.fees_paid:
            print("Fees status is already set to", status)
        else:
            self.fees_paid = status
            print("Fees status changed to", status)

    def withdraw_student(self):
        if self.active:
            self.active = False
            print("Student has been withdrawn from the course")
        else:
            print("Student has already been withdrawn from the course")

    def unwithdraw_student(self):
        if not self.active:
            self.active = True
            print("Student has been unwithdrawn from the course")
        else:
            print("Student has already been marked as active")

    def retrieve_student_information(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Student ID: {self.student_ID}\n"
            f"Email address: {self.email}\n"
            f"Course: {self.course}\n"
            f"Fees paid: {self.fees_paid}\n"
            f"Active: {self.active}"
        )


student1 = Student("John", "Doe", "Law")
student1.change_course("Computer Science")
student1.withdraw_student()
student1.withdraw_student()
student1.unwithdraw_student()
student1.unwithdraw_student()
print(student1.retrieve_student_information())
