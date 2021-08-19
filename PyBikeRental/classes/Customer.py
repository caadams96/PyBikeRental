import datetime
from datetime import datetime, timedelta

class Customer(object):
    """Functions to create a new customer and make a bike rental"""
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        
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

