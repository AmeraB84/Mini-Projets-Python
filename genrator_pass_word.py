import string
import random

x = int(input('Please enter the length of the pass word :'))
letre = string.ascii_letters + string.digits + string.punctuation
letters = random.choices(letre, k=x)
pass_word = ''.join(letters)
# for i in letters8:
#     pass_word += i
print(pass_word)
