# Problem: String Validators
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    if 0 < len(s) < 1000:
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isnumeric() for c in s))
        print(any(c.islower() for c in s))
        print(any(c.isupper() for c in s))
    else:
        print("Invalid string length.")