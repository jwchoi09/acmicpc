"""

"""

import sys

def calc(l, r, op):
    if op == "+":
        return l+r
    
    elif op == "-":
        return l-r

    elif op == "*":
        return l*r

    elif op == "/":
        return l/r

def main():
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()
    arr = []
    var = []

    for i in range(N):
        arr.append(int(sys.stdin.readline().strip()))

    for j in S:
        if j.isalpha():
            var.append(arr[ord(j)-ord("A")])
        
        else:
            r = var.pop()
            l = var.pop()
            var.append(calc(l, r, j))

    print("{:.2f}".format(var[0]))

main()