# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a sample weather dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Temperature': [30, 32, 31, 29, 28, 27, 26, 30, 31, 33],
    'Humidity': [70, 65, 75, 80, 85, 90, 88, 70, 72, 68],
    'Rainfall': [5, 0, 10, 0, 15, 20, 25, 0, 0, 5]
}

# Convert to DataFrame
weather_data = pd.DataFrame(data)

# Step 2: Display basic information about the dataset
print("Basic Information:\n", weather_data.info())
print("\nDataset Preview:\n", weather_data.head())

# Step 3: Analyze summary statistics
print("\nSummary Statistics:\n", weather_data.describe())

# Step 4: Visualize temperature trends over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=weather_data, x='Date', y='Temperature', marker='o', label='Temperature')
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# Step 5: Compare humidity and rainfall
plt.figure(figsize=(10, 6))
sns.barplot(data=weather_data, x='Date', y='Humidity', color='skyblue', label='Humidity')
sns.lineplot(data=weather_data, x='Date', y='Rainfall', marker='o', color='orange', label='Rainfall')
plt.title('Humidity and Rainfall Comparison')
plt.xlabel('Date')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# Step 6: Identify days with high rainfall
high_rainfall_days = weather_data[weather_data['Rainfall'] > 10]
print("\nDays with High Rainfall (>10 mm):\n", high_rainfall_days)
