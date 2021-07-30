from scraping.models.dataset import Dataset
from scraping.models.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, bugs, melon):
        this = self.preprocessing(bugs, melon)
        print(type(this))
        print('*'*100)
        print(this.bugs.head(3))
        print('*'*100)
        print(this.melon.head(3))

    def preprocessing(self, bugs, melon) -> object:
        service = self.service
        this = self.dataset
        this.bugs = service.new_model(bugs)
        this.melon = service.new_model(melon)
        return this


if __name__ == '__main__':
    view = View()
    view.modeling('bugs.csv', 'melon.csv')