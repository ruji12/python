


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
    "add": add,
    " subtract":subtract,
    "multiply":multiply,
    "divide":divide,
    }
def clear_screen():
    print("\033[H\033[J", end="")

calculation_finished=False
while not calculation_finished:
    operation=input("enter the operation that you want to perform?(add,subtract,multiply,divide)")
    if operation in values:
        num1=float(input("enter number one:"))
        num2=float(input("enter second number:"))
        final_value=values[operation](num1,num2)#calling functions from dictionary.
        print(f"the result is {final_value}")

    else:
        print("invalid input")

    check=input("Type 'y'to continue with the previous calculation or type 'n' to calculate new calculations:")
    if check=='y':
        calculation_finished=True
        print("calculation ends here!!")
    elif check=='n':
        clear_screen()
        


