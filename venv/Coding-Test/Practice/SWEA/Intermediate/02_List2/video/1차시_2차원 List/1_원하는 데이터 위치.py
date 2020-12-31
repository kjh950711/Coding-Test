## 2차원 List에서 원하는 데이터의 위치 찾기

n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
newlist = [(i, j) for i in range(n) for j in range(m) if mylist[i][j] == 1]
print(mylist)
print(newlist)
