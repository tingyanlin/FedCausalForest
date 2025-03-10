# 標準庫與第三方套件
import pandas as pd

# 自訂義檔案
import analysis
import visualization
import config

from causal_random_forest import CausalRandomForest


def main():
    model = CausalRandomForest(
        config.DATA_CONFIG['DATASET'],
        config.CAUSAL_FOREST_CONFIG['OUTCOME_COLUMN'],
        config.CAUSAL_FOREST_CONFIG['TREATMENT_COLUMN'],
        config.CAUSAL_FOREST_CONFIG['N_ESTIMATORS'],
        config.CAUSAL_FOREST_CONFIG['MAX_DEPTH'],
        config.CAUSAL_FOREST_CONFIG['MIN_SAMPLES_LEAF'],
        config.CAUSAL_FOREST_CONFIG['RANDOM_STATE'])

    model.fit()

    # 計算 treatment effect 與 confidence interval
    effect, lower, upper = analysis.predict_effect_with_ci(
        model,
        model.data,
        model.feature_columns,
        config.ANALYSIS_CONFIG['TREATMENT_TYPE'],
        config.ANALYSIS_CONFIG['SIGNIFICANCE_LEVEL']
    )

    treatment_effect_df = pd.DataFrame({
        'Treatment Effect': effect,
        'Lower Treatment Effect': lower,
        'Upper Treatment Effect': upper
    })

    analysis.save_results(treatment_effect_df, config.DATA_CONFIG['TREATMENT_EFFECT'])

    # 取得特徵的貢獻度
    importance = analysis.feature_importance(model)

    feature_importance_df = pd.DataFrame({
        'Feature': model.feature_columns,
        'Importance': importance
    })

    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    analysis.save_results(feature_importance_df, config.DATA_CONFIG['FEATURE_IMPORTANCE'])


    # Causal Tree 可視化
    visualization.plot_causal_tree(
        model,
        config.CAUSAL_FOREST_CONFIG['MAX_DEPTH'],
        config.CAUSAL_FOREST_CONFIG['MIN_SAMPLES_LEAF']
    )


    # SHAP 特徵貢獻度可視化
    visualization.plot_shap_feature_importance(model)





    # causal_forest = model.model.model_final_
    #
    # visualization.plot_shap_analysis(
    #     causal_forest,
    #     model.data[model.feature_columns],
    #     model.feature_columns
    # )

if __name__ == '__main__':
    main()