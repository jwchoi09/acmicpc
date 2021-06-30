"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

"""

import sys

def main():
    N = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    min = a[0]
    max = a[0]

    for i in range(len(a)-1):
        if a[i+1] > max:
            max = a[i+1]
        
        if a[i+1] < min:
            min = a[i+1]

    str1 = str(min) + " " + str(max)
    #print(str1)
    sys.stdout.write(str1)


main()