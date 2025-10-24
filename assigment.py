while True:
    try:
        hours =float(input(" please enter worked hours : "))
        break
    except ValueError:
        print("please enter a numeric value")
while True:
    try: 
        rate = float(input("please enter hourly rate : "))
        break
    except ValueError:
        print("please enter a numeric value")

if hours > 40 :
    pay = (hours*rate)+ (hours -40)*rate*1.5
else:
        pay = hours*rate
print("pay :",pay)



while True:
  
    try:
        score = float(input("please enter your score: "))
        if score >= 0.0 and score <= 1.0:
            break
        else:
            print("Bad score")
    except ValueError:
        print ("Bad Score")


if score >= 0.9 :
                print("A")
elif score >= 0.8:
                print("B")
elif score >= 0.7:
                print("C")
elif score >= 0.6:
                print("D")
else:
                print("F")