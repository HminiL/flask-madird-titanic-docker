import csv
import matplotlib.pyplot as plt
'''
next()는 두 가지 포맷으로 사용된다. 
function 구조로 사용되면 header만 리턴한다.
consumer 구조로 사용되면 data에서 header를 제거한다.

data: [] = list()는 list 타입의 data를 list()로 초기화 시키는 것이다.
단,한 메소드 내에서만 사용하면 로컬에서 초기화한다. 예제는 다음과 같다.
data: [] = None
def save_highest_temperature(self):
    data = list()
그러나 여러메소드에서 사용하면 필드에서 초기화한다. 예제는 다음과 같다.
data:[] = list()

row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] 최고기온은 -1(뒤에서 첫번째, =4)이다.
'''

class ChangeTemperatureOnMyBirthday():
    data: [] = list()
    highest_temperature: [] = list()
    lowest_temperature: [] = list()

    def processing(self):
        self.read_data()
        self.highest_temperature()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('data/seoul.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def show_highest_temperature(self):
        # print([i[-1] for i in self.data])
        return [i[-1] for i in self.data]

    def save_highest_temperature(self):
        [(self.highest_temperature.append(float(i[-1]))) for i in self.data if i[-1] != '']
        print(f' 총 {len(self.highest_temperature)}개')

    def highest_temperature_my_birthday(self):
        high = []  # 최고기온
        low = []
        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1995 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '10':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))

        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title("내 생일의 기온 변화 그래프")
        plt.plot(high, 'hotpink',label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show()

    def visualize_data(self):
        plt.plot(self.high, 'hotpink')
        plt.plot(self.low, 'skyblue')
        plt.show()


    def extract_date_data(self):
        '''
        for i in self.data:
            if i[-1] != '':
                if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '10':
                    self.highest_temperature.append(float(i[-1]))
        '''

        [(self.highest_temperature.append(float(i[-1]))) for i in self.data if i[-1] != ''
         if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '10']
        [(self.lowest_temperature.append(float(i[-2]))) for i in self.data if i[-2] != ''
         if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '10']
        print(self.highest_temperature)


if __name__ == '__main__':
    this = ChangeTemperatureOnMyBirthday()
    this.read_data()
    # print([i for i in this.data])
    # this.show_highest_temperature()
    # this.save_highest_temperature()
    this.highest_temperature_my_birthday()
    # this.visualize_data()
    # this.extract_date_data()
    # this.visualize_highest_data()
    # this.visualize_lowest_data()
