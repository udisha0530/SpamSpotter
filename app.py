from flask import Flask, render_template, request, jsonify
from scripts.preprocessing_script import process_raw_strings
import joblib

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

app = Flask(__name__)

# Load the SVM model
svm_model = joblib.load('models/SVM Classifier_model.pkl')

# Load the preprocessing pipeline
preprocessing_pipeline = joblib.load('models/preprocessing_pipeline.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        message = request.form['message']
        # Preprocess the input message
        processed_message = preprocessing_pipeline.transform([message])

        # Use model for prediction
        prediction = svm_model.predict(processed_message)[0]

        return render_template('index.html', prediction=prediction, message=message)

    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)