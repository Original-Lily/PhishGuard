import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the preprocessed data with TF-IDF matrix
input_file_path = 'preprocessed_data_with_tfidf.csv'
df = pd.read_csv(input_file_path)

#############################################################################################################

# Extract TF-IDF matrix and labels
X = df.drop('Email Type', axis=1)  # Assuming 'Email Type' is the column with labels
y = df['Email Type']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

#############################################################################################################

#MAKE PREDICTIONS FOR FINAL ROWS
new_data_for_prediction = df.iloc[-1, :-1].values.reshape(1, -1)  #EXCLUDE label column
final_row_prediction = model.predict(new_data_for_prediction)

#############################################################################################################

#Output the prediction for the final row
print(f"Prediction for the final row: {final_row_prediction[0]}")
df.at[df.index[-1], 'Email Type'] = final_row_prediction[0]

#EVALUATE MODEL
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
