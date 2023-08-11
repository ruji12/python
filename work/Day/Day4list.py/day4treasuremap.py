#write a program in which you should allow you to enter the position of the treasure using a two-digit sysytem.The first digit is the horizontal column number and the second digit is the vertical row number.


row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]

map =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position=input("where do you want to put treasure?")


horizontal=int(position[0])
vertical=int(position[1])

selected_row=map[vertical-1]
selected_row[horizontal-1]='X'


print(f"{row1}\n{row2}\n{row3}")