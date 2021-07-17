"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

Attempt 1: Solve factorial. Count zeros. Inefficient
Attempt 2: 소인수분해 10의 개수 = 0의 개수 
예를 들어 10! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 10
n%5 == 0일때는
n = 5, n = 10
Thus, 2

"""

import sys

def main():
    N = int(sys.stdin.readline().strip())
    facto = 1
    cnt = 0

    for i in range(1, N+1):
        facto = facto * i

    while facto % 10 == 0:
        facto = facto // 10
        cnt += 1

    print(cnt)

main()
