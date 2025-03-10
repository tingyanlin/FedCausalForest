# 標準庫與第三方套件
import numpy as np
import shap
import matplotlib.pyplot as plt

from econml.cate_interpreter import SingleTreeCateInterpreter

# 自訂義檔案
import config


def plot_causal_tree(model, max_depth, min_samples_leaf):
    feature_columns = model.feature_columns
    X = model.data[model.feature_columns]

    interpreter = SingleTreeCateInterpreter(
        include_model_uncertainty=True,
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf
    )
    interpreter.interpret(model.model, X)

    plt.title("CATE Heterogeneity Tree")
    plt.figure(figsize=(50, 15))
    interpreter.plot(feature_names=feature_columns, fontsize=12)
    plt.savefig(fname=config.DATA_CONFIG['TREE_FIGURE'],dpi=600, bbox_inches='tight')
    print(f"Tree figure saved to {config.DATA_CONFIG['TREE_FIGURE']}")

def plot_shap_feature_importance(model):
    X = model.data[model.feature_columns]
    shap_values = model.model.shap_values(X)

    ind = 0
    shap.plots.force(shap_values['Y0']['T0'][ind], matplotlib=True)
    shap.summary_plot(shap_values['Y0']['T0'])















# def plot_causal_feature_importance(causal_forest, X, feature_names):
#     # 計算 SHAP 值
#     explainer = shap.TreeExplainer(causal_forest)
#     shap_values = explainer.shap_values(X)
#
#     # 計算平均絕對 SHAP 值
#     if len(shap_values.shape) == 2:
#         importance = np.mean(np.abs(shap_values), axis=0)
#     else:
#         importance = np.abs(shap_values).mean(axis=0)
#
#     # 檢查維度一致性
#     if len(importance) != len(feature_names):
#         raise ValueError(
#             f"特徵數量不一致：重要性分數數 ({len(importance)}) vs 特徵名稱數 ({len(feature_names)})"
#         )
#
#     # 排序並繪製
#     sorted_idx = importance.argsort()
#
#     plt.figure(figsize=(10, 6))
#     plt.barh(range(len(sorted_idx)), importance[sorted_idx], align='center')
#     plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
#     plt.title("Feature Importance via SHAP")
#     plt.xlabel("Mean |SHAP Value|")
#     plt.tight_layout()
#     plt.show()
#
#
#
#
#
#
# def plot_shap_analysis(causal_forest, X, feature_columns):
#     # explainer = shap.TreeExplainer(causal_forest)
#     # shap_values = explainer.shap_values(X)
#
#     explainer = shap.KernelExplainer(causal_forest.predict, X.iloc[:100, :])
#     shap_values = explainer.shap_values(X)
#     shap.summary_plot(shap_values, X, feature_names=feature_columns)
