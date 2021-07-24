"""
요즘 민규네 동네에서는 스타트링크에서 만든 PS카드를 모으는 것이 유행이다.


"""

import sys

def main():
    N = int(sys.stdin.readline())
    P = list(map(int, sys.stdin.readline().split()))
    ans = [0]*(N+1)

    for i in range(1, N+1):
        for j in range(1, i+1):
            ans[i] = max(ans[i], ans[i-j] + P[j-1])

    print(ans[N])


main()
