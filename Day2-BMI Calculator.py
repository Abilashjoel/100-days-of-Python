print("Welcome To My BMI Calculator")
weight = float(input("Please Enter Your Weight "))
height = float(input("Please Enter Your Height "))/100
BMI = (weight/(height**2))
print("Your BMI is",BMI)