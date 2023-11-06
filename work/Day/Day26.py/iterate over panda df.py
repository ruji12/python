student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]

}
#Looping through dictionaries:
# for (key,value) in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

#loop through rows of a data frame
# for (index,row) in student_data_frame.iterrows():
#     print(row['student'],row['score'])


import csv
csv_file ='nato_phonetic_alphabet.csv'
data=[]

with open(csv_file,mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

print(data)