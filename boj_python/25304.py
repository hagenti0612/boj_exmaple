X = int(input())
N = int(input())
for i in range (0,N):
    a,b = map(int,input().split())
    X -= (a*b)
if X==0:
    print('Yes')
else:
    print('No')