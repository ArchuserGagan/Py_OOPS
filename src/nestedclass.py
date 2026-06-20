# nested class ia a class defined within another class
#class outer
#   class inner:
#benifits : allows you to logically group classes  that are closely related
# encapsulate private details that arent relevent outside the outer class
# keeps the namespace clean; reduce the possibility of naming conflicts
class Company:
    class Employee:
        def __init__(self, name, postion) -> None:
            self.name = name
            self.postion = postion
        
        def get_details(self) -> str:
            return f"{self.name} {self.postion}"

    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self, name, postion) -> None:
        new_employee = self.Employee(name, postion)
        self.employees.append(new_employee)

    def list_employees(self) -> list:
        return [employee.get_details() for employee in self.employees]

# class Nonprofit: 
#     class Employee:
#         print("this is the first class" )   

company2 = Company("GreyCloverLabs")
company = Company("GregyClover")
company.add_employee("Gagan", "CEO")
company.add_employee("Danish", "CTO")
company.add_employee("xyz", "sales rep")


company2.add_employee("gagan", "CEO")
company2.add_employee("danish", "cto")

for employee in company2.list_employees():
    print(employee)

for employee in company.list_employees():
    print(employee)

