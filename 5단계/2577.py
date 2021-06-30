"""
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
"""

import sys

def main():
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    c = int(sys.stdin.readline().strip())
    prod = a*b*c
    num_list = []
    #while prod != 0:
        #num_list.append(prod % 10)
        #prod = prod // 10
    num_list = list(str(a*b*c))

    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #print(num_list)

    for i in num_list:
        #print("i: ", i)
        cnt[int(i)] = cnt[int(i)] + 1

    for j in cnt:
        print(j)

main()