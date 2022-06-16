'''
Main module for application.
'''
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from catboost import CatBoostRegressor
import numpy as np
from .preprocessing import get_df

LABEL = 'SalePrice'

def main():
    '''
    Main Function
    '''
    df = get_df()

    X = df.drop(['SalePrice', 'Id'], axis=1)
    y = df[LABEL]

    k_fold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
    )

    scores = []
    for train_index, test_index in k_fold.split(X):
        X_train, X_test = X.loc[train_index], X.loc[test_index]
        y_train, y_test = y.loc[train_index], y.loc[test_index]

        reg = CatBoostRegressor(
            depth=7,
            iterations=1500,
            learning_rate = 0.025,
            logging_level='Silent'
            )

        reg.fit(X_train, y_train)

        y_predict = reg.predict(X_test)

        acc_score = np.sqrt(mean_squared_error(y_test, y_predict))

        print(acc_score)

        scores.append(acc_score)

    print()
    print("Average:", np.sum(scores)/5)
    print("Std:", round(np.std(scores), 3))

if __name__  == '__main__':
    main()
    print("Done")
