# https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    stack = []
    answer = []
    n = len(heights)
    for i in range(1, n+1): # 0, 1, 2, ...
        if len(stack) != 0: # i=0일때 만 통과
            for j in range(len(heights)-1, -1, -1):
                if stack[-1] < heights[j]: # 남아있는 heights들과 크기순차비교
                    answer.append(j+1)
                    break
                elif j == 0:
                    answer.append(0)
                    break
            print("answer:", answer)
        stack.append(heights.pop())
        print("stack:", stack)
    answer.append(0)
    answer.reverse()
    return answer

heights = [1,5,3,6,7,6,5]
print("정답: ", solution(heights))
