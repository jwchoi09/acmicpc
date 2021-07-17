"""
            
            Example 1. "B"
                ord("B") = 66
                chr(66 + 13) = "O"

            but, what if chr value exceeded 90?

            Example 2. "O"
                ord("O") = 79
                79 + 13 > 90 # illegal, encrypted goal: "B"

                First, operate 79 + 13
                And subtract by 65 (ord("A")) # 92 - 65 = 27
                since we want a value between 0 and 26,
                we calculate the remainder when divided by 26
                27 % 26 = 1
                To get to "B", we add above value back with 65 (ord("A"))
                Therefore, chr(1 + 65) = "B"

            
"""

import sys

def main():
    S = sys.stdin.readline().rstrip()
    # leading character may be whitespace, so use rstrip()
    # Uppercase alphabets: 65 to 90
    # Lowercase alphabets: 97 to 122
    encrypted = ""
    for i in S:
        if i.isupper():
            encrypted += chr((ord(i) + 13 - ord("A")) % 26 + ord("A"))

        elif i.islower():
            encrypted += chr((ord(i) + 13 - ord("a")) % 26 + ord("a"))

        else:
            encrypted += i

    print(encrypted)

main()
