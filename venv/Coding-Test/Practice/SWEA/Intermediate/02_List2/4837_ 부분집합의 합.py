## 4837_ 부분집합의 합
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 원하는 개수의 부분집합 구하기 실패
def select_num (N, possible_case):
    set_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while N != 0 :
        for num in set_A :
            possible_case.append(num)
            set_A.remove(num)
            N -= 1
    return possible_case

T = int(input())
for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    possible_case = []
    possible_case = select_num(N, possible_case)
    answer = 0
    if sum(possible_case) == k :
        answer += 1

    print('#' + str(test_case), )