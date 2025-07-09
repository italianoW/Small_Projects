##italianow

import pandas as pd
import kagglehub
import os
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


path = kagglehub.dataset_download("bismasajjad/global-ai-job-market-and-salary-trends-2025")

print(os.listdir(path))

skill_data = pd.read_csv(os.path.join(path, 'ai_job_dataset.csv'))

skill_data = skill_data.dropna(axis=0) #drops rows(axis = 0, if it was 1 it  
                                        #would be the column) who have missing data.
x_values = ['years_experience', 'job_description_length','benefits_score']

y = skill_data.salary_usd
x = skill_data[x_values]

print(x.describe())

train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 0)

print(train_x.describe())
print(val_x.describe())

ml_model = DecisionTreeRegressor(max_leaf_nodes=50000,random_state=1) #uses numeric values in a greedy way to predict through a
                                                  #tree separating states areas used to predict future values.
ml_model.fit(train_x, train_y)

train_predictions = ml_model.predict(train_x)
val_predictions = ml_model.predict(val_x)

print("(based only on training):", mean_absolute_error(train_y, train_predictions))
print("(based on new values): ", mean_absolute_error(val_y, val_predictions))

##italianow
