a = int(input())
if a%10==1 and a!=11:
    print(str(a)+" попугай")
elif (a%10) in (2,3,4) and a!=12 and a!=13 and a!=14:
    print(str(a)+' попугая')
elif (a%10) in (0,5,6,7,8,9) or (4<a<20):
    print(str(a)+' попугаев')
