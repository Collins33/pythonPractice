def getAge():
    print("Enter your age")
    try:
      age=int(input())
      return age
    except ValueError:
        return "That input was invalid"

    print(age)

getAge()
