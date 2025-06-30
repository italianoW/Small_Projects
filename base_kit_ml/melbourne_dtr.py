##italianow

#Yes, i have learned this through the kaggle basic tutorial, i'll put another file in this folder just to test my actual knowledge after this

import pandas as pd
import kagglehub
import os
from sklearn.tree import DecisionTreeRegressor

path = kagglehub.dataset_download("dansbecker/melbourne-housing-snapshot")
melbourne_data = pd.read_csv(os.path.join(path, 'melb_data.csv')) 

print(melbourne_data.describe())

melbourne_data = melbourne_data.dropna(axis=0) #
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

y = melbourne_data.Price
x = melbourne_data[melbourne_features]

print(x.describe())

melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head,"\n",y.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))

##italianow
