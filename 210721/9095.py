"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.






"""

import sys

def main():
    T = int(sys.stdin.readline())
    nums = []
    for _ in range(T):
        nums.append(int(sys.stdin.readline()))

    max_num = max(nums)

    ans = [0, 1, 2, 4]
    for i in range(4, max_num+1):
        ans.append(ans[i-3] + ans[i-2] + ans[i-1])

    for j in nums:
        print(ans[j])

main()
