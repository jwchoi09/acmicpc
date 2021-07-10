"""

"""
import sys
from collections import deque

def push_front(x, deq):
    tmp = [x]
    tmp.extend(deq)
    deq = tmp
    return deq

def push_back(x, deq):
    deq.append(x)
    return deq

def pop_front(deq):
    if deq : 
        print(deq.pop(0))
    else : 
        print(-1)
    
def pop_back(deq):
    if deq :
        print(deq.pop())
    else :
        print(-1)

def size(deq):
    print(len(deq))

def empty(deq) :
    if not deq : 
        print(1)
    else : 
        print(0)
    
def front(deq) :
    if deq :
        print(deq[0])
    else :
        print(-1)
    
def back(deq) :
    if deq :
        print(deq[-1])
    else :
        print(-1)

def main():
    statements_dict = {
        'push_front' : push_front,
        'push_back' : push_back,
        'pop_front' : pop_front,
        'pop_back' : pop_back,
        'size' : size,
        'empty' : empty, 
        'front' : front,
        'back' : back
    }

    N = int(sys.stdin.readline().strip())
    deq = []

    for _ in range(N) :
        statement = list(sys.stdin.readline().split())
        
        if len(statement) == 1 : 
            command = statement[0]
            statements_dict[command](deq)
        else :
            command, x = statement
            deq = statements_dict[command](x, deq)


main()