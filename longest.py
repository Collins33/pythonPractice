def longest(name):
  nameList=name.split()
  nameLengths=[]
  for x in range(len(nameList)):
      nameLengths.append(len(nameList[x]))

  finalIndex=nameLengths.index(max(nameLengths))
  print(nameList[finalIndex])


longest("Thissssssssss")
