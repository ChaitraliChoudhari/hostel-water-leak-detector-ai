import pandas as pd

# Load data
data = pd.read_csv("data/sample_water_usage.csv")

# Calculate average usage
average_usage = data['water_usage_liters'].mean()

# Detect anomaly
data['anomaly'] = data['water_usage_liters'] > (2 * average_usage)

print(data)
