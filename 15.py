n,k,m = map(int,input().split())
if abs(k-m)<n//2:
    print(max(k,m)-min(k,m)-1)
else:
    print(min(k,m)+n-max(k,m)-1)
