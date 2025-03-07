# 標準庫與第三方套件


def check_model_fit(causal_forest):
    if causal_forest is None:
        raise ValueError('Causal Forest is not Fit')

def predict_effect_with_ci(causal_forest, data, feature_columns, treatment_type, significance_level):
    check_model_fit(causal_forest)

    X = data[feature_columns].values

    if treatment_type == 'TE':
        effect = causal_forest.model.effect(X)
        lower, upper = causal_forest.model.effect_interval(X, alpha=significance_level)

        return effect, lower, upper

    elif treatment_type == 'ATE':
        effect = causal_forest.model.effect(X)
        lower, upper = causal_forest.model.effect_interval(X, alpha=significance_level)

        return effect, lower, upper

    else:
        raise ValueError(f"Invalid treatment_type: {treatment_type}. Please use 'TE' or 'ATE'.")

def feature_importance(causal_forest):
    check_model_fit(causal_forest)

    importance = causal_forest.model.feature_importances_

    return importance

def save_results(df, file_path):
    df.to_csv(file_path, index=False, encoding='utf-8')
    print(f"Results saved to {file_path}")
