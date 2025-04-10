import sys

# 전위 순회 (중-왼-오) : DFS
def preorder(root):
    
    if root != ".":
        print(root, end = "")
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회 (왼-중-오)
def inorder(root):
    
    if root != ".":
        inorder(tree[root][0])
        print(root, end ="")
        inorder(tree[root][1])
        
# 후위 순회 (왼-오-중)
def postorder(root):
    
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end ="")

input = sys.stdin.readline

N = int(input())
tree = {}

for i in range(N):
    
    vertex,left,right = input().rstrip().split(" ")
    tree[vertex] = [left,right]

preorder("A")
print()

inorder("A")
print()

postorder("A")
print()