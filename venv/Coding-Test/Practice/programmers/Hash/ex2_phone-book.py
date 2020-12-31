# https://programmers.co.kr/learn/courses/30/lessons/42577

# 방법1
def solution(phone_book):
    phone_book.sort()
    answer = True
    for a, b in zip(phone_book, phone_book[1:]):
        print(a, b)
        if b.startswith(a):
            answer = False
    return answer

# 방법2
def solution2(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j:
                if phone_book[i] in phone_book[j]:
                    answer = False
    return answer

# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))
print(solution2(phone_book))