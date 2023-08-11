names=["angel","ben","jenny","koal","jack"]
names_len=len(names)

import random
random_name =random.randint(0,names_len-1)
person_who_will_pay=names[random_name]

print("today bill will be paid by  " +person_who_will_pay )