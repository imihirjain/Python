import random

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def getStatus(slf):
        print(f"Train no. {slf.trainNo} is running on time")

    def book(self,fro,to):
        print(f"Ticket is booked in train no:- {self.trainNo} from {fro} to {to}")

    def getFare(mihir,fro,to):
        print(f"The price of ticket of train number {mihir.trainNo} from {fro} to {to} is {random.randint(222,5555)}")

t=Train(12401)
t.book("Delhi", "Katra")
t.getFare("Delhi", "Katra")
t.getStatus()
