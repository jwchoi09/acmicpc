"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

"""

import sys

def main():
    C = int(sys.stdin.readline().strip())
    N = []
    for i in range(C):
        N.append(list(map(int, sys.stdin.readline().split())))

    for j in N:
        cnt = 0
        num_stu = j[0]
        over_avg = 0
        avg = (sum(j) - num_stu) / num_stu
        for k in range(1, len(j)):
            if j[k] > avg:
                over_avg = over_avg + 1
        
        over_avg_cnt = (over_avg / num_stu) * 100
        print("{:.3f}%".format(round(over_avg_cnt,3)))

main()