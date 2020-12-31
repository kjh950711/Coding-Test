## 비트연산을 이용해 간결하게 부분 집합을 생성

arr = [3, 6, 7, 1, 5, 4]
n = len(arr) # 원소의 개수

for i in range(1 << n) : # 1 << n : 부분 집합의 개수
    for j in range(n) : # 원소의 수 만큼 비트를 비교
        if i & (1<<j) : # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=',')
    print() # 부분집합 완성