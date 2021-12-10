def longest_word(s):
    list = s.split()
    for i in range(0, len(list)-1):
        if len(list[i]) > len(list[i+1]):
            m = list[i]
        else:
            m = list[i+1]

    return f'The longest word is : {m}'


print(longest_word('I want to be data analyst'))
