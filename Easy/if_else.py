# Problem: If-Else
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/py-if-else/problem

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def is_weird(n):
    if not is_even(n):
        return True
    else:
        if n in range(2, 6):
            return False
        elif n in range(6, 21):
            return True
        elif n > 20:
            return False
    
if __name__ == '__main__':
    n = int(input().strip())
    print("Weird" if is_weird(n) else "Not Weird")