def remove_char(s, c):
    # s = s.replace(c, '')
    # s = s.replace(c.upper(), '')
    # return s
    result = filter(lambda x: x != c.lower() and x != c.upper(), s)
    return "".join(result)


print(remove_char('Amera', 'a'))
