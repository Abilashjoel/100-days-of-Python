print("welcome to the PIZZA Shop")
size = input("Enter your Size of Pizza? S,M,L")
bill = 5
if size=="S":
    pep = input("do you want pepperoni ? Y or N")
    if pep=="Y":
        bill=bill+2
    exche =input("do you want Extra Cheese ? Y or N")
    if exche =="Y":
        bill=bill+1
if size=="M":
    bill=bill+5
    pep = input("do you want pepperoni ? Y or N")
    if pep=="Y":
        bill=bill+2
    exche =input("do you want Extra Cheese ? Y or N")
    if exche =="Y":
        bill=bill+1
if size=="L":
    bill=bill+10
    pep = input("do you want pepperoni ? Y or N")
    if pep=="Y":
        bill=bill+2
    exche =input("do you want Extra Cheese ? Y or N")
    if exche =="Y":
        bill=bill+1

print(f"Your bill is $ {bill}")
            
            
