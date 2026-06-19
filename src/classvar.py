class Student:

    class_year = 2024  #share among all classess
    numofstud = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Student.numofstud += 1


student1 = Student("gagan", 20)
student2 = Student("Danish", 20)               #here student2 is self

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.numofstud)
