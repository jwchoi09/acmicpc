"""
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

"""

import sys

def main():
    N = int(sys.stdin.readline())
    for i in range(N):
        s = list(sys.stdin.readline().split())
        new_s = ""
        for j in s:
            new_s_j = ""
            for k in range(len(j)-1, -1, -1):
                new_s_j = new_s_j + j[k]

            #new_s = new_s + j[::-1] + " "
            new_s = new_s + new_s_j + " "

        new_s = new_s.strip()
        print(new_s)


main()

#Question: Pythonic way vs. Traditional way
"""
For example, when reversing a string, we normally need two strings. Original string A, and temporal string B.
In python, we only need [::-1] to reverse a string.
What is better?

"""