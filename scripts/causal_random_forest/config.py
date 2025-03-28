from pathlib import Path
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV

"""
=========================================

                  資料集

=========================================
"""
DATA_DIR = Path('./data')
DATA_CONFIG = {
    'DATASET': DATA_DIR / 'data_91.csv',
    'TREATMENT_EFFECT': DATA_DIR / 'treatment_effect.csv',
    'FEATURE_IMPORTANCE': DATA_DIR / 'feature_importance.csv',
    'TREE_FIGURE': DATA_DIR / 'tree_figure.png'
}


"""
=========================================

           CausalForestDML設定

=========================================
"""
CAUSAL_FOREST_CONFIG = {
    'TREATMENT_COLUMN': 'type',
    'OUTCOME_COLUMN': 'income',
    'CONTROL_COLUMN': None,
    'N_ESTIMATORS': 100,      # 樹的數量，影響模型穩定性，預設為 100 且需能被 4 整除
    'MAX_DEPTH': 4,
    'MIN_SAMPLES_LEAF': 5,    # 最小 leaf 節點數，防止 overfitting，預設為 5
    'RANDOM_STATE': 42,
    'MODEL_T': LassoCV(cv=3)
}


"""
=========================================

            Analysis設定            

=========================================
"""
ANALYSIS_CONFIG = {
    # 若 T 為連續變數使用 TE
    # 若 T 為離散變數使用 ATE
    'TREATMENT_TYPE': 'ATE',
    'SIGNIFICANCE_LEVEL': 0.05
}


"""
=========================================

            Visualization設定            

=========================================
"""
VISUALIZATION_CONFIG = {
    'TREE_INDEX': 0
}