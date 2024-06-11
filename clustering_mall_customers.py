import pandas as pd
import matplotlib as mp
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from matplotlib.pyplot import plot, show

#Loading the dataset
df = pd.read_csv("drive/MyDrive/Mall_Customers.csv")

#Finding and handling missing values
null_values = df.isnull()
rows_with_null_values = df[null_values.any(axis=1)]
#print(rows_with_null_values)


#Categorical Encoding for Genre column --- Male => 1 --- Female =>0
label_encoder = LabelEncoder()
df['Genre'] = label_encoder.fit_transform(df['Genre'])

#df['Age'].plot(kind='hist')
#df['Annual Income (k$)'].plot(kind='hist')
#df['Spending Score (1-100)'].plot(kind='hist')


# finding the k useing elbow method
# inertias = []
# for k in range(1, 10):
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(df)
#     inertias.append(kmeans.inertia_)
#Plot the inertia vs k
# plot(range(1, 10), inertias)
# show()


#clustering using k-means algorithm
kmeans = KMeans(n_clusters=2)
kmeans.fit(df)
label = kmeans.predict(df)
df['label'] = label
print(df)

#Visualizing the clusters
# df['label'].plot(kind='hist')
# plot(df['Age'], df['Annual Income (k$)'], df['label'], 'go')
for label in df['label']:
  subset = df[df['label'] == label]
  if (label == 0):
    plot(subset['Age'], subset['Annual Income (k$)'], 'ro', color='red')
  else:
    plot(subset['Age'], subset['Annual Income (k$)'], 'ro', color='blue')

