# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    A = a+b
    S = a-b
    P = a*b
    D = a//b
    R = a%b

    #print("{}\n{}\n{}\n{}\n{}".format(A, S, P, D, R))
    print(A)
    print(S)
    print(P)
    print(D)
    print(R)


main()