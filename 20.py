b = input()
cl = b[0]
n = b[1]
if (cl in 'aceg' and n in '1357') or (cl in 'bdfh' and n in '2468'):
    print('черный')
else:
    print("белый")