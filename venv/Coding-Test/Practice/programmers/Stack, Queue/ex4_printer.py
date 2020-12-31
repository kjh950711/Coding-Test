# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    array = [] # index 확인용
    for i in range(len(priorities)):
        array.append(i)
        i += 1
    array2 = []
    list = [] # 인쇄순서 담기
    while len(priorities) > 0:
        if priorities[0] == max(priorities):
            list.append(priorities[0])
            priorities.remove(priorities[0])
            array2.append(array[0])
            array.remove(array[0])
        else:
            priorities.append(priorities[0])
            priorities.remove(priorities[0])
            array.append(array[0])
            array.remove(array[0])
    # print(array2)
    # print(list)
    find =  array2.index(location)
    # print(find)
    answer = find+1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))