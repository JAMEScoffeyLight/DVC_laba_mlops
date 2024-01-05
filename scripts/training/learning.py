from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate

from sklearn.linear_model import Ridge # Регуляризация Ridge от scikit-learn

model = Ridge(alpha=0.001, random_state=42)

model.fit(X_train, Target)

scoring = {'R2': 'r2',
           '-MSE': 'neg_mean_squared_error',
           '-MAE': 'neg_mean_absolute_error',
           'Max': 'max_error'}


scores = cross_validate(model, X_train, y_train,
                      scoring=scoring, cv=ShuffleSplit(n_splits=5, random_state=42) )
DF_cv_linreg = pd.DataFrame(scores)
DF_cv_linreg.to_csv('model_score.csv', index = True)
