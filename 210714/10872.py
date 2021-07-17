"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.


"""

import sys

def main():
    N = int(sys.stdin.readline().strip())
    ans = 1
    for i in range(1, N+1):
        ans = ans * i

    print(ans)
    
main()