### **OVERVIEW**

The Loan Prediction System is designed to help bank employees assess customer eligibility for loans based on various personal and financial attributes. The model uses machine learning techniques to predict whether a customer is likely to default on a loan, based on input data such as employment history, income, credit history, and other factors.

### **FEATURES**
- Prediction of loan eligibility based on key inputs such as:
  - Gender
  - Marital status
  - Employment status
  - Income and co-applicant income
  - Loan amount and loan term
  - Credit history
  - Property area
- User-friendly interface to input customer data and receive predictions.
- Built using a random forest classifier (`rf_best`), optimized for high prediction accuracy.

### **DATASET**
The model is trained using a publicly available dataset of historical loan applications on kaggle, which includes both approved and denied loans along with customer attributes. The dataset is preprocessed to handle missing values, outliers, and categorical data before feeding it into the model.

**Dataset columns**:
- Loan_ID: Unique identifier for each loan application.
- Gender: Male or Female.
- Married: Yes or No.
- Dependents: Number of dependents.
- Education: Graduate or Not Graduate.
- Self_Employed: Yes or No.
- ApplicantIncome: Monthly income of the applicant.
- CoapplicantIncome: Monthly income of the co-applicant.
- LoanAmount: Loan amount in dollars.
- Loan_Amount_Term: Loan repayment term in months.
- Credit_History: 1 if the customer has a good credit history, 0 otherwise.
- Property_Area: Urban, Semiurban, or Rural.
- Loan_Status: Whether the loan was approved (Y) or not (N).

### **TECHNOLOGIES USED**
- **Programming Languages**: Python
- **Machine Learning Libraries**: scikit-learn, pandas, NumPy, TensorFlow
- **Framework**: Flask for creating the web-based prediction system
- **Frontend**: HTML, CSS
- **Backend**: Flask, integrated with the machine learning model
- **Version Control**: Git, GitHub
- **Deployment**: Flask app hosted locally

### **SETUP INSTRUCTIONS**
1. **Clone the repository**:
    git clone https://github.com/Vee2002/loan-prediction-system.git
   
3. **Navigate to the project directory**:
   cd loan-prediction
   
5. **Create a virtual environment** (optional but recommended):
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'

   For Anaconda:
   conda create --name env-name
   conda activate env-name   
   
7. **Install the required dependencies**:
   pip install -r requirements.txt
   
9. **Run the Flask application**:
   python app.py
   
11. **Access the application** by opening your browser and navigating to `http://localhost:5000`.

### **USAGE**
1. Open the application in a web browser.
2. Input the required customer details in the provided form.
3. Submit the form to receive a prediction of loan eligibility.
4. The model will display "Eligible" or "Not Eligible" based on the provided inputs.

### **MODEL TRAINING**
- The model was trained using the RandomForestClassifier from scikit-learn, with hyperparameter tuning done using grid search..

### **FUTURE IMPROVEMENTS**
- Improve model accuracy by exploring advanced models such as gradient boosting or XGBoost.
- Integrate more customer features, like repayment history or debt-to-income ratio, for better prediction results.
- Expand deployment to cloud platforms for scalability.
- Add more detailed error handling and logging features.
