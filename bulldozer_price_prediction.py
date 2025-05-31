import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("bulldozer_data.csv")

# Select features and target variable
features = ['YearMade', 'MachineHoursCurrentMeter', 'UsageBand', 'ProductSize']
target = 'SalePrice'

# Drop missing values
df = df.dropna(subset=features + [target])

# Split features and target
X = df[features]
y = df[target]

# Convert categorical features to dummy variables
X = pd.get_dummies(X)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate performance
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")
