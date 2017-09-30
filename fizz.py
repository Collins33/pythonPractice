numbers=list(range(0,101))
for list in numbers:
    if list%15 == 0:
        list = "fizzBuzz"
    elif list%5 == 0:
        list= "Buzz"
    elif list%3 ==0:
        list="fizz"

    print(list)
