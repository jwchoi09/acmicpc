"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.


"""

import sys

def gcd(a, b):
    # Euclidean
    if b == 0:
        return a

    else:
        return gcd(b, a % b)

def main():
    t = int(sys.stdin.readline().strip())
    nums = []
    for _ in range(t):
        nums = list(map(int, sys.stdin.readline().split()))
        n = nums.pop(0) # pop(0):  pop first element from list
        nums.sort()
        sum = 0
        for i in range(n):
            for j in range(i+1, len(nums)):
                sum += gcd(nums[j], nums[i])


        print(sum)


main()
