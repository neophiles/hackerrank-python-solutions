# Problem: Write a Function
# Difficulty: Medium
# URL: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
            
    return False

year = int(input())
print(is_leap(year))