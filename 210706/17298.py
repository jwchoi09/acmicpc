"""
오큰수

"""
import sys

def main():
    N = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = [-1] * N
    i = 1
    stack = [0]

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack.pop()] = arr[i]
        stack.append(i)

    print(*answer)

main()