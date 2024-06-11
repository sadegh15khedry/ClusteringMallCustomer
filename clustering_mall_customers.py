import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
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


#normalizing the data using The z-score method
# for column in df.columns:
#   df[column] = df[column] / df[column].abs().max()

# for column in df.columns: 
#     df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())     

# for column in df.columns: 
#     df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())  

for column in df.columns: 
    df[column] = (df[column] -
                           df[column].mean()) / df[column].std() 


#df['Age'].plot(kind='hist')
#df['Annual Income (k$)'].plot(kind='hist')
#df['Spending Score (1-100)'].plot(kind='hist')


# finding the k useing elbow method
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df)
    inertias.append(kmeans.inertia_)


# Plot the inertia vs k
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
show()


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
      plt.scatter(subset['Age'], subset['Annual Income (k$)'], s=100, c="red")
  elif label == 1:
      plt.scatter(subset['Age'], subset['Annual Income (k$)'], s=100, c="blue")
  # elif label == 2:
  #     plt.scatter(subset['Age'], subset['Annual Income (k$)'], s=100, c="green")
  # elif label == 3:
  #     plt.scatter(subset['Age'], subset['Annual Income (k$)'], s=100, c="brown")
      

plt.title('Customer Segments')
plt.xlabel('Age')
plt.ylabel('Annual Income (k$)')
plt.legend()
plt.show()

