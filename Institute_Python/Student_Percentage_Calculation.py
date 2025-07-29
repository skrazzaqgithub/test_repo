class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def percentage(self):
        student_Name = input("Enter your name: ")
        total_marks = 100
        english = int(input("Enter your english marks: "))
        maths = int(input("Enter your maths marks: "))
        total = english+maths
        if total > 70%total_marks:
            print("You are from 9th standard and have passed with first class")
        elif total > 50%total_marks:
            print("You are from 9th standard and have passed with second class")
        else:
            print("You are failed")
sobj = Student("abdul", 27)
sobj = Student("razzaq", 31)
print("Your name is : ", sobj.name, "your age is :", sobj.age)
sobj.percentage()