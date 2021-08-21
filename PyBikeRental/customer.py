import datetime
from datetime import datetime, timedelta
from bikerental import BikeRental
last_id = 0
customers = []

class Customer(object):
    """description of class"""


    def __init__(self,name):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.bikeModelRented = ""
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        #Added variables
        self.name = name
        global last_id
        last_id += 1
        self.id = last_id
        #for validation for rental menu class function GetRentalTime
        self.customerRentalTime = 0

    def getBikeModel(self,choice):
        self.bikeModelRented = choice

    def getRentalBasis(self,choice):
        self.rentalBasis = choice

    def requestRentalTime(self):
        rentTime = 0
        #Ask user
        customerRentalTime = input("How long do you plan on renting the bike out? ")
        try:
            customerRentalTime = int(customerRentalTime)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if customerRentalTime < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            if self.rentalBasis == 1:
                rentTime = customerRentalTime
            elif self.rentalBasis == 2 or self.rentalBasis == 3:
                rentTime = customerRentalTime
            self.customerRentalTime += 1



        rentalTime = datetime.now() + timedelta(rentTime)
        self.rentalTime = rentalTime

        return self.rentalTime


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




            
            