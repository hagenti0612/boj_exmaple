H,M = map(int,input().split())
R = int(input())

M = M + R
H = (H + M//60) % 24
M = M % 60

print(H,M)  