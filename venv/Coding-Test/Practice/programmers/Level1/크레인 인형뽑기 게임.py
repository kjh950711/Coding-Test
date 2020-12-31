## 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket = []
    for move in moves :
        doll = 0
        layer = 0
        while True :
            doll = board[layer][move-1]
            board[layer][move-1] = 0
            layer += 1
            if layer == len(board) or doll != 0 :
                break
        if len(basket) > 0 and doll != 0:
            last = basket.pop()
            if last == doll :
                answer += 2
            else :
                basket.append(last)
                basket.append(doll)
        else :
            basket.append(doll)
    return answer

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
board = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
moves = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(solution(board, moves))