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

#this method finds the average of the work and multiples the average by the weight
#it takes a dictionary as an argument
def get_average(student):
  homework=average(student["homework"])*0.1
  quizzes=average(student["quizzes"])*0.3
  tests=average(student["tests"])*0.6

  return homework+quizzes+tests
#this method finds the total grade based on the average score of the student
def get_letter_grade(score):
  if score >=90:
    return 'A'
  elif score >=80:
    return 'B'
  elif score >=70:
    return 'C'
  elif score >=60:
    return 'D'
  else:
    return 'F'
for student in students:
    print (get_letter_grade(get_average(student)))
#get the average of each student
#then find average of that average
def get_class_average(class_list):
  results=[]
  for student in class_list:
    finalresult=get_average(student)
    results.append(finalresult)
  return average(results)
print ("class average")
print (get_class_average(students))
#get class grade
print ("class grade")
print (get_letter_grade(get_class_average(students)))
