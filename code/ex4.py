# 100 is assigned to cars
cars = 100
# 4.0 is assigned to space_in_a_car
space_in_a_car = 4.0
# 30 is assigned to drivers
drivers = 30
# 90 is assigned to passengers
passengers = 90
# Difference of cars and drivers is assigned to cars_not_driven
cars_not_driven = cars - drivers
# value in dreivers is assigned to cars_driven
cars_driven = drivers
# Product pf cars_driven and space_in_a_car values is assigned to car pool
# car_pool_capacity
car_pool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car is assigned with the division of passengers and
# cars_driven
average_passengers_per_car = passengers / cars_driven

# Print cars to the screen
print "There are", cars, "cars available."
# Print number of drivers to the screen.
print "There are only", drivers, "drivers available."
# Print cars_not_driven to the screen.
print "There will be", cars_not_driven, "empty cars today."
# print car_pool_capacity to the screen.
print "We can transport", car_pool_capacity, "people today."
# Print passengers to the screen.
print "We have", passengers, "to car pool today."
# Pritn average_passengers_per_car to the screen.
print "We need to put about", average_passengers_per_car, "in each car."
