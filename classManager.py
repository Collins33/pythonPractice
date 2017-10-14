lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
#add the three dictionaries to a list
students=[lloyd,alice,tyler]
#loop through the list to access the dictionaries
#loop through the dictionaries to print the values using the keys
print ("the class manager")
for student in students:
  for key in student:
    print (key)
    print (student[key])
#this method takes a list of numbers and finds the average
def average(numbers):
  total=sum(numbers)
  total=float(total)
  total=total/len(numbers)
  return total
