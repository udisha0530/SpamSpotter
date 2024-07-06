# Flask SVM Text Classification App

This is a Flask web application that uses a Support Vector Machine (SVM) model to classify text messages. The application preprocesses the input text and uses the trained SVM model to make predictions.

## Features

- **Input Text Classification**: Users can input text messages which are then classified using a pre-trained SVM model.
- **Preprocessing Pipeline**: The text messages are preprocessed using a custom preprocessing pipeline before classification.
- **Error Handling**: The application includes error handling to manage and display any issues during processing.

## Project Structure

project_root/
│
├── app.py
├── models/
│ ├── SVM Classifier_model.pkl
│ └── preprocessing_pipeline.pkl
├── scripts/
│ └── preprocessing_script.py
├── templates/
│ ├── index.html
│ └── error.html
├── static/
│ └── (optional static files like CSS, JS)
└── README.md
## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- joblib
- scikit-learn

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. Create and activate a virtual environment:
 ```sh 
 python -m venv venv
 source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
4.Place your SVM model and preprocessing pipeline in the models/ directory:

   models/SVM Classifier_model.pkl
   models/preprocessing_pipeline.pkl
5.Run the application:

   ```sh
   python app.py
6.Open your browser and navigate to http://127.0.0.1:5000/ to access the application.

Usage
Enter a text message in the input box on the home page and submit.
The application will classify the message and display the prediction.
