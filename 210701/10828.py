import sys
#push x, pop, size, empty, top
def main():
    N = int(sys.stdin.readline())
    temp = []

    for i in range(N):
        cmd = list(sys.stdin.readline().split())
        if cmd[0] == "push":
            temp.append(int(cmd[1]))

        elif cmd[0] == "pop":
            
            if len(temp) == 0:
                print("-1")
            
            else:
                print(temp[-1])
                temp.pop()

        elif cmd[0] == "size":
            print(len(temp))

        elif cmd[0] == "empty":

            if len(temp) == 0:
                print("1")

            else:
                print("0")

        elif cmd[0] == "top":

            if len(temp) == 0:
                print("-1")

            else:
                print(temp[-1])

main()