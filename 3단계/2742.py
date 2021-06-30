"""
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

"""

def main():
    N = int(input())
    for i in range(0, N):
        print(N - i)

main()