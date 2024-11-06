import sys
import time

s_Time= time.time()

def TreeCheck(x):
    Tree = True
    q = [x]
    while q:
        key = q.pop(0)
        if preorder[key] == 1: 
            Tree = False 
        preorder[key] = 1
        for j in Dep[key]:
            if preorder[j] == 0:
                q.append(j)
    return Tree

#n=정점, m=간선
TestCase = 0
while True:
    TestCase += 1
    n, m = map(int, sys.stdin.readline().split())
    if [n, m] == [0, 0]: 
        break
    Dep = [[] for _ in range(n + 1)] 
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        Dep[a].append(b)
        Dep[b].append(a)
    treeCnt = 0 
    preorder = [0] * (n + 1)
    for i in range(1, n + 1):
        if preorder[i] == 1: 
            continue
        if TreeCheck(i) is True: 
            treeCnt += 1
    if treeCnt == 0:
        print('Case {}: No trees.'.format(TestCase))
    elif treeCnt == 1:
        print('Case {}: There is one tree.'.format(TestCase))
    else:
        print('Case {}: A forest of {} trees.'.format(TestCase, treeCnt))
e_Time=time.time()
execution_time = e_Time - s_Time
print("실행 시간:", execution_time, "초")
