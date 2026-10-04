a = int(input())
con1 = 10**3<=a<10**4
con2 = len(set(str(a)))==4
con3 = not(1900<=a<=2050)
if con1 and con2 and con3:
    print('OK')
else:
    print('ERROR')