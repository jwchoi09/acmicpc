"""
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.



"""

import sys

def main():
    N = int((sys.stdin.readline().strip()), 8)
    # int(x, 2) we need to specifiy the input characteristic, whether it is binary, octal, hex.
    # default is 10
    print(bin(N)[2:])

main()
