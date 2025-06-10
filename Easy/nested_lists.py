# Problem: Nested Lists
# Difficulty: Easy
# URL: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    
    records = []
    for _ in range(int(input())):
        name = input()
        score = input()
        if score != '':
            score = float(score)
        else:
            break
        records.append([name, score])

    grades = [sublist[1] for sublist in records]
    grades.sort()

    records.sort(key=lambda x: x[1])
    records.sort(key=lambda x: x[0])

    low_grade = min(grades)
    rn_up_low = float()
    for grade in grades:
        if grade > low_grade:
            rn_up_low = grade
            break

    for sublist in records:
        if sublist[1] == rn_up_low:
            print(sublist[0])
        continue