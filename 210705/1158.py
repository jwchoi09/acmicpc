"""

"""
import sys

def main():
    T, n = map(int, sys.stdin.readline().split())
    arr = []
    seq = []
    idx = 0

    for i in range (1, T+1):
        arr.append(i)

    for j in range(T):
        idx += n - 1
        if idx >= len(arr):
            idx = idx%len(arr)
        
        seq.append(str(arr.pop(idx)))
    print("<",", ".join(seq)[:],">", sep='')



main()


