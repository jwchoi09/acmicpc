"""
쇠막대기

"""
import sys

def main():
    N = sys.stdin.readline().rstrip()
    pieces = 0
    cnt = 0

    for i in range(len(N)):
        if N[i] == ")":
            if N[i-1] == "(":
                if cnt != 0:
                    cnt -= 1
                
                else:
                    cnt = 0

                pieces += cnt
            
            else:
                pieces += 1
                cnt -= 1
        
        else:
            cnt += 1

    print(pieces)

main()
