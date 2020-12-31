# 1087
num = input()
num = int(num)
final = 0
a = 0
while a < num:
    a += 1
    final += a
    if final >= num:
        print(final)
        break