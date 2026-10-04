a = int(input())
a-=1
if a<=9:
    print(a)
elif 10<=a<=189:
    z = (10+a)//2
    if a%2==0:
        print(z//10)
    else:
        print(z%10)
elif 190<=a:
    z = (110+a)//3
    if (a-1)%3==0:
        print(z//100)
    elif a%3==0:
        print(z%10)
    else:
        print((z//10)%10)
