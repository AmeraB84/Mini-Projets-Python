import random
print('game rule: type 1 to roll the dice or 0 to quit the game')
while True:
    x = int(input('Please clic on any boutum and valid with enter '))
    if x == 1:
        print(random.randint(1, 6))
    elif x == 0:
        print('thank you , see you soon')
        break
    else:
        print('bad input , please choose 1 or 0 to quit')
