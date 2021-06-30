"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

"""

def main():
    N = int(input())
    sum = []
    for i in range(N):
        left, right = input().split()
        left = int(left)
        right = int(right)
        sum.append(left+right)

    for j in sum:
        print(j)

main()