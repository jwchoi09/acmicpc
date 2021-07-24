"""
45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

"""
# 참고: https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98

import sys

def main():
    N = int(sys.stdin.readline())
    stairs = [[0] * 10 for _ in range(N+1)]

    stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, N+1):
        stairs[i][0] = stairs[i-1][1]
        stairs[i][9] = stairs[i-1][8]

        for j in range(1, 9):
            stairs[i][j] = stairs[i-1][j-1] + stairs[i-1][j+1]

    print(sum(stairs[N]) % 1000000000)

main()
