# 1088
num = input()
num = int(num)
result = ""
for i in range(1, num+1):
    if i%3 != 0:
        i = str(i) + " "
        result += i
print(result)