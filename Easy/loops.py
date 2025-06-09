# Problem: Loops
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20:
        for i in range(n):
            print(i**2)
    else:
        print("Invalid number input. Must be in 1-20 range.")