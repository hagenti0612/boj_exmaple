H,M = map(int,input().split())
M = M-45
if M < 0 :
    M=M+60
    H=H-1
if H<0 :
    H=H+24
print(H,M)  

H=(H+(M//45-1)) %24

M=(M-45) %60

print(H,M)  