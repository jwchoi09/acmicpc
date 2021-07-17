"""
수빈이는 동생 N명과 숨바꼭질을 하고 있다. 수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.

수빈이는 걸어서 이동을 할 수 있다. 수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.

모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.

"""

import sys

def gcd(a, b):
    # Euclidean
    if b == 0:
        return a

    else:
        return gcd(b, a % b)

def main():
    N, S = map(int, sys.stdin.readline().split())
    # N: num of people, S = current position
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()

    distance = []
    
    for i in A:
        distance.append(abs(S-i))

    # 동생이 한명일 경우
    if len(distance) == 1:
        print(distance[0])

    else:
        sum = 0
        ans = []
        d = 0
        for i in range(N-1):
            d = gcd(distance[i], distance[i+1])
            ans.append(d)
            
        print(min(ans))

main()
