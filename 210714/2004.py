"""

nCm 의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오

0의 개수 = 
min (
        M!의 2의 개수 - N!의 2의개수 - (M-N)!의 2의 개수
    )
/
min (
        M!의 5의 개수 - N!의 5의개수 - (M-N)!의 5의 개수
    )

"""

import sys

def countNum(x, k):
    cnt = 0
    while x:
        x //= k
        cnt += x
    return cnt


def main():
    n, m = map(int, sys.stdin.readline().split())
    cntFive = countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5)
    cntTwo = countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2)
    ans = min(cntFive, cntTwo)
    print(ans)

main()
