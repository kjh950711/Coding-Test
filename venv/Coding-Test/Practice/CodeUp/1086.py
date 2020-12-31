# 1086
w, h, b = input().split()
w = int(w) # 정수
h = int(h) # 정수
b = int(b) # 40이하의 4의 배수

result = (w * h * b)/(8 * 1024**2)
print('%.2f' % result, "MB")