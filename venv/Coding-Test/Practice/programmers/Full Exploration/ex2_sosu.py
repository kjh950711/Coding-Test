# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    comb_list = []

    # 1자리
    for number in numbers: 
        comb_list.append(int(number))
    # 2자리 이상
    for i in range(2, len(numbers)+1):
        comb = list(permutations(numbers, i))
        for j in comb:
            string = ''
            for k in range(i):
                string += j[k]
                # print(string)
            comb_list.append(int(string))
    comb_list = list(set(comb_list))
    comb_list.sort()
    if comb_list[0] == 0:
        comb_list.remove(0)
    if comb_list[0] == 1:
        comb_list.remove(1)
    # print(comb_list)
    # print(len(comb_list))
    
    # 소수 체크
    for i in range(2, max(comb_list)): # log(n)
    # for i in range(2, int(max(comb_list)**0.5)): # log(n^1/2)
        for j in comb_list:
            if j > i and j%i == 0:
                comb_list.remove(j)
    return len(comb_list)

def solution2(numbers):
    numbers = list(numbers)
    comb_list = []

    # 1자리
    for number in numbers:
        comb_list.append(int(number))
    # 2자리 이상
    for i in range(2, len(numbers) + 1):
        comb = list(permutations(numbers, i))
        for j in comb:
            string = ''
            for k in range(i):
                string += j[k]
                # print(string)
            comb_list.append(int(string))
    comb_list = list(set(comb_list))
    comb_list.sort()
    if comb_list[0] == 0:
        comb_list.remove(0)
    if comb_list[0] == 1:
        comb_list.remove(1)
    # print(comb_list)
    # print(len(comb_list))

    # 소수 체크
    for i in comb_list:
        if i == 2:
            answer += 1
        check = 0 # 안나눠지는 개수
        if i != 0 and i != 1:
            for j in range(2, i):
                if i%j == 0:
                    break
                else:
                    check += 1
        print(i, check)
        if check == i-2:
            answer += 1
    return answer

numbers = '17'
# numbers = '011'
# numbers = '1234'
print(solution(numbers))