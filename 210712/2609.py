"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


"""

import sys

def gcd(a, b):
    # Euclidean
    if b == 0:
        return a

    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def main():
    a, b = map(int, sys.stdin.readline().split())
    # 최대공약수: GCD (Greatest Common Divisor)
    # 최소공배수: LCM (Least Common Multiple)
    dividend = max(a, b)
    divisor = min(a, b)
    print(gcd(dividend, divisor))
    print(int(lcm(dividend, divisor)))


main()
