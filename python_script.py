# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Attendance_Rate, Weekly_Study_Hours, JAMB_Score)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Define features and target
X = dataset[['Weekly_Study_Hours', 'Attendance_Rate']]  
y = dataset['JAMB_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.20,
                                                    random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


# Get the feature names
feature_names = X_train.columns

# Combine names and coefficients
coef_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model.coef_
})
print(coef_df)

intercept = model.intercept_
print(f"Intercept: {intercept}")

# Predict on test set
y_pred = model.predict(X_test)

# Create output DataFrame with predictions and actual values
test_results = X_test.copy()
test_results['Actual_Score'] = y_test
test_results['Predicted_Score'] = y_pred

# Scatter plot: Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(test_results['Actual_Score'], test_results['Predicted_Score'], alpha=0.7, color='teal')
plt.plot([test_results['Actual_Score'].min(), test_results['Actual_Score'].max()],
         [test_results['Actual_Score'].min(), test_results['Actual_Score'].max()],
         'r--', linewidth=2)  # reference line y = x

plt.xlabel('Actual Score')
plt.ylabel('Predicted Score')
plt.title('Predicted vs Actual Score')
plt.grid(True)
plt.tight_layout()
plt.show()
