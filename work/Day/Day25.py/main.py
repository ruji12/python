# with open("/Users/user/Desktop/weatherdata.csv") as data:
#     my_data = data.readlines()
#     print(my_data)

# import csv

# with open("/Users/user/Desktop/weatherdata.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature=[]
#     for row in data:
#        if row[1]!="temp":
#            temperature.append(int(row[1]))

#     print(temperature)


# import pandas           
# data=pandas.read_csv("/Users/user/Desktop/weatherdata.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)


# def calculated_average(num):
# max_num = max(num)
# my_sum = sum(num)
# average = my_sum/len(num)
  


# num=data["temp"].to_list()
# max_num = max(num)
# # my_sum = sum(num)
# # average = my_sum/len(num)
# print(data[data.temp==max_num])
  

# # print("average temperature:",average)
# print("The maximum temperature is:",max_num)

# # also

# print(data["temp"].max()) to find max number .
# print(data["temp"].mean()) to find mean.

# get data in the rows

import pandas
data = pandas.read_csv("/Users/user/Desktop/squirrelcensus.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"]=="Black"])

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict={

    "Fur Color":["Gray","Cinnamon","Black"],
    "Count" :[gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
    

    }
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel.csv")






        