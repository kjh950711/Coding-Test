# Node 클래스 선언
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List 클래스
class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    ## 추가
    def append(self, *args): # args : [node : 필수, idx : 선택(idx 지정 안 할 경우 리스트의 끝에 추가 됨)]
        cur_node = self.head # 현재 노드
        prev_node = None # 이전 노드
        cur_idx = 0 # 현재 인덱스

        # 빈 리스트일 경우
        if cur_node == None:
            self.head = args[0]
            
        # idx 지정 안 한 경우
        elif len(args) == 1:
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = args[0]
        
        # 원하는 idx에 넣기
        else:
            if args[1] == 0:
                next_node = self.head
                self.head = args[0]
                self.head.next = next_node
            else:
                while cur_idx < args[1]:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    cur_idx += 1
                args[0].next = cur_node
                prev_node.next = args[0]
        return -1

    ## 출력
    def print(self):
        cur_node = self.head
        string = ""
        while cur_node != None:
            string += str(cur_node.data)
            if cur_node.next != None:
                string += "->"
            cur_node = cur_node.next
        print(string)

if __name__ == "__main__":
    sl = SingleLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(23), 1)
    sl.print()


