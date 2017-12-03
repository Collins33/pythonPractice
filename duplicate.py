def removeDuplicate(name):
    #return new string without duplicates
    nameSet=set(name)

    #set into sorted list
    final=sorted(''.join(str(s) for s in nameSet))
    #convert list into string
    finalWord=''.join(final)
    
    #no of duplicates
    difference =(len(name)-len(nameSet))

    return ((finalWord,difference))





removeDuplicate("abccdbahh")
