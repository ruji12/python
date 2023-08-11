#LOVE CALCULATOR

print("Welcome to Love calculator")
name1=input("enter your name!")
name2=input("enter your name!")
lower_name = name1 + name2
name = lower_name.lower()
t=name.count("t")
r= name.count("r")
u= name.count("u")
e=name.count("e")

true = t +r + u+ e

l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")


love = l+o+v+e
love_s=str(true) + str(love)
love_score = int(love_s)


if (love_score <10)  and  (love_score >90):
    print(f"you got score{ love_score},you are  alright together! ")

elif (love_score >40)  and  (love_score <50):
    print(f"you got score {love_score},you are  good together! ")

else:
    print(f"you got score is{love_score}")







