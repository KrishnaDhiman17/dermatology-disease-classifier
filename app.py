from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('classification_model.pkl')  # Load the classifier model

# Mapping from class number to disease name
disease_classes = {
    1: "Psoriasis",
    2: "Seborrheic dermatitis",
    3: "Lichen planus",
    4: "Pityriasis rosea",
    5: "Chronic dermatitis",
    6: "Pityriasis rubra pilaris"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_features = np.array(data).reshape(1, -1)
    prediction = model.predict(final_features)[0]
    
    disease_name = disease_classes.get(int(prediction), "Unknown Disease")
    
    return render_template('index.html', prediction_text=f'Predicted Disease Class: {int(prediction)} ({disease_name})')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
