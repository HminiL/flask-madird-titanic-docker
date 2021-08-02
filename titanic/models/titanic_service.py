from titanic.models.dataset import Dataset
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier


class TitanicService(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        # this = self.dataset
        # this.context = './data/'
        # this.fname = payload
        return pd.read_csv(f"/data/{payload}.csv")

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this


    def embarked_nominal(this):
        return this


    def fare_oridnal(this):
        return this


    def title_nominal(this):
        return this


    def gender_norminal(this):
        return this


    def age_ordinal(this):
        return this


    def create_k_fold(this):
        return None


    def accuracy_by_classfier(this):
        return  ""