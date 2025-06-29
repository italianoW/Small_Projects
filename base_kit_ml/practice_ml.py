##italianow

import pandas as pd
import kagglehub
import os
from sklearn.tree import DecisionTreeRegressor

path = kagglehub.dataset_download("bismasajjad/global-ai-job-market-and-salary-trends-2025")

print(os.listdir(path))

skill_data = pd.read_csv(os.path.join(path, 'ai_job_dataset.csv')) 

print(skill_data.columns) 
print(skill_data.describe()) #naturally doesn't show aplhabetic values unless include='all'

skill_data = skill_data.dropna(axis=0) #drops rows(axis = 0, if it was 1 it would be the column) who have missing data. 
x_values = ['years_experience', 'job_description_length','benefits_score']

y = skill_data.salary_usd
x = skill_data[x_values]

print(x.describe(include='all'))
print(x.head())

melbourne_model = DecisionTreeRegressor(random_state=1) #uses numeric values in a greedy way to predict through a 
                                                        #tree, separating state areas used to predict future values.
melbourne_model.fit(x, y)

print("Making predictions for the head:")
print(x.head,"\n",y.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))

##italianow
