import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_excel('cotton.xlsx')

dataset=dataset[['Variety','Year','Yr Average']]


X = dataset.iloc[:, :2]

#Converting words to integer values

y = dataset.iloc[:, -1]

#Splittmodel.predict([3,2021])ing Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,2026]]))
