"""
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
"""

import sys

def equation1(A, B, C):
    return (A+B) % C

def equation2(A, B, C):
    return ((A%C) + (B%C)) % C

def equation3(A, B, C):
    return (A*B) % C

def equation4(A, B, C):
    return ((A%C) * (B%C)) % C

def main():
    A, B, C = map(int, sys.stdin.readline().split())
    print(equation1(A, B, C))
    print(equation2(A, B, C))
    print(equation3(A, B, C))
    print(equation4(A, B, C))


main()
