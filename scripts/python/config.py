from pathlib import Path
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV

"""
=========================================

                  資料集

=========================================
"""
DATA_DIR = Path('./data')
DATA_CONFIG = {
    'DATASET': DATA_DIR / 'data_91.csv'
}


"""
=========================================

           CausalForestDML設定

=========================================
"""
CAUSAL_FOREST_CONFIG = {
    'OUTCOME_COLUMN': 'sex',
    'TREATMENT_COLUMN': 'kind',
    'N_ESTIMATORS': 100,      # 樹的數量，影響模型穩定性，預設為 100 且需能被 4 整除
    'MIN_SAMPLES_LEAF': 5,    # 最小 leaf 節點數，防止 overfitting，預設為 5
    'RANDOM_STATE': 42,
    'MODEL_T': LassoCV(cv=3)
}


"""
=========================================

            Visualization設定            

=========================================
"""
VISUALIZATION_CONFIG = {
    'TREE_INDEX': 0
}