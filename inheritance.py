class Employee:
    company = "Google"

    def __init__(self ,name , salary , unit  ):
        self.salary = salary
        self.name = name
        self.unit = unit
        print(f"{name} is working at {Employee.company} and his salary is {salary} , unit is {unit}" )

    
    def getSalary(self):
        print(f"{self.salary}")

class Labour():
    def __init__(self , name ,salaryy , unnit) :
        self.name = name
        self.salaryy = salaryy
        self.unnit = unnit

    def getInfo(self):
        print(f"The unit off employee {self.name} is {self.unnit}")    


class hellow(  Employee , Labour  ):

    def getInfo(self):
        print(f"The unit of employee {self.name} is {self.unit}")    

gaurav = Employee("Gaurav" , "100k" , "Developer" )
karan = hellow("Karan" , "50k" , "Intern" )
# karan = Labour("Karan" , "50k" , "Intern" )
# Employee.getSalary(gaurav)   #  is equvalent to gaurav.getSalary()
gaurav.getSalary()
karan.getInfo()