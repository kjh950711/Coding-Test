## ex1_target number.py
# https://programmers.co.kr/learn/courses/30/lessons/43165

def DFS(numbers, target, idx, value) :
    if idx == len(numbers) and value == target :
        return 1
    elif idx == len(numbers) :
        return 0
    else :
        answer = 0
        answer += DFS(numbers, target, idx + 1, value + numbers[idx])
        answer += DFS(numbers, target, idx + 1, value - numbers[idx])
        return answer

def solution(numbers, target):
    answer = 0
    idx = 0
    value = 0
    answer += DFS(numbers, target, idx, value)
    return answer

numbers = [1, 4, 2, 5, 3]
target = 1
print(solution(numbers, target))