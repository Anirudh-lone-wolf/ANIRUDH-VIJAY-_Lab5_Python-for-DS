from flask import Flask, render_template, jsonify,  request
import pickle as pkl
import numpy as np

# read the pickle
sp_pred_model = pkl.load(open('selling_price_pred.pkl', 'rb'))

#initialize the flask app
app = Flask(__name__)

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        # Get form data
        Age_of_the_car = int(request.form['Age_of_the_car'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type = int(request.form['Fuel_Type'])
        Seller_Type = int(request.form['Seller_Type'])
        Transmission = int(request.form['Transmission'])
    
    # Make prediction
    prediction = sp_pred_model.predict([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, Age_of_the_car]])
    
    # Display prediction on index.html
    return render_template('index.html', prediction_text='Predicted Selling Price: {:.2f} lakhs'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)