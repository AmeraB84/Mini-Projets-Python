def remove_duplicate_word(s):
    # l = s.split(" ")
    # ls = [l[0]]
    # for word in l:
    #     if word not in ls:
    #         ls.append(word)
    # print(ls)
    # return ' '.join(ls)
    # u = list(dict.fromkeys())
    return ' '.join(list(dict.fromkeys(s.split(" "))))


print(remove_duplicate_word(
    'hello amera amera amera data wants to be data analyst and data scientist'))
