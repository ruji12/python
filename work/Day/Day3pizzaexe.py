print("Welcome to python Pizza Deliveries!")
size = input("\n What size of pizza do you want? S ,M ,L?")
add_pepperoni = input("Do you want to add pepperoni or not? Y,N")
extra_cheese = input("Do you want to add extra cheese?Y,N?")
total_price=0


if size == "S":
    total_price +=15
    
    
    
        
elif size == "M":
    total_price  +=20
    


else :
    total_price +=25

if add_pepperoni == "Y":
    if size == "S":
        total_price +=2
    else:
         total_price +=3

if extra_cheese == "Y":
    total_price+=1






    
print(f"the total bill is {total_price}")


    
 




