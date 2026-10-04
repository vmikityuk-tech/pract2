from turtle import *
from math import *
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
up()
setpos(xc,yc-r)
down()
circle(r)
up()
setpos(x,y)
dot(4,'red')
setpos(0,yc-2*r)
dist = sqrt((x-xc)**2+(y-yc)**2)
color('red')
hideturtle()
if dist==r:
    write('Точка на окружности',align='center')
elif dist<r:
    write('Точка внутри окружности',align='center')
else:
    write('Точка вне окружности',align='center')
done()