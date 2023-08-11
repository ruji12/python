# positional arguments
def greet(name,location):
    print(f"hello  {name}")
    print(f"Ilive in {location}")
greet("angela","USA")#position of an arguments cannot be changed  in positional arguments.

#keyword arguments
def num(a,b,c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
num(c=3,b=4,a=7)#position of an arguments can be changed.
    