#static method is  a method that is belong to a class rather than any object from that class (instance) usually used for general
# utility functions

#Instance methods = best for operations on instance of class(object)
#static methods = best for utility functions that do not need access to class data
##basically class se lena dena nhi

class Employee:

    def __init__(self, name, position) -> None:
        self.name = name
        self.positon = position

    #instance method
    def get_info(self) -> str:
        return f"{self.name} = {self.positon}"
    
    #staticmethod
    @staticmethod
    def is_valid_postion(position) -> bool: #doesnt have self
        valid_positions = ["Manager", "CEO", "salesrep", "CTO"]
        return position in valid_positions

employee1 = Employee("Gagan", "CEO")
employee2 = Employee("danish", "cto")
employee3 = Employee("xyz", "salesrep")
print(Employee.is_valid_postion("CEO"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())