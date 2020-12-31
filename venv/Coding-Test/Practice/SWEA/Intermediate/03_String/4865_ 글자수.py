## 4865_ 글자수
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for test_case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    answer_list = []
    for find_word in str1 :
        same_num = 0
        for compare_word in str2 :
            if find_word == compare_word :
                same_num += 1
        answer_list.append(same_num)

    print('#' + str(test_case), max(answer_list))