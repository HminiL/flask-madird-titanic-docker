class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)


def main():
    grade = Grade(input('name : '))
    for i in ['Korean', 'English', 'Math']:
        grade.addScores(int(input(f'{i} : ')))
    avg = int(grade.avg())
    if avg >= 90:
        result = 'A'
    elif avg >= 80:
        result = 'B'
    elif avg >= 70:
        result = 'C'
    elif avg >= 60:
        result = 'D'
    else:
        result = 'F'
    print('*' * 100)
    print(f'Average : {avg}')
    print(f'Grade : {result}')
    print('*' * 100)


if __name__ == '__main__':
    main()

