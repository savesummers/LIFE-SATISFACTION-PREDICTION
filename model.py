import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data_root = 'https://github.com/ageron/data/raw/main/'
lifesat = pd.read_csv(data_root + 'lifesat/lifesat.csv')
X = lifesat[['GDP per capita (USD)']].values
y = lifesat[['Life satisfaction']].values

lifesat.plot(kind = 'scatter', grid = True, x = 'GDP per capita (USD)', y = 'Life satisfaction')
plt.axis([23500, 62500, 4, 9])
plt.show()

model = LinearRegression()
model.fit(X,y)
x_new = [[int(input('Enter GDP per capita (USD): '))]]
print('Life Satisfaction Prediction: ', model.predict(x_new))
