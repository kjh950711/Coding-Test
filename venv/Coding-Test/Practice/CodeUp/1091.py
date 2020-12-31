# 1091

a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

for i in range(n-1):
    a = a*r
print(a)