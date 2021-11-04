import random

num = random.randint(0, 10)
print(f'number is {num}')
print('#'*40)
print(' the number is between 0 and 10 '.center(40, '#'))
print('#'*40)
user_num = int(input('please enter a number choose by pc :'))
for i in range(2):
    if user_num > num:
        print('your propostion is bigger than our number')
        user_num = int(input('please enter a number choose by pc :'))

    elif user_num < num:
        print('Your proposision in smaller than our number')
        user_num = int(input('please enter a number choose by pc :'))

    else:
        print('Congratulations we have a winner')
        break
if user_num != num:
    print('Sorry game over')
