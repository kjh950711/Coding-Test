## 5208. 전기버스2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    station, *charge_list = map(int, input().split()) # *M ???

    # 초기값
    move = 0
    charge_amount = charge_list[move]
    count = 0

    while move + charge_amount < station-1:
        max_charge = 0
        next_move = None
        for i in range(charge_list, 0, -1): # 갈 수 있는 충전소
            charge = charge_list[move+i] - (charge_amount-i) # 충전 가능한 양

    print('#' + str(test_case), answer)