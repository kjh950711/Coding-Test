## 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # 여벌 보유 학생 도난당한 경우 제외
    for lost_one in lost.copy() :
        if lost_one in reserve :
            reserve.remove(lost_one)
            lost.remove(lost_one)

    answer = n - len(lost)
    for borrow in lost :
        if borrow-1 in reserve :
            answer += 1
            reserve.remove(borrow-1)
        elif borrow+1 in reserve :
            answer += 1
            reserve.remove(borrow+1)
        if len(reserve) == 0 :
            break
    return answer