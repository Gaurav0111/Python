class Parent:

    def __init__(self , txt) :
        self.message = txt

    def printmessage(self):
        print(self.message)

class Child(Parent):
    # def __init__(self, txt):
    #     super().__init__(txt)

    def printmessage(self):
        super().printmessage()
        # print(self.message)

gaurav = Child("hello , and welcome")
gaurav.printmessage()