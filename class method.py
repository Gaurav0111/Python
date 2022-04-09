class Employee:
    No_of_leaves = 50

    def __init__(self) :
        pass

    @classmethod
    def changeLeaves(cls , newleaves):
        cls.No_of_leaves = newleaves

gaurav = Employee()
gaurav.changeLeaves(5)

print(Employee.No_of_leaves)