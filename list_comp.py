"""HACKER RANK LIST COMPREHENSIONS"""

"""Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]"""

# def main(x, y, n):
#     ar = []
#     p = 0
    # for i in range(x + 1):
    #     for j in range(y + 1):
    #         if i + j != n:
    #             ar.append([])
    #             ar[p] = [i, j]
    #             p += 1
    #             print(ar)

from sys import stdin
x,y,z,n = map(int, stdin.readlines())

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())