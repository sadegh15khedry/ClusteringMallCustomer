# Mall Customer Segmentation

This project aims to segment mall customers based on their demographic and spending behavior. The dataset used for this analysis is available in the `Mall_Customers.csv` file.

## Requirements

Make sure you have the following Python packages installed:

- pandas
- matplotlib
- scikit-learn

You can install these packages using pip:

pip install pandas matplotlib scikit-learn

## Usage

1. Clone the repository:
```bash
git clone https://github.com/sadegh15khedry/ClusteringMallCustomer.git
```
2. Navigate to the project directory:
```bash
cd ClusteringMallCustomer
```
3. Run the Python script:
```bash
python mall_customer_segmentation.py
```
## Description

- `mall_customer_segmentation.py`: This script performs customer segmentation using K-means clustering algorithm. It preprocesses the data, finds the optimal number of clusters using the elbow method, applies K-means clustering, and visualizes the clusters.

## Dataset

The dataset contains the following columns:

- `CustomerID`: Unique identifier for each customer.
- `Genre`: Gender of the customer (0 for Female, 1 for Male).
- `Age`: Age of the customer.
- `Annual Income (k$)`: Annual income of the customer in thousands of dollars.
- `Spending Score (1-100)`: Spending score assigned to the customer based on their spending behavior.

## Methodology

1. **Data Preprocessing**:
   - Missing values are handled, if any.
   - Categorical encoding is performed for the 'Genre' column.

2. **Normalization**:
   - The data is normalized using the z-score method.

3. **Finding Optimal K**:
   - The elbow method is used to find the optimal number of clusters (k).
![Screenshot 2024-06-11 183628](https://github.com/sadegh15khedry/ClusteringMallCustomer/assets/90490848/d19d56b6-5073-41a3-82ff-44db6da31a54)


4. **Clustering**:
   - K-means clustering algorithm is applied with the optimal k value.

5. **Visualization**:
   - The clusters are visualized using a scatter plot with 'Age' and 'Annual Income' as axes. Each cluster is represented by a different color.
![Screenshot 2024-06-11 183636](https://github.com/sadegh15khedry/ClusteringMallCustomer/assets/90490848/834eed63-a91d-4da2-b6ae-c42ead54cc9b)


## Results

The scatter plot shows distinct clusters of mall customers based on their age and annual income. Each cluster represents a different segment of customers.

## License

This project is licensed under the Apache-2.0 License - see the LICENSE file for details.
