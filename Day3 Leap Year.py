year = int(input("Enter Year"))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print(" leap Year")
        else:
            print("not leap Year")
            
    else:
        print("leap Year")
else:
    print("not leap year")
    
    
