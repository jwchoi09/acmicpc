"""

"""

import sys

def main():
    S = sys.stdin.readline().rstrip()
    reverse_check = True
    ans = ''
    tmp = ''
    for c in S:
        if c == '<':
            reverse_check = False
            ans += tmp
            tmp = '<'
        elif c == '>':
            reverse_check = True
            ans += (tmp + '>')
            tmp = ''
        elif c == ' ':
            ans += (tmp + ' ')
            tmp = ''
        elif reverse_check:
            tmp = c + tmp
        else:
            tmp += c

    print(ans + tmp)

main()