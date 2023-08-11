# letters_nr=int(input("enter the number of letters you wsnt to include"))
# print(type(letters_nr))
scores=input("Enter the scores of the students!").split()
for n in range(0,len(scores)):
    scores[n]=int (scores[n])

print(scores)