print("program to calculate total expenditure for a trip-hotelcost,planecost,rentedvehiclecost,extraexpenditure")
def hotel_cost(night):
    return night*100
def plane_cost(city):
    if city=="dehli":
        return 1000
    elif city=="mumbai":
        return 600
    elif city=="chenai":
        return 800
      
def rentedvehicle_cost(days):
    if days>=7:
        return days*100-50
    elif days>=3:
        return days*100-10
    else:
        days*100
def trip_cost(city,days,night,extraexpenditure):
    return plane_cost(city)+hotel_cost(night)+rentedvehicle_cost(days)+extraexpenditure
print("total cost of the trip is=",trip_cost("dehli",5,3,100))
    
    

