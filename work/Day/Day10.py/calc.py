def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

#storing function inside a dictionary
values={ 
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    }
should_continue=True
def calculator():
    num1=int(input("what's the first number ?:" ))
    for symbols in values:
        print(symbols)
    # should_continue=True
    while  should_continue:
        symbol=input("Pick an operation of your choice:")
        num2=int(input("What's the next number?:"))
        my_operation=values[symbol](num1,num2)
        print(my_operation)
        result=input("Type 'y' to continue calculating with previous value,'n' to continue new calculation")
        if result=='y':
            num1=my_operation
        elif result=='n':
            should_continue= False
            calculator()
            
           
calculator()





