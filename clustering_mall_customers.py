import pandas as pd
import matplotlib as mp
from sklearn.preprocessing import LabelEncoder


#Loading the dataset
df = pd.read_csv("Mall_Customers.csv")

#Finding and handling missing values
null_values = df.isnull()
rows_with_null_values = df[null_values.any(axis=1)]
#print(rows_with_null_values)

#Categorical Encoding for Genre column
label_encoder = LabelEncoder()
df['Genre'] = label_encoder.fit_transform(df['Genre'])
         
print(df['Genre'].unique())