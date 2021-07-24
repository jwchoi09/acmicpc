"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

"""

import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    ans = [1]*N
    #arr = [[x] for x in A]

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                ans[i] = max(ans[i], ans[j]+1)

    l_cnt = max(ans)
    print(l_cnt)

    #idx = ans.index(l_cnt)
    A2 = []
    """
    while idx >= 0:
        if ans[idx] == l_cnt:
            A2.append(A[idx])
            l_cnt -= 1
        idx -= 1
    
    for k in A2[::-1]:
        print(k, end=" ")
    
    print()"""
    for k in range(N-1, -1, -1):
        if ans[k] == l_cnt:
            A2.append(A[k])
            l_cnt -= 1

    A2 = A2[::-1]
    for l in A2:
        print(l, end=" ")

main()
