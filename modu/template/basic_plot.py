import matplotlib.pyplot as plt

from commom.menu import print_menu

"""
list 값은 y축 이고, x축은 0부터 1까지 자동으로 증가한다. 
"""
def plot_show():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], color='yellow')
    plt.show()

"""
첫 번째 리스트가 x축, 두 번째 리스트가 y축
"""
def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 46, 25, 15],linestyle = '--')
    plt.show()


def scatter():
    plt.title("marker")     #제목설정
    plt.plot([10, 20, 30, 40], 'r.', label='circle')        # 빨간색 원형 마커 그래프
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')   # 초록색 삼각형 마커 그래프
    plt.legend()        # 범례표시
    plt.show()



