import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}#dictionary comprehensions



word =input("Enter a word").upper()
output_list=[phonetic_dict[letter] for letter in word]#used list comprehensions
print(output_list)