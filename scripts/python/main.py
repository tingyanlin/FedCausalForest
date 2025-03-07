# 自訂義檔案
import config

from causal_random_forest import CausalRandomForest


def main():
    model = CausalRandomForest(
        config.DATA_CONFIG['DATASET'],
        config.CAUSAL_FOREST_CONFIG['OUTCOME_COLUMN'],
        config.CAUSAL_FOREST_CONFIG['TREATMENT_COLUMN'],
        config.CAUSAL_FOREST_CONFIG['N_ESTIMATORS'],
        config.CAUSAL_FOREST_CONFIG['MIN_SAMPLES_LEAF'],
        config.CAUSAL_FOREST_CONFIG['RANDOM_STATE'])

    model.fit()

    effect = model.predict_effect()
    print(f"Estimated Treatment Effect: {effect}")

if __name__ == '__main__':
    main()