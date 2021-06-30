"""
셀프넘버
"""

def main():
    self_num_list = [0]*10001
    
    for i in range(1, 10001):
        x = i
        while True:
            digits = [int(k) for k in str(x)]
            x = x + sum(digits)
            if x > 10000:
                break

            self_num_list[x] = self_num_list[x] + 1

    for j in range(1, 10001):
        if self_num_list[j] == 0:
            print(j)

main()