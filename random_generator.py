import random
import string
def make(size):
    all_chars= string.ascii_letters+string.digits
    charsc=len(all_chars)
    serial=[]
    while size>0:
        random_num=random.randint(0,charsc-1)
        random_char=all_chars[random_num]
        serial.append(random_char)
        size-=1
    print(serial)
make(6)    
