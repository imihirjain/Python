class Programmer:
    company = "Google"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

mihir = Programmer("Mihir", 120000000, 110040)
rajneesh = Programmer("Rajneesh", 4564654648, 110039)

print(mihir.name, mihir.salary, mihir.pin, mihir.company)
print(rajneesh.name, rajneesh.salary, rajneesh.pin, rajneesh.company)
