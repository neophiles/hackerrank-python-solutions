# Problem: Print Function
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/python-print/problem

def sequence():
    n = int(input())
    num = 0
    
    for i in range(n):
        count = 0
        add = i+1
        while add != 0:
            add //= 10
            count += 1
        
        multiplier = 10 ** (count)
        num = (num * multiplier) + (i + 1)
        
    return num
    
if __name__ == '__main__':
    print(sequence())