# You are going to write a program that automatically prints the solution to the FizzBuzz game.


#Your program should print each number from  1 to 100 in turn .
# when the number is divisible by 3 then instead of printing the number it should print "Fizz"
# # 


#  when the number is divisible by 3 then instead of printing the number it should print "Buzz"


# and if the number is divisible by both 3 and 5 then it should print "Fizz Buzz"


for n in range(1,101):

    if n%3 ==0 & n%5 ==0:
        print("fizzbuzz")

    elif n%3 ==0:
        print("Fizz")
    elif n%5 ==0:
        print("Buzz")

    
    else:
        print(n)

    







