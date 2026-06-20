#classmethod = Allow operations related to the class itself
# take (cls ) as the first  parameter. which represents the class itself.



#instance methods best for operations on instances of the class (obj)
#static methods = best of utility functions that do not need access to class data
#Class methods = best for class-level data or require access to the class itself



class Student:
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self) -> str :
        return f"{self.name} {self.gpa}"
    


    @classmethod #to work with data in class like here we are working with count
    def get_count(cls) -> str:
        return f"total no of student : {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"avg gpa : {cls.total_gpa / cls.count:.2f}"


    
student1 = Student("gagan", 5)
student2 = Student("danish", 5)
student3 = Student("xyz", 2)
print(Student.get_count())
print(Student.get_average_gpa())
        

