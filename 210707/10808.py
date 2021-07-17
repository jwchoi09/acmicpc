"""

"""

import sys

def main():
    S = sys.stdin.readline().strip()
    num_alpha = [0]*26

    for i in S:
        num_alpha[ord(i) - ord("a")] += 1

    for j in num_alpha:
        print(j, end=" ")

main()
