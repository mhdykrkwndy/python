class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    def add_passenger(self, name):
        if self.open_seat()==0:
            return False
        else:
            self.passengers.append(name)
            return True  
    def open_seat(self):
        return self.capacity - len(self.passengers)   


flight = Flight(2) 
pepole=["mahdi","ali","reza","sogand"]
for person in pepole:
    succes=flight.add_passenger(person)
    if succes:
        print(f"add {person} was succesful")
    else:
        print(f"add {person} was not succesful")
                    
print(f"new list is {flight.passengers}")        


    