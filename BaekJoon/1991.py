import sys
count = int(input())
list =[]

class Tree(object) :
    # 생성자
    def __init__(self, root , left , right):
        self.root = root
        self.left = left
        self.right = right

#root의 index찾기
def search_root(root):
        index = -1
        for i in range(0,len(list)) :
              if list[i].root == root :
                    index = i
        return int(index)

#전위순회(루트 , 왼쪽 , 오른쪽)
def preorder(root, left ,right) :
    sys.stdout.write(root)
    if left != '.' :
        find = search_root(left)
        preorder(list[find].root , list[find].left , list[find].right)
    if right != '.':
        find = search_root(right)
        preorder(list[find].root, list[find].left, list[find].right)

#중위순회(왼쪽 , 루트 , 오른쪽)
def inorder(root, left, right) :
    if left != '.':
        find = search_root(left)
        inorder(list[find].root, list[find].left, list[find].right)

    sys.stdout.write(root)
    if right != '.':
        find = search_root(right)
        inorder(list[find].root, list[find].left, list[find].right)

#후위순회(왼쪽 , 오른쪽 , 루트)
def postorder(root, left , right) :
    if left != '.':
        find = search_root(left)
        postorder(list[find].root, list[find].left, list[find].right)
    if right != '.':
        find = search_root(right)
        postorder(list[find].root, list[find].left, list[find].right)

    sys.stdout.write(root)

for i in range(0,count) :
    tree_pair = input().split(" ")
    list.append( Tree(tree_pair[0] , tree_pair[1] , tree_pair[2]) )

if __name__ =="__main__":
    preorder(list[0].root , list[0].left,list[0].right)
    print()
    inorder(list[0].root , list[0].left,list[0].right)
    print()
    postorder(list[0].root , list[0].left,list[0].right)


