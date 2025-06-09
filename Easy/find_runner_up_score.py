# Problem: Find the Runner-Up Score!
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    scores = sorted((map(int, input().split())), reverse=True)
        
    highest = 0
    rn_up = 0
    for i, score in enumerate(scores):
        if i == 0:
            highest = score
        if score < highest:
            rn_up = score
            break
            
    print(rn_up)