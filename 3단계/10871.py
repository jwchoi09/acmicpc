"""
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

"""

import sys

def main():
    N, X = map(int, sys.stdin.readline().split())
    str1 = ""
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        if arr[i] < X:
            str1 = str1 + str(arr[i]) + " "

    print(str1.strip())

main()