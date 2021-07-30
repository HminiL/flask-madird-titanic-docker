import matplotlib.pyplot as plt
import numpy as np

class Numpy(object):
    def show_numpy(self):
        t = np.arange(0., 5., 0.2)
        plt.plot(t, t, 'b--', t, t**2, 'rs', t, t**3, 'y^')
        plt.show()

    def numpy_choice(self):
        dice = np.random.choice(6, 1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
        plt.hist(dice, bins=6)
        plt.show()

    def numpy_not_need_for_loop(self):
        x = np.random.randint(low=10, high=100, size=200)     # low, high=None, size=None, dtype=None
        y = np.random.randint(low=10, high=100, size=200)
        size = np.random.randint(100) *100

        plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
        plt.colorbar()
        plt.show()
    '''
    np.random.randint(low=0, high=100, size=200)
    low~high 추출되는 숫자의 범위
    size 추출되는 데이터의 숫자
    '''

    def indexing_slicing(self):
        a = np.array([1,2,3,4])
        print(f'list -> array : array : {a}')
        print(f'indexting a[1] : {a[1]}, indexing a[-1]: {a[-1]}')
        print(f'slicing a[1:] : {a[1]}')

    def array_have_one_type(self):
        a = np.array([1,2,'3',4])
        print(f'int -> str : {a}')

    def np_zeros(self):
        print(np.zeros(10))

    def np_ones(self):
        print(np.ones(10))

    def np_eye(self):
        print(np.eye(3))

    def np_arange(self):    # arange(start=None, *args, **kwargs)
        print(f'[0 1 2] : {np.arange(3)}')
        print(np.arange(start=3, stop=7)) # [3 4 5 6]
        print(np.arange(start=3, stop=7, step=2)) # [3 5]
        print(f'[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9] : {np.arange(start=1, stop=2, step=0.1)}')

    def np_linspace(self):
        a = np.linspace(1, 2, 11)
        print(f'[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ] : {a}')
        print({np.sqrt(a)})
        '''
        [1.         1.04880885 1.09544512 1.14017543 1.18321596 1.22474487
            1.26491106 1.30384048 1.34164079 1.37840488 1.41421356]
        '''

    def np_mask(self):
        a = np.arange(-5, 5)
        print(f'[-5 -4 -3 -2 -1] : {a[a < 0]}')   # [-5 -4 -3 -2 -1]
        mask1 = abs(a) > 3
        print(f'[-5 -4  4] : {a[mask1]}') # [-5 -4  4]
        mask2 = abs(a) % 2 == 0
        print(f'[-5 -4 -2  0  2  4] : {a[mask1 + mask2]}')  # 자바에서의 ||(or) 연산
        print(f'[-4  4] : {a[mask1 * mask2]}')  # 자바에서의 &&(and) 연산

    def np_bubble(self):
        x = np.random.randint(-100, 100, 1000)
        y = np.random.randint(-100, 100, 1000)
        size = np.random.randint(100) * 100
        mask1 = abs(x) > 50
        mask2 = abs(y) > 50
        x = x[mask1+mask2]
        y= y[mask1+mask2]
        plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
        plt.colorbar()
        plt.show()
