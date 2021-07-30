import random
import matplotlib.pyplot as plt

from modu.template import ChangeTemperatureOnMyBirthday
from modu.template.basic_hist import highest_temperature


def sorted_random_arr(count) ->[] :
    arr = []
    [arr.append(random.randint(1, 1000)) for i in range(count)]
    return arr


def show_box_highest_temperature(arr:[]):
    plt.boxplot(arr)
    plt.show()


def show_boxplot_month(month):
    plt.boxplot(highest_temperature(month))
    plt.show()


def show_boxplot_all_month_day():
    birth = ChangeTemperatureOnMyBirthday()
    birth.read_data()
    arr = birth.data

    day = []
    [day.append([]) for i in range(31)]
    print(day)

    [day[int(i[0].split('-')[2])-1].append(float(i[-1]))
        for i in arr
            if i[-1] != ''
                if i[0].split('-')[1] == '08']

    plt.style.use('ggplot') #Grape Style
    plt.figure(figsize=(10,5), dpi=300) #Grape Size
    plt.boxplot(day, showfliers=False) #Omit Outlier

    plt.show()


def show_box_all_month():
    birth = ChangeTemperatureOnMyBirthday()
    birth.read_data()
    arr = birth.data
    month = [[], [], [], [], [], [], [], [], [], [], [], []]
    '''
    for i in arr:
        if i[-1] != '':
            month[int(i[0].split('-')[1]) - 1].append(float(i[-1]))
    '''
    [month[int(j[0].split('-')[1]) - 1].append(float(j[-1])) for j in arr if j[-1] != '']

    plt.boxplot(month)
    plt.show()


def show_boxplot_per_date(month: str):
    pass


if __name__ == '__main__':
    # show_box_highest_temperature(sorted_random_arr(13))
    # show_boxplot_month('03')
    show_boxplot_all_month_day()
    # show_box_all_month()