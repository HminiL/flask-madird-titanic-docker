class Grade(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return round((self.sum() / 3), 2)

    @staticmethod
    def main():
        kor = int(input('Korean : '))
        eng = int(input('English : '))
        math = int(input('Mathematics : '))
        grade = Grade(kor, eng, math)
        avg = grade.avg()

        if avg >= 90:
            result = 'A'
        elif avg >= int('80'):
            result = 'B'
        elif avg >= int('70'):
            result = 'C'
        elif avg >= int('60'):
            result = 'D'
        else:
            result = 'F'

        print('*' * 100)
        print(f'Average : {avg}')
        print(f'Grade : {result}')
        print('*' * 100)



Grade.main()

