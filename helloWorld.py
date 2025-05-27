class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers=[]
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        else :
            self.passengers.append(name)
            return True
    def open_seats(self):
        print(self.capacity-len(self.passengers))
        return self.capacity-len(self.passengers)  

flight=Flight(5)
people=["Sunil","Nisha","Madhav","Pranav","AN","OP"]
for person in people:
    success=flight.add_passenger(people)
    if success:
        print (f"Added {person} successfully")
    else:
        print (f"Couldn't add {person} as the flight is full")