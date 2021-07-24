"""
"""

import sys

def main():
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    A, B = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    dec = 0
    ans = []
    fin = ""

    for i in range(m):
        dec += nums[i] * (A ** i)
        #print(dec)

    while dec != 0:
        r = dec % B
        ans.append(r)
        dec //= B

    ans = ans[::-1]
    for j in ans:
        print(j, end=" ")
    #fin = " ".join(ans)
    print(fin)

main()

"""
import math # pow라는 n제곱을 쉽게 해주는 내장함수 이용을 위함

a, b = map(int, input().split())    # a진법의 수를 b진법으로
n = int(input())    # n자리수인 a진법 수
lists = list(map(int, input().split()))
ten = 0	# 10진법으로 만든 수
result = []
fin = ''

for i in range(n):
    ten += int(lists[i] * math.pow(a, n - i - 1))
    print(ten)

while ten:
    nam = ten % b
    result.append(str(nam))
    ten = ten // b

result = result[::-1]
fin = ' '.join(result)	# 절 대 띄 어 쓰 기 삽 입 해
print(fin)"""