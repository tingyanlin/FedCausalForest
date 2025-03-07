# 標準庫與第三方套件
import pandas as pd

from econml.dml import CausalForestDML
from sklearn.ensemble import RandomForestRegressor

# 自訂義檔案
import config


class CausalRandomForest:
    def __init__(self, data_path, outcome_column, treatment_column,
                 n_estimators, min_samples_leaf, random_state):
        self.data_path = data_path
        self.outcome_column = outcome_column
        self.treatment_column = treatment_column
        self.n_estimators = n_estimators
        self.min_samples_leaf = min_samples_leaf
        self.random_state = random_state
        self.data = None
        self.model = None
        self.feature_columns = None

    def load_data(self):
        self.data = pd.read_csv(self.data_path, encoding='utf-8')

        all_columns = list(self.data.columns)
        self.feature_columns = []

        for column in all_columns:
            if column not in [self.outcome_column, self.treatment_column]:
                self.feature_columns.append(column)

    def fit(self):
        if self.data is None:
            self.load_data()

        X = self.data[self.feature_columns].values
        Y = self.data[self.outcome_column].values
        T = self.data[self.treatment_column].values

        # 建立 CausalForest
        self.model = CausalForestDML(
            model_y=RandomForestRegressor(
                n_estimators=self.n_estimators,
                min_samples_leaf=self.min_samples_leaf,
                random_state=self.random_state
            ),
            model_t=config.CAUSAL_FOREST_CONFIG['MODEL_T'],
            n_estimators=self.n_estimators,
            min_samples_leaf=self.min_samples_leaf,
            random_state=self.random_state
        )

        self.model.fit(Y=Y, T=T, X=X, cache_values=True) # cache_values 為存取統計數據