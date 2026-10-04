p1,p2 = map(str,input().split('-'))
x1 = int(ord(p1[0])-ord('a')+1)
y1 = int(p1[1])
x2 = int(ord(p2[0])-ord('a')+1)
y2 = int(p2[1])
rx = abs(x2-x1)
ry = abs(y2-y1)
if (rx==1 and ry==2) or(rx==2 and ry==1):
    print('верно')
else:
    print("ошибка")