def separate_number(n):
    # Convert to string
    s = str(n)
    if len(s) == 3:
        return int(s)
    elif len(s) > 3 and len(s) < 7:
        return '_'.join([s[i:i+3] for i in range(0, len(s) - 2, 3)])
    else:
        return ','.join([s[i:i+3] for i in range(0, len(s) - 2, 3)])+'_'+s[-3:]


print(separate_number(12489789856))
