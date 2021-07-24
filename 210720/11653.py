"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.


"""

import sys

def main():
    N = int(sys.stdin.readline())
    d = 2
    while N != 1:
        if N % d == 0:
            print(d)
            N //= d

        else:
            d+=1

main()
