class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def make_binary_tree(val_list):
    node_list = []

    # 노드 주소 할당
    for one in val_list:
        node_list.append(Node(one))

    for i in range(len(val_list)-3):
        node_list[i].left = node_list[2 * i + 1]
        try:
            node_list[i].right = node_list[2 * i + 2]
        except:
            pass

    # 루트 리턴
    return node_list[0]


# 넓이 우선 탐색 BFS
def print1(root):
    visited = []
    que = [root]
    while que:
        nod = que.pop(0)
        if nod.val not in visited:
            print(nod.val)  # 바로바로 출력

            visited.append(nod)
            if nod.left != None:
                que.append(nod.left)
            if nod.right != None:
                que.append(nod.right)
    # return list(map(lambda x: x.val, visited)) #한번에 출력 가능
    return


# 깊이 우선 탐색 DFS
def print2(root):
    visited = []
    stack = [root]
    while stack:
        nod = stack.pop()
        if nod.val not in visited:
            print(nod.val)  # 바로바로 출력

            visited.append(nod)
            # pop으로 스택에서 빼기 때문에
            # 오른쪽 노드를 먼저 넣어야 왼쪽부터 뺀다.
            if nod.right != None:
                stack.append(nod.right)
            if nod.left != None:
                stack.append(nod.left)
    # return list(map(lambda x: x.val, visited)) #한번에 출력 가능
    return


val_list = [10, 12, 15, 25, 30, 36]
root = make_binary_tree(val_list)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)