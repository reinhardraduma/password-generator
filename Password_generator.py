import random

small_letter = 'abcdefghijklmnopqrstuvwxyz'
capital_letter = small_letter.upper()
num = '123456789'
symbols = '!@#$%^&*()?/><.,+='
all = small_letter + capital_letter + num + symbols
lenght = 9
password = "".join(random.sample(all, lenght))
print(password)

