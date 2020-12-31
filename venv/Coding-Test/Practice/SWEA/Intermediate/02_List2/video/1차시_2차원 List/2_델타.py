## 델타를 이용한 2차 List 탐색

arr = [[0, 1, 2, 3],
       [10, 11, 12, 13]]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [-0, 0, -1, 1]

for x in range(len(arr)) :
    for y in range(len(arr[x])) :
        for i in range(4) :
            testX = x + dx[i]
            testY = y + dy[i]
            print(x, y, testX, testY, arr[testX][testY])

