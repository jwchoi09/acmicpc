"""
"""

import sys

def main():
    str = list(sys.stdin.readline().strip())
    s2 = []
    N = int(sys.stdin.readline())
    cursor = len(str)

    for i in range(N):
        cmd = sys.stdin.readline().strip()
        if cmd[0] == "P":
            str.append(cmd[2])
        
        elif cmd[0] == "L" and str != []:
            s2.append(str.pop())
        
        elif cmd[0] == "D" and s2 != []:
            str.append(s2.pop())

        elif cmd[0] == "B" and str != []:
            str.pop()

    print("".join(str + list(reversed(s2))))

main()