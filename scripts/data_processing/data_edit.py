import pandas as pd

ass = pd.read_csv('assessments.csv') # работает в связке с results (пересекающиеся данные)
courses = pd.read_csv('courses.csv') #+
results = pd.read_csv('studentAssessment.csv')# поможет интегрировать ass в общую таблицу данных
info = pd.read_csv('studentInfo.csv')  #+
reg = pd.read_csv('studentRegistration.csv') #+

#Чтобы потом не путаться спрячем id-шники в тип данных "объект"
reg['id_student'] = reg['id_student'].astype(object)
info['id_student'] = info['id_student'].astype(object)
vle['id_student'] = vle['id_student'].astype(object)
vle['id_site'] = vle['id_site'].astype(object)

# Соединение таблиц в один dataframe
DF_total = pd.merge(reg, courses, on=['code_module', 'code_presentation'], how='inner')
DF_total = pd.merge(DF_total, info, on=['code_module', 'code_presentation', 'id_student'], how='inner')
DF_total = pd.merge(DF_total, results, on=['id_student'], how='inner')
DF_total = pd.merge(DF_total, ass, on=['id_assessment', 'code_module', 'code_presentation'], how='left')

# Выкинем за ненадобностью
DF_total.drop(columns = ['id_student'], inplace = True) 

# Удалим те объекты у которых количество очков больше 300
 #Из графика обнаружено, что эти персоны статистически незначимы
question_dist = DF_total[DF_total.studied_credits > 300]
DF_total = DF_total.drop(question_dist.index)

# анализ гистограмм и статистическая незначимость
question_dist = DF_total[ (DF_total.num_of_prev_attempts > 4)]
DF_total = DF_total.drop(question_dist.index)

# Выкинем те объекты, у которых дата регистрации меньше -230 и больше 30
question_dist = DF_total[(DF_total.date_registration < -230)]
DF_total = DF_total.drop(question_dist.index)
question_dist = DF_total[(DF_total.date_registration > 30)]
DF_total = DF_total.drop(question_dist.index)

# Выкинем данные по дате больше 200
question_dist = DF_total[(DF_total.date > 200)]
DF_total = DF_total.drop(question_dist.index)

DF_total = DF_total.reset_index(drop=True)

DF_total.to_csv('prepared_data.csv', index = True)