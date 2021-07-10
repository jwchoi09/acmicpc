"""
오등큰수

"""

import sys
from collections import Counter

def main():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = Counter(arr)
    #for i in arr:
        #arr = [[i, cnt[i]]]
    arr = [[idx, cnt[idx]] for idx in arr]

    answer = [-1] * N
    i = 1
    stack = [0]

    for i in range(len(arr)):
        while stack and arr[stack[-1]][1] < arr[i][1]:
            answer[stack.pop()] = arr[i][0]
        stack.append(i)
    print(*answer)

main()