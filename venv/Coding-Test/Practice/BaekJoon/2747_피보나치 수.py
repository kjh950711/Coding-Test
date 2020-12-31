## 2747_피보나치 수

n = int(input())
answer = 0
a1 = 0
a2 = 1
if n == 0 :
    answer = a1
elif n == 1 :
    answer = a2
else :
# a1 = a1 + a2
# a2 = a2 + a1
    for i in range(n-1) :
        if i % 2 == 0 :
            a1 = a1 + a2
            answer = a1
        else :
            a2 = a2 + a1
            answer = a2
print(answer)