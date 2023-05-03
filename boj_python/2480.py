A,B,C = map(int,input().split())
D = 0
if A==B and B==C :
    D=10000 + A*1000
elif A==B:
    D=1000 + A*100
elif B==C:
    D=1000 + B*100
elif A==C:
    D=1000 + C*100    
else:
    if A>B>C: 
        D=A*100
    elif B>A and B>C:
        D=B*100
    else:
        D=C*100
print(D)  


A,B,C = sorted(map(int,input().split()))
D = 0
if A==B and B==C :
    D=10000 + A*1000
elif A==B:
    D=1000 + A*100
elif B==C:
    D=1000 + B*100
else:
    D=C*100
print(D)  