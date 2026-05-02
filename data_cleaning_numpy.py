import numpy as np

# Example: cleaning NaN values
data = np.array([10, np.nan, 20, 30, np.nan])
print("Original data:", data)

# Replace NaN with mean
mean_val = np.nanmean(data)
cleaned_data = np.nan_to_num(data, nan=mean_val)
print("Cleaned data:", cleaned_data)
