
queue = []

def push(x):
    queue.append(x)

def pop() :
    if len(queue) == 0 :
        print(-1)
    else :
        temp = queue[0]
        queue.remove(temp)
        print(temp)
def size() :
    print(len(queue))

def empty() :
    if len(queue) == 0 :
        print(1)
    else :
        print(0)

def front() :
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[0])
def back() :
    if len(queue) == 0:
        print(-1)
    else :
        print(queue[len(queue)-1])

case = input()

for i in range(0, int(case)) :
    test = input().split(" ")
    if test[0] == "push" :
        push(test[1])
    elif test[0] == "pop" :
        pop()
    elif test[0] == "front" :
        front()
    elif test[0] == "back" :
        back()
    elif test[0] == "empty" :
        empty()
    elif test[0] == "size" :
        size()
