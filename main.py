import pandas as pd
import numpy as np
from sklearn.utils import resample

# Load the dataset
file_path = r'C:\Users\nemes\PycharmProjects\pythonProject\AXISBANK.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Display basic information about the dataset
print(data.info())


# Example feature engineering
def add_features(data):
    # Calculate moving averages
    data['MA_5'] = data['Close'].rolling(window=5).mean()
    data['MA_10'] = data['Close'].rolling(window=10).mean()

    # Calculate price changes
    data['Price_Change'] = data['Close'].pct_change()

    # Calculate volatility
    data['Volatility'] = data['Close'].rolling(window=5).std()

    return data


# Add new features to the dataset
data = add_features(data)

# Drop rows with NaN values generated by rolling calculations
data = data.dropna()

print(data.head())

# Number of new data points to generate
n_new_samples = 5037

# Create synthetic data points by bootstrapping
augmented_data = resample(data, replace=True, n_samples=n_new_samples, random_state=42)

# Combine the original data with the augmented data
combined_data = pd.concat([data, augmented_data])

# Shuffle the combined dataset
combined_data = combined_data.sample(frac=1).reset_index(drop=True)

# Print information about the combined dataset
print(combined_data.info())

# Save the combined dataset to a new CSV file
output_file_path = r'C:\Users\nemes\PycharmProjects\pythonProject\AXISBANK_augmentedded.csv'
combined_data.to_csv(output_file_path, index=False)
print(f"Augmented dataset saved to {output_file_path}")
