"""
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.

"""

import sys

def main():
    N = int(sys.stdin.readline())
    ans = [0, 1, 3]
    for i in range(3, N+1):
        ans.append(ans[i-1]+2*ans[i-2])
    
    print(ans[N] % 10007)

main()
