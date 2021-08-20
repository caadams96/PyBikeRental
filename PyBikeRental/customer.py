import datetime
from datetime import datetime, timedelta
    
last_id = 0
class Customer(object):
    """description of class"""


    def __init__(self,Name):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.Name = Name 
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        last_id += 1
        self.id = last_id
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent? ")
        
        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
  
        