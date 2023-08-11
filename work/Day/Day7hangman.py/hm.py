stages=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    


import random
word_list=["bamboo","shampoo","Pandaa"]
choosen_word= random.choice(word_list)
print(f"the choosen word is:{choosen_word}")


display=[]
for char in range(0,len(choosen_word)):
    display +="_"

print(display)

print(logo)

end_of_game = False
lives=6
while not end_of_game:
    
    guess = int(input("guess a letter").lower())
    print(guess)

    
    for char in range(0,len(choosen_word)):
     if(choosen_word[char]==guess):
        display[char]=guess
    print(display)

    if guess not in choosen_word:
       lives -=1
       if lives==0:
          end_of_game=True
          print("you lose game")

    if "_" not in display:
       end_of_game=True
    print("You win")


print(stages[lives])

    









