# -*- coding: utf-8 -*-
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import os
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import csv


dataset = read_csv(os.path.abspath("viborka1.csv"),',')
# print(dataset.head())

# print(dataset.corr())

trg = dataset[['V']]
trn = dataset.drop(['V'], axis=1)

models = [
			LinearRegression(), # метод наименьших квадратов
			RandomForestRegressor(n_estimators=100, max_features ='sqrt'), # случайный лес
			KNeighborsRegressor(n_neighbors=6), # метод ближайших соседей
			SVR(kernel='linear'), # метод опорных векторов с линейным ядром
			LogisticRegression() # логистическая регрессия
		]

Xtrn, Xtest, Ytrn, Ytest = train_test_split(trn, trg, test_size=0.2)


#создаем временные структуры
TestModels = DataFrame()
tmp = {}
korrs = []
#для каждой модели из списка
for model in models:
    #получаем имя модели
    m = str(model)
    tmp['Model'] = m[:m.index('(')]    
    #обучаем модель
    model.fit(Xtrn, Ytrn.values.ravel())
    # korrs.append(model.feature_importances_)
    #вычисляем коэффициент детерминации
    tmp['R2_Y%s'%str(1)] = r2_score(Ytest, model.predict(Xtest))
    #записываем данные и итоговый DataFrame
    TestModels = TestModels.append([tmp])
#делаем индекс по названию модели
TestModels.set_index('Model', inplace=True)

fig, axes = plt.subplots(ncols=2, figsize=(10,4))
TestModels.R2_Y1.plot(ax=axes[0], kind='bar', title='R2_Y1')
# TestModels.R2_Y2.plot(ax=axes[1], kind='bar', color='green', title='R2_Y2')
print(TestModels)
# TestModels.show()

model = models[0]
model.fit(Xtrn, Ytrn)
korrs.append(model.coef_[0])
print(model.intercept_[0])
# print("\n")
# print(model.coef_[0])
# print(trn['X60'][0])
# print(trg[0])

# for i, col in enumerate(dataset.values):
# 	print(i)
# 	print(col)
# 	print("dseeeeee")

# print(dataset.values[0][:len(dataset.values[0])-1])
for i, col in enumerate(dataset.values):
	s = 0.0
	for k, x in zip(model.coef_[0], dataset.values[i][:len(dataset.values[i])-1]):
		s += k * x
	# s -= len(dataset.values[i])//2
	s += model.intercept_[0]
	print(s)
	print( dataset.values[i][len(dataset.values[i])-1] )
	print("\n")

model = models[1]
model.fit(Xtrn, Ytrn.values.ravel())
korrs.append(model.feature_importances_)

with open('korr.csv', 'wb') as myfile:
    out = csv.writer(myfile, delimiter=',',quoting=csv.QUOTE_ALL)
    for korr in korrs:
        out.writerow(korr)