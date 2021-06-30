"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

"""

import sys

def main():
    while True:
        try:
            left, right = map(int, sys.stdin.readline().split())       
            sys.stdout.write(str(left + right) + "\n")
        except:
            break

main()