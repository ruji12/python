import string
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alphabet)
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

direction=input("Type 'encode' to encrypt ,type 'decode' to decrypt")

text=input("Type your message\n").lower()
shift=int(input("Type the shift number:\n"))
def caeser(my_text,shift_amount):
     
      if direction=='encode':
          cipher_text=""
          for letter in my_text:
             if letter in alphabet:
                 
              
                index_num=alphabet.index(letter)
                new_position=index_num + shift_amount
                new_letter=alphabet[new_position]
                cipher_text+=new_letter
             else:
                 cipher_text+=letter
          
          print(f" the encoded text is {cipher_text}")
      elif direction=='decode':
          decrypted_text=""
          for letter in my_text:
             if letter in alphabet:
                 
              
               index_num=alphabet.index(letter)
               new_position=index_num - shift_amount
               new_letter=alphabet[new_position]
               decrypted_text+=new_letter
             else:
                 decrypted_text+=letter

          print(f" the decoded text is {decrypted_text}")

shift=shift%26

caeser(text,shift)

result=input("do you want to continue type 'yes' to continue 'no' to exit\n")
if result=='yes':
    direction=input("Type 'encode' to encrypt ,type 'decode' to decrypt")
    text=input("Type your message\n").lower()
    shift=int(input("Type the shift number:\n")) 
    
else:
    print("goood bye!")






# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         index_num=alphabet.index(letter)
#         new_position=index_num + shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter

#     print(f" the encoded text is {cipher_text}")
# def decrypt(cipher_text,shift_amount):
#     decrypted_text=""
#     for letter in cipher_text:
#         index_num=alphabet.index(letter)
#         new_position=index_num - shift_amount
#         new_letter=alphabet[new_position]
#         decrypted_text+=new_letter

#     print(f" the encoded text is {decrypted_text}")


# if direction=='encode':
#     encrypt(text,shift)
# elif direction=='decode':
#     decrypt(text,shift)
