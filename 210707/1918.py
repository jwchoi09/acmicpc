"""

"""

# pemdas
import sys

def main():
    S = sys.stdin.readline().strip()
    ans = ""
    stack = []

    for i in S:
        if i.isalpha():
            ans += i

        else:
            if i == "(":
                stack.append(i)
        
            elif i == ")":
                while stack and stack[-1] != "(":
                    ans += stack.pop()

                stack.pop()

            elif i == "*" or i == "/":
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    ans += stack.pop()

                stack.append(i)

            elif i == "+" or i == "-":
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                
                stack.append(i)

    while stack:
        ans += stack.pop()

    print(ans)

main()