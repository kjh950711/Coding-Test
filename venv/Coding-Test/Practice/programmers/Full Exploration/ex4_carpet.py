# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, red):
    all = brown + red
    for i in range(brown): # 가로
        for j in range(brown): # 세로
            if i < j:
                break
            if i*j == all and (i-2)*(j-2) == red:
                answer = [i, j]
    return answer


brown1 = 10
red1 = 2
brown2 = 8
red2 = 1
brown3 = 24
red3 = 24
print(solution(brown3, red3))