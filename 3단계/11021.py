"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

"""

import sys

def main():
    N = int(input())
    for i in range(1, N+1):
        left, right = map(int, sys.stdin.readline().split())
        print("Case #{}: {} + {} = {}".format(i, left, right, left+right))

main()