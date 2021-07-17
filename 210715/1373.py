"""
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.


"""

import sys

def main():
    N = int((sys.stdin.readline().strip()), 2)
    # int(x, 2) we need to specifiy the input characteristic, whether it is binary, octal, hex.
    # default is 10
    print(oct(N)[2:])

main()
