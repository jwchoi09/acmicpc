'''
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
'''

def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    q1 = (a+b)%c
    q2 = ((a%c) + (b%c))%c
    q3 = (a*b)%c
    q4 = ((a%c) * (b%c))%c

    #print(q1, "\n", q2, "\n", q3, "\n", q4)
    print(q1)
    print(q2)
    print(q3)
    print(q4)

main()