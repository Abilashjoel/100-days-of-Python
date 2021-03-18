  
print("Welcome To My BMI Calculator")
weight = float(input("Please Enter Your Weight "))
height = float(input("Please Enter Your Height "))/100
BMI = (weight/(height**2))
print("Your BMI is",BMI)
if BMI <18.5:
    print("Under Weighted")
elif BMI > 18.5 and BMI <25:
    print ("Normal Weight")
else:
    print("Over Weight")
