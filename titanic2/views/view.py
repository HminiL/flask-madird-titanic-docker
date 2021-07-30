from titanic2.models.dataset import Dataset
from titanic2.models.service import Service


class View():
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        this = self.processing(train, test)
        print(type(this))
        print('*'*100)
        print(this.train.head(2))
        print('*'*100)
        print(this.test.head(3))


    def processing(self, train, test):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        return this


if __name__ == '__main__':
    view = View()
    view.modeling('train.csv', 'test.csv')

