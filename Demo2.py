'''Program 1: Rewrite the program from project 1 for pay computation to give the employee 1.5 times the 
hourly rate for hours worked above 40 hours. 
Enter Hours: 45 
Enter Rate: 10 
Pay: 475.0

'''
import numpy as np

hours = int(input("enter hours : "))
rate = int(input(" Enter rate"))

if hours== 40 or 40 > hours :
    Pay = hours* rate
    print(Pay)
else:
    Pay = hours*rate*1.5
    print(Pay)