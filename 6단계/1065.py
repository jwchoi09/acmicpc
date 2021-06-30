"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

"""

import sys

def han_num(num):
    han_num_cnt = 0
    
    for i in range(1, num+1):
        diff = []
        num_list = list(map(int, str(i)))
        if len(num_list) <= 2:
            han_num_cnt += 1
        
        else:
            for j in range(1, len(num_list)):
                diff.append(num_list[j-1] - num_list[j]+1)

            num_diff = len(set(diff))
            if num_diff == 1:
                han_num_cnt += 1
    
    return han_num_cnt

def main():
    N = int(sys.stdin.readline().strip())
    print(han_num(N))
    
main()
