import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Connect to the Illinois iQuery Database
conn = sqlite3.connect('iquery.sqlite')

# Collect the data on diabetes from people in Chicago
df = pd.read_sql('SELECT * FROM diabetes WHERE city = "Chicago"', conn)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(df.drop('diabetes', 1), df['diabetes'], test_size=0.25)

# Train a machine learning model on the training set
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate the machine learning model on the test set
y_pred = clf.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))

# Use the machine learning model to predict the risk of diabetes for people in Chicago
new_data = {'age': 30, 'weight': 150, 'blood_pressure': 120, 'glucose_level': 100}
y_pred = clf.predict([new_data])
print('Risk of diabetes:', y_pred)
