## 5254_부분 문자열
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# https://daep93.github.io/2020/04/10/SW-5254/ 참조

T = int(input())
for test_case in range(1, T + 1):
    number, text = input().split()
    number = int(number)

    unordered_suffixes=[(i, text[i:]) for i in range(len(text))]
    ordered_suffixes=sorted(unordered_suffixes, key = lambda elements: elements[1])
    print(ordered_suffixes)

    # print('#' + str(test_case), answer[0], len(answer))