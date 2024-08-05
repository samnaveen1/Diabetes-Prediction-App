from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        df = pd.read_csv(file)
        selected_features = request.form.get('selectedFeatures').split(',')
        prediction = loaded_model.predict(df[selected_features])
        result = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
        return jsonify({'prediction': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
