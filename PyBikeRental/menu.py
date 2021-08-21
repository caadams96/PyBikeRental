import sys
import datetime
from datetime import datetime, timedelta
from bikerental import BikeRental
from customer import Customer
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#WORK IN PROGRESS
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#************************************************
#//Base Class: Menu
#
#************************************************ 
class Menu(object):

    def __init__(self):
        pass
    #************************************************
    #//Function Run
    #
    #************************************************ 
    def Run(self):
        self.Menu()
        global strValidated 
        
        strValidated = bool(False)
        while strValidated is False:
            choice = input("Enter an option: ")
            Menu.Validate_Integer_Input(choice)
        action = self.choices.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))
        return 
    #************************************************
    #//Function Menu
    #
    #************************************************ 
    def Menu(self):
        print(
"""
 _______________________
|         Menu          |
|-----------------------|
|1.                     |
|-----------------------|
|2.                     |
|_______________________|

""" )

    #************************************************
    #//Function Validate_Integer_Input
    #
    #************************************************ 
    def Validate_Integer_Input(int_Input):
        try:
            int_Input = int(int_Input)
            if(int_Input >= 0):
                global strValidated
                strValidated = True
            else:
                print("Input Must Be 0 or More")
        except ValueError:
            int_Input = int(0)
            print("Input Must be Numeric")
        return int_Input

    #************************************************
    #//Function Exit
    #
    #************************************************ 
    def Exit(self):
        sys.exit(0)



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
shopOpens = []
#************************************************
#//CLASS: STARTUP MENU
#
#************************************************    
class StartupMenu(Menu):
    pass
    def __init__(self):
        global shopOpens
        self.shopOpens = shopOpens

        self.choices = {
            "1": self.StartUpQuestions,
            "2": self.Exit
        }


    #************************************************
    #//Function Menu
    #
    #************************************************ 
    def Menu(self):
        print(
"""
 _______________________
|Start Up Menu          |
|-----------------------|
|1. Enter Inventory     |
|-----------------------|
|2. Exit                |
|_______________________|

"""
            
    )

    #************************************************
    #//Function StartUpQuestions
    #
    #************************************************ 
    def StartUpQuestions(self):
        print("\n")
        print("Welcome, Lets set up shop.")
        print("__________________________")
        print("\n")


        global strValidated 
        
        strValidated = bool(False)
        while strValidated is False:
            MB = input("Enter Mountain Bike Inventory: ")
            MB = StartupMenu.Validate_Integer_Input(MB)

        strValidated = bool(False)
        while strValidated is False:
            RB = input("Enter Road Bike Inventory: ")
            RB = StartupMenu.Validate_Integer_Input(RB)

        strValidated = bool(False)
        while strValidated is False:
            TB = input("Enter Touring Bike Inventory: ")
            TB = StartupMenu.Validate_Integer_Input(TB)

        
        Shop = BikeRental(MB,RB,TB)
        Shop.displaystock()

        StartupMenu.DisplayMainMenu(Shop)
        return Shop
    #************************************************
    #//Function DisplayMainMenu
    #
    #************************************************ 
    def DisplayMainMenu(Shop):
        RentalMenu(Shop).Run()








#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

