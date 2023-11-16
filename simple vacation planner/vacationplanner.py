planeTicket=float(input("\nEnter the cost of the plane ticket :Rs."))   #inputs from user
hotelCost=float(input("\nEnter the cost of the hotel per night:Rs."))
numNights=int(input("\nEnter the number of nights:"))
mealCost=float(input("\nEnter the average cost of a meal:Rs."))
numMeals=int(input("\nEnter the number of meals per day:"))
roundTripCost=(planeTicket*2)                          #calculating for round trip cost
accmdtnCost=(numNights*hotelCost)              #calculating for accomodation cost
foodCost=(numNights*numMeals*mealCost)         #calculating for food cost
print("\n\n\t\t"+"*" *5+ "VACATION PLANNER" + "*"*5 )
print(f"\n\t\t\t Plane Cost for a Round Trip :Rs.{roundTripCost}")
print(f"\n\t\t\t Accomodation Cost for {numNights} days :Rs.{accmdtnCost}")
print(f"\n\t\t\t Food Cost for {numNights} days :Rs.{foodCost}")
print("-"*50)
print(f"\n\n\t\t\tThe total cost of your trip is: Rs.{roundTripCost+accmdtnCost+foodCost}\n")   #calculating total cost for trip
print("-"*50)
