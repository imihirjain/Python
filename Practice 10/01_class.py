class Employee:
    language = "C++"
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am __init__ dunder method which is called when any object is created")
    
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

# mihir = Employee();
# mihir.language = "Python" 
# print(mihir.salary, mihir.language)
# mihir.getInfo( )
# mihir.greet()
# Employee.getInfo(mihir)

rajneesh = Employee("Rajneesh", 13000000, "C#")
print(rajneesh.name, rajneesh.salary, rajneesh.language)


# instance object takes preference to class object
