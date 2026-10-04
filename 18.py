a,b = map(int,input().split('x'))
c,d,e = map(int,input().split('x'))
if (c<=a and d<=b) or (c<=b and d<=a):
    print('да')
elif (c<=a and e<=b) or (c<=b and e<=a):
    print('да')
elif (d<=a and e<=b) or (e<=a and d<=b):
    print('да')
else:
    print('нет')