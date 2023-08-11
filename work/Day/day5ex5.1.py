# fruits =["apple","kiwi","mango"]
# for fruit in fruits:
  # print average height of students


heights=input("give the height of students").split()
for n in range(0,len(heights )):#to convert heights into strings as input alwways takes string value
    heights[n]=int(heights[n])
print(heights)
total_heights= 0
for height in heights:
    total_heights +=height

print(total_heights)


stu_num=0
for students in heights:
    stu_num +=1

print(stu_num)


avg=total_heights/stu_num
print(avg)