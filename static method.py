class Employee:
    company = "Google"

    def __init__(self ,name , salary , unit  ):
        self.salary = salary
        self.name = name
        self.unit = unit
        print(f"{name} is working at {Employee.company} and his salary is {salary} , unit is {unit}" )

    
    def getSalary(self , signature):
        print(f"{self.salary} {signature} ")
    

    @staticmethod
    def greet():
        print("Hello every one present here")

gaurav = Employee("Gaurav" , "100k"  , "Youtube")
gaurav.getSalary("Develpoer")
gaurav.greet()