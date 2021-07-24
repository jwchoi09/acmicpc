"""
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

"""
"""
dp[n] = dp[n-1] + dp[n-2]
"""

import sys

def main():
    N = int(sys.stdin.readline())
    ans = [0, 1, 2]
    for i in range(3, N+1):
        ans.append(ans[i-1]+ans[i-2])
    
    print(ans[N] % 10007)


main()
