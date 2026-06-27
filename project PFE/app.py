import pandas as pd
from flask import Flask, render_template, request, send_file
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
import webbrowser
import os

app = Flask(__name__)

def preprocess_new_data(df, label_encoders, scaler):
    for col, le in label_encoders.items():
        if col in df.columns:
            df[col] = le.transform(df[col].astype(str))
    
    # Scale only the columns the scaler was trained on
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    
    # Ensure columns are in the exact order the model expects
    expected_cols = ['SeniorCitizen', 'Dependents', 'tenure', 'OnlineSecurity', 'OnlineBackup', 
                     'DeviceProtection', 'TechSupport', 'Contract', 'MonthlyCharges', 'TotalCharges']
    return df[expected_cols]

with open('models/label_encoders_and_scaler.pkl', 'rb') as f:
    label_encoders, scaler = pickle.load(f)
model = pickle.load(open('models/random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    try:
        df_examples = pd.read_csv('data/data-predect.csv').head(15)
        examples = df_examples.to_dict(orient='records')
    except Exception as e:
        print(f"Error loading examples: {e}")
        examples = []
    return render_template('home.html', examples=examples)

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    global model
    try:
        df_examples = pd.read_csv('data/data-predect.csv').head(15)
        examples = df_examples.to_dict(orient='records')
    except:
        examples = []

    if 'file_csv' in request.files and request.files['file_csv'].filename != '':
        try:
            file_csv = pd.read_csv(request.files['file_csv'])
            if len(file_csv) > 200:
                file_csv = file_csv.head(200)
            colonnes_a_garder = ['SeniorCitizen', 'Dependents', 'tenure', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'Contract', 'MonthlyCharges', 'TotalCharges']
            file_csv = file_csv[colonnes_a_garder]
            df = file_csv.copy()
            cust_transformed = preprocess_new_data(file_csv, label_encoders, scaler)
            predictions = model.predict(cust_transformed)
            df['Churn Prediction'] = ['Not Churn' if pred == 0 else 'Churn' for pred in predictions]
            df.to_csv('predicted_data.csv', index=False)
            table_html = df.to_html(classes='table table-bordered table-hover', index=False)
            return render_template('home.html', table=table_html, examples=examples, download_available=True)
        except Exception as e:
            table_html = f"<h1><em style='color:red'>Error:</em> {str(e)}</h1>"
            return render_template('home.html', table=table_html, examples=examples)
    else:
        try:
            contract = request.form['contract']
            onlinesecurity = request.form['onlinesecurity']
            techsupport = request.form['techsupport']
            onlinebackup = request.form['onlinebackup']
            tenure = float(request.form['tenure'])
            monthlycharges = float(request.form['monthlycharges'])
            totalcharges = float(request.form['totalcharges'])
            seniorcitizen = request.form['SeniorCitizen']
            dependents = request.form['Dependents']
            deviceprotection = request.form['DeviceProtection']
            cust = {
                'SeniorCitizen': [seniorcitizen],
                'Dependents': [dependents],
                'tenure': [tenure],
                'OnlineSecurity': [onlinesecurity],
                'OnlineBackup': [onlinebackup],
                'DeviceProtection': [deviceprotection],
                'TechSupport': [techsupport],
                'Contract': [contract],
                'MonthlyCharges': [monthlycharges],
                'TotalCharges': [totalcharges]
            }
            input_data = pd.DataFrame(cust)
            cust_transformed = preprocess_new_data(input_data, label_encoders, scaler)
            prediction = model.predict(cust_transformed)[0]
        except Exception as e: 
            prediction = f"<h1><em style='color:red'>Error:</em> {str(e)}</h1>"
        return render_template('home.html', prediction=prediction, examples=examples)

@app.route('/download')
def download():
    path = "predicted_data.csv"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
