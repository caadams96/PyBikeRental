import datetime
from datetime import datetime, timedelta
   
class BikeRental(object):
    """description of class"""


    def __init__(self,MountainBikes=0,RoadBikes=0,TouringBikes=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.MountainBikes = MountainBikes
        self.RoadBikes = RoadBikes
        self.TouringBikes =  TouringBikes 
        self.stock = MountainBikes + RoadBikes + TouringBikes

        self.bikeModel = ""
        income = 0
        self.income = income
        
        self.bikesRented = 0

    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("\n")
        print("We have currently {} bikes available to rent.".format(self.stock))
        print("________________________________________________________________")
        print(f""" 
Mountain Model: {format(self.MountainBikes)}                   
Road Model: {format(self.RoadBikes)}                
Touring Model: {format(self.TouringBikes)}
        """)
        return self.stock

    #/////////////////////////////////////////////////////////////////
    #Function
    #/////////////////////////////////////////////////////////////////

    def rentBikeOnHourlyBasis(self, n, model):
        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        # do not rent bike is stock is less than requested bikes
        
        mBikeStock = self.MountainBikes
        rBikeStock = self.RoadBikes
        tBikeStock = self.TouringBikes
        if n <= 0:
            print("Number of bikes should be positive!")
            return True
        elif  model == "MountainBike":
            if n > mBikeStock:
                print("Sorry! We have currently {} mountain bikes available to rent.".format(self.MountainBikes))
                return True  
            else:
                self.MountainBikes -= n
                self.stock -= n
                self.bikesRented += n

        elif  model == "RoadBike":
            if n > rBikeStock:
                print("Sorry! We have currently {} road bikes available to rent.".format(self.RoadBikes))
                return True 
            else:
                self.RoadBikes -= n
                self.stock -= n
                self.bikesRented += n

        elif  model == "TouringBike":
            if n > tBikeStock:
                print("Sorry! We have currently {} touring bikes available to rent.".format(self.TouringBikes))
                return True
            else:
                self.TouringBikes -= n
                self.stock -= n
                self.bikesRented += n

    
        now = datetime.now()                      
        print("You have rented {} {}(s) on hourly basis today at {} hours.".format(n,model,now.hour))
        print("You will be charged $5 for each hour per bike.")
        print("We hope that you enjoy our service.")


    #/////////////////////////////////////////////////////////////////
    #Function
    #/////////////////////////////////////////////////////////////////


    def rentBikeOnDailyBasis(self, n, model):
        """
        Rents a bike on daily basis to a customer.
        """
        
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        mBikeStock = self.MountainBikes
        rBikeStock = self.RoadBikes
        tBikeStock = self.TouringBikes
    
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif  model == "MountainBike":
            if n > mBikeStock:
                print("Sorry! We have currently {} mountain bikes available to rent.".format(self.MountainBikes))
                return None  
            else:
                self.MountainBikes -= n
                self.stock -= n
                self.bikesRented += n

        elif  model == "RoadBike":
            if n > rBikeStock:
                print("Sorry! We have currently {} road bikes available to rent.".format(self.RoadBikes))
                return None 
            else:
                self.RoadBikes -= n
                self.stock -= n
                self.bikesRented += n

        elif  model == "TouringBike":
            if n > tBikeStock:
                print("Sorry! We have currently {} touring bikes available to rent.".format(self.TouringBikes))
                return None
            else:
                self.TouringBikes -= n
                self.stock -= n
                self.bikesRented += n


    
        now = datetime.now()                      
        print("You have rented {} {}(s) on hourly basis today at {} hours.".format(n,model,now.hour))
        print("You will be charged $5 for each hour per bike.")
        print("We hope that you enjoy our service.")

    #/////////////////////////////////////////////////////////////////
    #Function
    #/////////////////////////////////////////////////////////////////

    def rentBikeOnWeeklyBasis(self, n, model):
        """
        Rents a bike on weekly basis to a customer.
        """
        mBikeStock = self.MountainBikes
        rBikeStock = self.RoadBikes
        tBikeStock = self.TouringBikes
    
       
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif  model == "MountainBike":
            if n > mBikeStock:
                print("Sorry! We have currently {} mountain bikes available to rent.".format(self.MountainBikes))
                return None  
            else:
                self.MountainBikes -= n
                self.stock -= n
                self.bikesRented += n


        elif  model == "RoadBike":
            if n > rBikeStock:
                print("Sorry! We have currently {} road bikes available to rent.".format(self.RoadBikes))
                return None 
            else:
                self.RoadBikes -= n
                self.stock -= n
                self.bikesRented += n


        elif  model == "TouringBike":
            if n > tBikeStock:
                print("Sorry! We have currently {} touring bikes available to rent.".format(self.TouringBikes))
                return None
            else:
                self.TouringBikes -= n
                self.stock -= n
                self.bikesRented += n

    
        now = datetime.now()  
        
        print("You have rented {} {}(s) on hourly basis today at {} hours.".format(n,model,now.hour))
        print("You will be charged $5 for each hour per bike.")
        print("We hope that you enjoy our service.")


    def showIncome(self):
        
        print(f"income {self.income}")

    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes, bikeModel = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes and bikeModel:
            if bikeModel == "MountainBike":
                self.MountainBikes += numOfBikes
                self.stock += numOfBikes
            elif bikeModel == "RoadBike":
                self.RoadBikes += numOfBikes
                self.stock += numOfBikes
            elif bike == "TouringBike":
                self.TouringBikes += numOfBikes
                self.stock += numOfBikes

            now = datetime.now()
            rentalPeriod = now - rentalTime
            
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
                self.income += bill
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
                self.income += bill
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
                self.income += bill
            
            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
                self.income += bill
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        
        else:
            print("Are you sure you rented a bike with us?")
            return None