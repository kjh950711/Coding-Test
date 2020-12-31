## 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):

    # 1, 3, 5, 7, 8, 10, 12 - 31일
    # 2 - 29일
    # 4, 6, 9, 11

    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]

    day = b
    for mon in range(1, a) :
        if mon in d31 :
            day += 31
        elif mon in d30 :
            day += 30
        else :
            day += 29
    answer = day % 7
    dict = {1:'FRI', 2: 'SAT', 3: 'SUN', 4: 'MON', 5:'TUE', 6:'WED', 0: 'THU'}
    answer = dict[answer]

    return answer