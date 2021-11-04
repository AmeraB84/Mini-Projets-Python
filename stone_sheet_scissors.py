import random

print("*"*80)
print('Welocme do want play with me stone sheet scissors'.center(80, '*'))
print("*"*80)
score_cpu = 0
score_user = 0

while True:
    ch_cump = ''.join(random.sample(['stone', 'sheet', 'scissors'], k=1))
    # print(ch_cump)
    ch_user = str(
        input('Please choose one items : stone , sheet , scissors : '))
    if ch_cump == 'stone':
        if ch_user == 'sheet':
            print('Oh you won st/sh, good job ')
            score_user += 1
        elif ch_user == 'scissors':
            print('st/sci You lose')
            score_cpu += 1
        else:
            print('We are equal')
#####################################################
    elif ch_cump == 'sheet':
        if ch_user == 'stone':
            print(' sh/st You lose')
            score_cpu += 1
        elif ch_user == 'scissors':
            print('sh/sci Oh you won , good job ')
            score_user += 1
        else:
            print('We are equal')
#####################################################
    elif ch_cump == 'scissors':
        if ch_user == 'stone':
            print('sci/st Oh you won , good job ')
            score_user += 1
        elif ch_user == 'sheet':
            print(' sci/st You lose')
            score_cpu += 1
        else:
            print('We are equal')

    if ch_user == 'quit' or ch_user == 'Quit':
        break

print(
    f'///////it was so fun thank you ///////// \n The score is : \n You = {score_user}\n Me = {score_cpu}')
