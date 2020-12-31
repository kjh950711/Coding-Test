# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for one in range(len(citations), 1, -1):
        check = 0
        for i in range(len(citations)):
            if citations[i] >= one:
                check += 1
            if check >= one:
                return one
    return 0

# citations = [3, 0, 6, 1, 5]
# citations = [0, 0, 0, 0]
citations = [20, 19, 18, 1]
print(solution(citations))