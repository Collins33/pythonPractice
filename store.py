prices={"banana": 4,"apple": 2,"orange":1.5,"pear":3}
stock={"banana": 6,"apple": 0,"orange": 32,"pear": 15}
#loop through the dictionaries and print name ,price and stock
for key in prices:

  print key

  print "price: %s" % prices[key]

  print "stock: %s" % stock[key]

#get how much our store is worth by multiplying total stock and total price
total=0
for key in prices:
  amount=prices[key]*stock[key]
  total +=amount
  print total


#grocery list
groceries=['banana','orange','apple']

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total
