from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request


class Melon(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers = {"User-Agent": "Mozilla/5.0"})), "lxml")
        _ = 0
        ls = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        ls2 = soup.find_all('div', {'class': 'ellipsis rank01'})
        for i, j in zip(ls, ls2):
            _ += 1
            print(f'{str(_)}Rank : {i.find("a").text} : {j.find("a").text}')


def main():
    Melon(f'https://www.melon.com/chart/index.htm?dayTime={input("DayTime : ")}').scrap()


if __name__ == '__main__':
    main()
