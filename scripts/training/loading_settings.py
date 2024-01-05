from sklearn.impute import SimpleImputer # Объект для замены пропущенных значений
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler # Импортируем нормализацию и One-Hot Encoding от scki-kit-learn
from sklearn.pipeline import Pipeline # Pipeline.Не добавить, не убавить
from sklearn.compose import ColumnTransformer # т.н. преобразователь колонок

cat_columns = []
num_columns = []

for column_name in DF_total.columns:
    if (DF_total[column_name].dtypes == object):
        cat_columns +=[column_name]
    else:
        num_columns +=[column_name]

print('categorical columns:\t ',cat_columns, '\n len = ',len(cat_columns))

print('numerical columns:\t ',  num_columns, '\n len = ',len(num_columns))

# Составляем пайплайн численных и категориальных данных
numerical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', MinMaxScaler())
])

categorical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent', )),
    ('encoder', OneHotEncoder(drop='if_binary', handle_unknown='ignore', sparse_output=False))
])

# ColumnTransformer, куда на вход ему также подаем список из того, что мы хотим объединить в формате
preprocessors = ColumnTransformer(transformers=[
    ('num', numerical_pipe, num_columns),
    ('cat', categorical_pipe, cat_columns)
])
preprocessors.fit(Train)

#разбиваем данные через дополнительные переменные X_train и X_test
X_train = preprocessors.transform(Train) # преобразуем  тренировочные данные
X_test = preprocessors.transform(Test) # преобразуем  тестовые данные
y_train = Target['weighted_score'].values.ravel()
#X_train_, X_val, y_train_, y_val = train_test_split(X_train,y_train,test_size = 0.2, random_state = 42)