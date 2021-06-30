"""
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.



(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

"""


def main():
    #a, b = input().split()
    a = int(input())
    b = int(input())
    bcopy = b

    num_pos = []
    while b != 0:
        num_pos.append(b % 10)
        b = b // 10

    num_q = []
    for i in num_pos:
        num_q.append(i * a)

    num_q.append(a*bcopy)
    for j in num_q:
        print(j)

main()