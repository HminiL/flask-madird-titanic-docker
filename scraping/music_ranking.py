from bs4 import BeautifulSoup
import requests
import pandas as pd

from commom.menu import print_menu


class MusicRanking(object):

    domain = ''
    query_string = ''
    html = ''
    tag_name = ''
    fname = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'Crawling HTML is \n {self.html}')

    def get_ranking(self):
        _=0
        soup = BeautifulSoup(self.html, 'lxml')
        a = soup.find_all(self.tag_name, self.class_name[0])
        t = soup.find_all(self.tag_name, self.class_name[1])
        for i, j in zip(a, t):
            _ += 1
            #print(f'{str(_)}Rank {i.find("a").text} : {j.find("a")}.text')
            self.artists.append(f'{i.find("a").text}')
            self.titles.append(f'{j.find("a").text}')
        print("*"*100)
        print(self.artists)
        print(self.titles)

    def insert_dict(self):
        '''
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        '''
        # 방법 3
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]

        print(self.dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


def main():
    mr = MusicRanking()
    while 1 :
        menu = print_menu(['exit', 'Bugs', 'Melon', 'output', 'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            mr.fname = 'bugs'
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = f'chartdate={"20210720"}&charthour={"16"}'
            mr.set_html()
        elif menu == 2:
            mr.fname = 'melon'
            mr.domain = 'https://www.melon.com/chart/index.htm?'
            mr.query_string = f'dayTime={"2021072111"}'
            mr.set_html()
        elif menu == 3:
            mr.tag_name = 'div'
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.get_ranking()
        elif menu == 4:
            mr.insert_dict()
        elif menu == 5:
            mr.dict_to_dataframe()
        elif menu == 6:
            mr.df_to_csv()


if __name__ == '__main__':
    main()
