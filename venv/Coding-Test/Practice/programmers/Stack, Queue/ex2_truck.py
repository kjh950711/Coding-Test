# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    time = 0
    sum_truck_weights = 0
    while len(truck_weights) != 0:
        time += 1
        truck = bridge.pop()
        sum_truck_weights -= truck
        if (sum_truck_weights + truck_weights[0]) <= weight:
            bridge.insert(0, truck_weights[0])
            sum_truck_weights += truck_weights[0]
            truck_weights.remove(truck_weights[0])
        else:
            bridge.reverse()
            bridge.append(0)
            bridge.reverse()
        # print(time, bridge)
    while len(bridge) != 0:
        time +=1
        bridge.pop()
    return time

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))
