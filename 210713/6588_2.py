"""
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

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
    N = [] # list of input except for last 0

    # receive inputs and save them to list N, break if input equals 0
    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break
            
        N.append(n)

    # we will precalculate prime numbers of the biggest value from the list
    max_num = max(N)
    prime_nums = [0] * (max_num+1)
    for i in range(max_num+1):
        if isPrime(i):
            prime_nums[i] = i

    for i in N:
        for j in prime_nums:
            if isPrime(i - j):
                print("{} = {} + {}".format(i, j, i - j))
                break

main()
