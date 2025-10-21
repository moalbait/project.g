
# create four variables 
#two strings
# two integers

#strings values
FirstName = input("please enter your name ") # first name
LastName = input("please enter your last name ") #last name

#integer values
YearOfBirth = int(input("what year were you born?  "))
CurrentYear = int(input("what year is this year? "))

FullName = FirstName + Lastname
#print concatenation of string
print(FullName)

# sum and multiply
print("the sum of ",YearOfBirth, "and", CurrentYear, "is" , YearOfBirth + CurrentYear)
print("the multiplied value of ",YearOfBirth, "and", CurrentYear, "is", YearOfBirth* CurrentYear)

# single print length of strings
print("lenth of",FirstName, "is", len(FirstName),"and", LastName , "is", len(LastName))

#print data type
print("data type of ",FirstName, "is",type(FirstName) ,
        "and", LastName , "is", type(LastName),
        "and",YearOfBirth,"is", type(YearOfBirth), 
        "and", CurrentYear, "is",type(YearOfBirth) )

# boolean to check the values
print (True if (YearOfBirth > CurrentYear) else  False )


Student = {
    "fname": "mohammed",
    "lname": "albaiti"
}