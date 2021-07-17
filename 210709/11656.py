"""

"""

import sys

def main():
    S = sys.stdin.readline().strip()
    arr = []
    for i in range(len(S)):
        arr.append(S[i:])

    #sorted_arr = sorted(arr)
    arr.sort()
    
    for j in arr:
        print(j)

main()
