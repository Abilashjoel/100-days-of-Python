print("Wwelcome To Tip Calculator $")
bill= float(input("Whats Was Your total Bill? $"))
percent = float(input("What Percentage tip would you like to give ? 10, 12, or 15 ?"))
people = float (input("How many people to split the bill? "))
tip = (((bill*12)/100)+bill)/people
print(tip)
