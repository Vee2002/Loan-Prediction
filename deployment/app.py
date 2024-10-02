from flask import Flask, request, render_template
from model import rf_best
import numpy as np
import os

app = Flask(__name__,template_folder=os.path.join(os.path.pardir,'templates'))

# Creating the routes
@app.route('/predict',methods=['POST'])
def predict():
    try:
        # Extracting form data

        dependents = int(request.form['Dependents'])
        applicant_income = float(request.form['ApplicantIncome'])
        coapplicant_income = float(request.form['CoapplicantIncome'])
        loan_amount = float(request.form['LoanAmount'])
        loan_amount_term = int(request.form['Loan_Amount_Term'])
        credit_history = int(request.form['Credit_History'])
        gender = int(request.form['Gender'])
        married_status = int(request.form['Married'])
        area_semiurban = int(request.form['Property_Area_Semiurban'])
        area_urban = int(request.form['Property_Area_Urban'])
        education = int(request.form['Education'])        
        self_employed = int(request.form['Self_Employed'])

        # Creating an input array for prediction
        input_array = np.array([[dependents,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,gender,married_status,area_semiurban,area_urban,education,self_employed]])

        # Making prediction using the model
        prediction = rf_best.predict(input_array)

        # Return a statement based on the value of the prediction
        if prediction == 0:
            result_message = "This customer is unfortunately not eligible for a loan based on the information provided"
        else:
            result_message = "The customer is eligible for a loan based on the information provided"

        # Return predicition
        # print(f"The prediction is: {prediction[0]}")

    except Exception as e:
        return str(e)
     
    # Returning the function/Passing the form data to the template
    return render_template('predict.html',prediction=result_message)

@app.route('/')
def home():
    return render_template('predict.html')
    

if __name__ == "__main__":
    app.run(debug=True)






