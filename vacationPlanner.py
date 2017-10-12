def hotel_cost(night):
  return night*140
hotel_cost(12)

def plane_ride_cost(city):
  if city == 'Charlotte':
    return 183
  elif city == 'Tampa':
    return 220
  elif city =='Pittsburgh':
    return 222
  elif city == 'Los Angeles':
    return 475

plane_ride_cost('Tampa')

def rental_car_cost(days):
  cost=days*40
  if days >= 7:
    cost-=50
  elif days >= 3:
    cost-=20
  return cost
rental_car_cost(10)


def trip_cost(city,days):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)  
