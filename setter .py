class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please enter the credential "
        return f"{self.fname}.{self.lname}@google.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


gaurav_garwal = Employee("Gaurav", "Garwal")
print(gaurav_garwal.email)
gaurav_garwal.fname = "India"
print(gaurav_garwal.email)


gaurav_garwal.email = "this.that@google.com"
print(gaurav_garwal.fname)
print(gaurav_garwal.lname)


del gaurav_garwal.email
print(gaurav_garwal.email)
gaurav_garwal.email = "New.Email@google.com"
print(gaurav_garwal.email)

