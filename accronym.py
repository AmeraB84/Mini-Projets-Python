s = input('Please enter a string ')
liste = s.split()
a = ''
for x in liste:
    a += x[0].upper()
print(a)
