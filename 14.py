knat = int(input())
gal = knat//(17*29)
knat -=gal*17*29
sik = knat//29
knat -=sik*29
if gal!=0 and sik!=0 and knat!=0:
    print(str(gal)+' галлеонов',str(sik)+' сиклей',str(knat)+' кнатов',sep = '\n')
elif gal!=0 and sik==0 and knat!=0:
    print(str(gal)+' галлеонов',str(knat)+' кнатов',sep = '\n')
elif gal!=0 and sik!=0 and knat==0:
    print(str(gal)+' галлеонов',str(sik)+' сиклей',sep = '\n')
elif gal==0 and knat!=0 and sik!=0:
    print(str(sik)+' сиклей',str(knat)+' кнатов',sep = '\n')
elif gal==0 and knat==0 and sik!=0:
    print(str(sik)+' сиклей')
elif gal==0 and sik==0 and knat!=0:
    print(str(knat)+' кнатов')
elif gal!=0 and sik==0 and knat==0:
    print(str(gal)+' галлеонов')
