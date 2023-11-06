#list comprehensions

# num=[1,2,3]
# #creating a new list from the above list num without list comprehensions.
# new_list=[]
# for n in num:
#     new_list.append(n+1)

# print(new_list)

# #creating a new list from the above list num with list comprehensions.

# num=[1,2,3]
# # new_list=[new_item for item in list] syntax for list comprehensions

# new_list = [n+1 for n in num]
# print(new_list)


range(1,5)
new_range=[n*2 for n in range(1,5)]

print(new_range)


names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

new_names=[name.upper() for name in names if len(name)>5]
print(new_names)