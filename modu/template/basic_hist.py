import matplotlib.pyplot as plt
import random
import csv

from modu.template import ChangeTemperatureOnMyBirthday


def hist_show():
    plt.hist([1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 10])
    plt.show()


def dice_random(count):
    # print(random.randint(1,6))
    dice = []
    '''
    for i in range(5):
        dice.append(random.randint(1,6))
    print(dice)
    '''
    [dice.append(random.randint(1, 6)) for i in range(count)]
    return dice

def show_hist(dice):
    plt.hist(dice, bins=6)
    plt.show()
    print(dice)


def highest_temperature(month) -> []:
    birth= ChangeTemperatureOnMyBirthday()
    birth.read_data()
    #[print(i) for i in birth.data]
    arr = []
    [arr.append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month]
    return arr
    # 35line append가 consumer라서 바로 리턴X


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='r', label=f'{month}Month')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    show_hist(dice_random(10))
    # show_hist_about(highest_temperature('11'), '11')

