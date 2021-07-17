"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.


"""

import sys

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

def main():
    N = int(sys.stdin.readline().strip())
    num = list(map(int, sys.stdin.readline().split()))
    counter = 0
    for i in num:
        if isPrime(i):
            counter += 1

    print(counter)

main()
