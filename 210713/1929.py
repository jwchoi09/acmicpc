"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.


"""

import sys

def isPrime(x):
    if x == 2 or x == 3:
        return True

    if x == 1 or x%2 == 0 or x < 2:
        return False

    for i in range(3, int(x**0.5) + 1, 2):
        # 시간 초과가 떠서 range(2, x) 가 아닌 x의 제곱근까지만 검사
        # 시간 초과 또 떠서 range(2, x의 제곱근) 가 아닌 짝수는 버린다
        if x % i == 0:
            return False
    
    return True

def main():
    M, N = map(int, sys.stdin.readline().split())
    for i in range(M, N+1):
        if isPrime(i):
            print(i)

main()
