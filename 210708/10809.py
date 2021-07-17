"""

"""

import sys

def main():
    S = sys.stdin.readline().strip()
    num_alpha = [-1]*26

    for i in range(len(S)-1, -1, -1):
        num_alpha[ord(S[i]) - ord("a")] = i

    for j in num_alpha:
        print(j, end=" ")

main()
