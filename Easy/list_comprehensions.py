# Problem: List Comprehensions
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n])