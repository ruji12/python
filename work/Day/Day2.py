
#type casting i.e converting one datatype to another  datatyoe
# num_char=len(input("What is your name?"))
# new_num_char=str(num_char)
# print("your name has" + new_num_char +"characters")

#to check type of data type 
# print(type(num_char))


#exercise 1
# Write a program that adds the digits in a 2 digit number.e.g.if the input was 35,then the output should be 3+5=8


# Solution

# two_digit_number=input("enter any two digit number")

# first_digit=two_digit_number[0]
# second_digit=two_digit_number[1]

# result=int(first_digit) + int(second_digit)

# print(result)


#mathmatical oprations
# 3+5
# 7-3
# 3*2
# 4/2
# **  #work as  exponential i.e. power

#operators priority in python

# PEMDAS
# () paranthesis
# ** power
# *  # /multiplication

# + - substraction addition

#BMI Calculator
# weight=input("enter weight")
# height=input("enter height")
# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = weight_as_int/ height_as_float**2
# bmi_as_int=int(bmi)
# print(bmi_as_int)
 


# print(round(8/3,2)) 2 represents precision 
 
# score =0
# string manipulation
# score +=2
# print(score)


# f-strings displays all type sof data types together without type casting

# score=2
# height=7.5
# iswinning=True

# print(f"Your score is {score},your height is{height},and your winning is {iswinning}")


#Create a program using maths and f-strings that tells us how many days ,weeks,months we have left if we live until 90 years.

# age=input("enter your current age")

# age_int=int(age)

# years_left=90-age_int
# months_left=years_left*12
# weeks_left=years_left*52
# days_left=years_left*365


# print(years_left)
# print(months_left)
# print(weeks_left)
# print(days_left)


# print(f"if I live 90 years the days I live is{days_left},years left is {years_left},week left is{weeks_left}and month left is {months_left}")
 


#tip calculator day2 project
print("Welcome to the tip calculator.")
total_bill =  float(input("\nWhat was the total bill? $"))
tip = int(input("what percentage tip would you like to give ?10,12, or 15?"))
num_people = int(input("How many people to split the bill?"))

total_tip =tip/100 * total_bill + total_bill
bill_each_person =total_tip/num_people
finalamount="{:.2f}".format(bill_each_person) #to round number to two decimal places


print(f"Each person should pay :{finalamount}")