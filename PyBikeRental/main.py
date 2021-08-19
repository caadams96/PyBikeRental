from bikerental import BikeRental
from customer import Customer 

shop1 = BikeRental(30)
shop2 = BikeRental(30)

shop1.displaystock()

shop1.rentBikeOnHourlyBasis(31)

shop2.rentBikeOnDailyBasis(-1)

shop2.rentBikeOnWeeklyBasis(11)



# Create Customers

customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer4 = Customer()

# Set up rental basis
customer1.rentalBasis = 1 # hourly
customer2.rentalBasis = 1 # hourly
customer3.rentalBasis = 2 # daily
customer4.rentalBasis = 2 # daily

# determine number of bikes
customer1.bikes = 1
customer2.bikes = 5 # eligible for family discount 30%
customer3.bikes = 2
customer4.bikes = 0

# detrmine rental time
customer1.rentalTime = datetime.now() + timedelta(hours=-4)
customer2.rentalTime = datetime.now() + timedelta(hours=-23)
customer3.rentalTime = datetime.now() + timedelta(days=-4)
customer4.rentalTime = datetime.now() + timedelta(days=-14)

# create request to return the bike
request1 = customer1.returnBike()
request2 = customer2.returnBike()
request3 = customer3.returnBike()
request4 = customer4.returnBike()

# return the bike to shop and get a bill
shop1.returnBike(request1) 
shop1.returnBike(request2) 
shop1.returnBike(request3) 
shop1.returnBike(request4) 