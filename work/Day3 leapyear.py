year = int(input("please enter theyear!"))
if year % 4 == 0 & year % 100 != 0:
    print("leap year")
elif year % 100 == 0 & year % 400 == 0:
    print("Divisible by both 100 and 400 so a leap year")

else :
    print("leap year")


