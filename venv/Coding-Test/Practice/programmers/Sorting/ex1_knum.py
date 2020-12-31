# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for ijk in commands:
        print(array)
        i = ijk[0]
        j = ijk[1]
        k = ijk[2]
        new_array = sorted(array[i-1:j])
        print(new_array)
        answer.append(new_array[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))