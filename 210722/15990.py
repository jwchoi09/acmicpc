"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

1+2+1
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

"""

import sys

def main():
    T = int(sys.stdin.readline())
    nums = []
    for _ in range(T):
        nums.append(int(sys.stdin.readline()))

    max_num = max(nums)
    divisor = 1000000009

    #ans = [[0]*4]*max_num
    #ans = [[]]
    ans = [ [0]*4 for _ in range(max_num)]
    ans[0] = [0, 0, 0, 0]
    ans[1] = [0, 1, 0, 0]
    ans[2] = [0, 0, 1, 0]
    ans[3] = [0, 1, 1, 1]

    for i in range(4, max_num+1):
        #ans.append(ans[i-3] + ans[i-2] + ans[i-1])
        ans[i][1] = (ans[i - 1][2] + ans[i - 1][3] % divisor)
        ans[i][2] = (ans[i - 2][1] + ans[i - 2][3] % divisor)
        ans[i][3] = (ans[i - 3][1] + ans[i - 3][2] % divisor)

    for j in nums:
        print(sum(ans[j]) % divisor)

main()
