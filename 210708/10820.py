"""

"""

import sys

def main():
    while True:
        ans = [0] * 4
        S = sys.stdin.readline().rstrip("\n")
        # need to account for leading and trailing whitespaces. Therefore use rstrip() only with "newspace

        if not S:
            break
        
        for c in S:
            if c.islower():
                ans[0] += 1

            elif c.isupper():
                ans[1] += 1

            elif c.isdigit():
                ans[2] += 1

            elif c.isspace():
                ans[3] += 1

        for i in ans:
            print(i, end=" ")

        print()

main()
