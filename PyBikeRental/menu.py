import sys
from bikerental import BikeRental
from customer import Customer

    #************************************************
    #//Validate_Integer_Input
    #
    #************************************************ 
class Menu(object):

    def __init__(self):
        pass

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

""" )

    #************************************************
    #//Validate_Integer_Input
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
    #//Exit
    #
    #************************************************ 
    def Exit(self):
        sys.exit(0)




    #************************************************
    #//CLASS: STARTUP MENU
    #
    #************************************************    
class StartupMenu(Menu):
    pass
    def __init__(self):
        
        self.choices = {
            "1": self.StartUpQuestions,
            "2": self.Exit
        }

    #************************************************
    #//StartUpQuestions
    #
    #************************************************ 
    def StartUpQuestions(self):
        print("\n")
        print("Welcome, Lets set up shop.")
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

    def DisplayMainMenu(Shop):
        MainMenu(Shop).Run()

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
    #//CLASS: MAIN MENU
    #
    #************************************************  

class MainMenu(Menu):

    def __init__(self,Shop):

        self.Shop = Shop
        self.choices = {
             "1": self.DisplayCustomerMenu,
             "2": self.DisplayEmployeeMenu
            }
    

    #************************************************
    #//DisplayCustomerMenu
    #
    #************************************************ 
    def DisplayCustomerMenu(self):
        RentalMenu(self.Shop).Run()
        

    def DisplayEmployeeMenu(self):
       EmployeeMenu(self.Shop).Run()

    #************************************************
    #//Display Main Menu
    #
    #************************************************ 
    def Menu(self):
        print(
"""
 _______________________
|Main Menu              |
|-----------------------|
|1. Customer            |
|-----------------------|
|2. Employee            |
|_______________________|

"""
            
    )

    #************************************************
    #//Display Main Menu
    #
    #************************************************ 
class RentalMenu(Menu):
    def __init__(self,Shop):
        self.Shop = Shop
        self.choices = {
            "1": self.ShowInventory,
            "2": self.SayHi,
           
            }      
    #************************************************
    #//ShowInventory
    #
    #************************************************ 
    def ShowInventory(self):
        self.Shop.displaystock()
    def SayHi(self):
        print("Hello")

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

class EmployeeMenu(Menu):



    def __init__(self,Shop) -> None:
        
        self.Shop = Shop
        self.choices = {
            "3": self.ShowInventory,
            
           
        }


    #************************************************
    #//ShowInventory
    #
    #************************************************ 
    def ShowInventory(self):
        self.Shop.displaystock()
        
        MainMenu(self.Shop).Run()

    #************************************************
    #//Menu
    #
    #************************************************ 
    def Menu(self):
       
        print(
"""
 ____________________________
|Employee Menu               |
|----------------------------|
|1. Issue Bill               |
|----------------------------|
|2. Verify Stock             |
|----------------------------|
|3. Show Inventory           |
|----------------------------|
|4. Show Daily Bikes Rented  | 
|----------------------------|
|5. Show Daily Revenue       |
|----------------------------|
|4. End of Day               |
|____________________________|

"""
            
    )