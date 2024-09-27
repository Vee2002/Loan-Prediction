
import joblib
from sklearn.metrics import precision_score

# Loading the variables and the model
X_train_encoded = joblib.load('X_train_encoded.pkl')
X_test_encoded = joblib.load('X_test_encoded.pkl')
y_train = joblib.load('y_train.pkl')
y_test = joblib.load('y_test.pkl')
rf_best = joblib.load('rf_best.pkl')

# Making predictions
prediction = rf_best.predict(X_test_encoded)

# print(f"Precision Score: ", round(precision_score(y_test,prediction)*100,2))