#************************************************
#//Class RentalMenu
#
#************************************************ 
#TODO Should probaly make some of the get information function into customer class functions
#TODO Make a Get Coupon Function
customers = []
class RentalMenu(Menu):
    def __init__(self,Shop):
        global customers
        self.customers = customers
        self.id = len(customers)
        self.Shop = Shop
        self.choices = {
            "1": self.NewCustomerRental,
            "3": self.ShowInventory,
            "2": self.ShowCustomers ,
            "4": self.Exit
            
           
            }      
        self.models = {
            "1": self.MountainBike,
            "2": self.RoadBike,
            "3": self.TouringBike,
            }
        self.DailyBasis = {
            "1": self.RentalHourlyBasis,
            "2": self.RentalDailyBasis,
            "3": self.RentalWeeklyBasis,
            }

    #************************************************
    #//Function Menu
    #
    #************************************************ 
    def Menu(self):
       
        print(
"""
 _______________________
|Rental Menu            |
|-----------------------|
|1. New Customer Rental |
|-----------------------|
|2. Rental Return       |
|-----------------------|
|3. Show Inventory      |
|-----------------------|
|4. End of Day          |
|_______________________|

"""
            
    )

    def BikeModels(self):
        print(""" 
 _______________________
|Bike Models            |
|-----------------------|
|1. Mountain Bike       |
|-----------------------|
|2. Road Bike           |
|-----------------------|
|3. Touring Bike        |
|_______________________|

""")

    def RentalBasis(self):
        print(""" 
 _______________________
|Rental Basis           |
|-----------------------|
|1. Hourly              |
|-----------------------|
|2. Daily               |
|-----------------------|
|3. Weekly              |
|_______________________|

""")

    #/////////////////////////////////////////////////
    def RentalHourlyBasis(self):

        choice = 1
        self.customers[self.id].getRentalBasis(choice)
  
        if choice == 1:
            basis = "Hourly"
        print("\n")
        print(f"You Chose This Rental Basis: {basis}")

    
    def RentalDailyBasis(self):
        choice = 2
        self.customers[self.id].getRentalBasis(choice)
        if choice == 2:
            basis = "Daily"
        print("\n")
        print(f"You Chose This Rental Basis: {basis}")


    def RentalWeeklyBasis(self):
        choice = 3
        self.customers[self.id].getRentalBasis(choice)
        if choice == 3:
            basis = "Weekly"     
        print("\n")
        print(f"You Chose This Rental Basis: {basis}")



    def GetRentalBasis(self):
        print("\n")
        print("Ok now we need your desired Rental Basis")
        print("________________________________________")
        self.RentalBasis()
        global strValidated 
        strValidated = bool(False)
        
        while strValidated is False:
            choice = input("Enter an option: ")
            Menu.Validate_Integer_Input(choice)
        action = self.DailyBasis.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))
            print("Lets Try this Again")
            #Removes last customer added to customers
            customers.pop()
            RentalMenu(self.Shop).Run()

        return 

    #//////////////////////////////////////////
    def MountainBike(self): 
        choice = "MountainBike"
        self.customers[self.id].getBikeModel(choice)
        model = self.customers[self.id].bikeModelRented
        print("\n")

        print(f"You Chose This Model: {model}")
    def RoadBike(self):
        choice = "RoadBike"
        self.customers[self.id].getBikeModel(choice)
        model = self.customers[self.id].bikeModelRented
        print("\n")
        print(f"You Chose This Model: {model}")

    def TouringBike(self):
        choice = "TouringBike"
        self.customers[self.id].getBikeModel(choice)
        model = self.customers[self.id].bikeModelRented
        print("\n")
        print(f"You Chose This Model: {model}")



    def GetBikeModel(self):
        print("\n")
        print("First lets pick out a bike model.")
        print("_________________________________")
        self.BikeModels()
        global strValidated 
        strValidated = bool(False)
        
        while strValidated is False:
            choice = input("Enter an option: ")
            Menu.Validate_Integer_Input(choice)
        action = self.models.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))
            print("Lets Try this Again")
            customers.pop()
            RentalMenu(self.Shop).Run()

        return 

    def GetNumberOfBikes(self):
        #self.id - 1 = Customer index 
        customer = self.customers[self.id - 1]
        blnSwitch = bool(True)  
        while blnSwitch == bool(True): 
            customer.requestBike()
            if customer.bikes > 0:
                blnSwitch = False
           

    def GetRentalTime(self):
        customer = self.customers[self.id - 1]
        blnSwitch = bool(True)
        while blnSwitch == bool(True):
            customer.requestRentalTime()
            if self.customers[self.id - 1].customerRentalTime > 0:
                blnSwitch = False      
            
 

    def ShowCustomers(self):
        print(len(self.customers))

    #/////////////////////////////////////////
    def NewCustomerRental(self):
       
        #Get Name and create new Customer
        print("\n")
        name = input("Please Enter Name For Bike Rental: ")
        
        print("___________________________________")
        customers.append(Customer(name))
        customer = customers[self.id].name
        print(f"Total Customers: {self.id}")
        print("\n")
        print(f"Hey, {customer}. Lets get you set up to rent a bike.")
        print("____________________________________________________")
       
        print("\n")
        # 
        self.GetBikeModel()
        self.GetRentalBasis()
        print("\n")
        self.GetNumberOfBikes()
        print("\n")
        self.GetRentalTime()
        print("\n")
        self.FinalizeRental()
        RentalMenu(self.Shop).Run()
  
    #************************************************
    #//Function ShowInventory
    #
    #************************************************ 
    def ShowInventory(self):
        self.Shop.displaystock()
        input("Press [Enter] To Go Back To The Main Menu")
        RentalMenu(self.Shop).Run()

  

    def FinalizeRental(self):

        customer = self.customers[self.id]
        bikes = customer.bikes        
        model = customer.bikeModelRented
        
        mBikes = self.Shop.MountainBikes
        rBikes = self.Shop.RoadBikes
        tBikes = self.Shop.TouringBikes


        if customer.rentalBasis == 1:
             self.Shop.rentBikeOnHourlyBasis(bikes,model)
             #if a fail happens in the function this will get rid of the customer in list
             if bikes > mBikes or rBikes or tBikes:
                self.customers.pop()
        elif customer.rentalBasis == 2:
             self.Shop.rentBikeOnDailyBasis(bikes,model)
             if bikes > mBikes or rBikes or tBikes:
                self.customers.pop()
        elif customer.rentalBasis == 3:
            self.Shop.rentBikeOnWeeklyBasis(bikes,model)
            if bikes > mBikes or rBikes or tBikes:
                self.customers.pop()

        

