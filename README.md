
```markdown
# 🧠 Dermatology Disease Classifier

This project uses machine learning to predict the **class of dermatological disease** based on 33 clinical and histopathological features from a dataset. It includes a trained model and a Flask web app for live predictions.

🌐 **Live Demo** (Render):  
➡️ [https://dermatology-disease-classifier.onrender.com](https://dermatology-disease-classifier.onrender.com) *(when deployed)*

---

## 📊 Dataset Overview

- **Source**: UCI Dermatology Dataset  
- **Features (33 total)**: Includes inputs such as `erythema`, `scaling`, `itching`, `acanthosis`, etc.  
- **Target column**: `class` (values: 1–6)
  - `1`: Psoriasis  
  - `2`: Seborrheic dermatitis  
  - `3`: Lichen planus  
  - `4`: Pityriasis rosea  
  - `5`: Chronic dermatitis  
  - `6`: Pityriasis rubra pilaris

---

## 🚀 Project Structure

```

├── app.py                       # Flask backend app
├── train\_rf\_model.py           # Model training script (Random Forest Classifier)
├── classification\_model.pkl    # Trained model file (serialized)
├── CO22340\_dermatology\_database\_1.csv   # Dataset used for training
├── templates/
│   └── index.html              # Web form frontend for user input
├── requirements.txt            # Python dependencies (optional)
└── README.md                   # Project overview and usage

````

---

## ⚙️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/KrishnaDhiman17/dermatology-disease-classifier.git
cd dermatology-disease-classifier
````

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
```

### 3. Install required libraries

```bash
pip install flask scikit-learn pandas joblib numpy
```

### 4. Train the model (if needed)

```bash
python train_rf_model.py
```

### 5. Start the Flask app

```bash
python app.py
```

Then open your browser at:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌐 How to Deploy on Render

1. Push this repo to GitHub.
2. Go to [https://render.com](https://render.com)
3. Create a **New Web Service**.
4. Use:

   * **Build command**: `pip install flask scikit-learn pandas joblib`
   * **Start command**: `python app.py`
5. Make sure `app.py` uses:

   ```python
   app.run(host='0.0.0.0', port=10000)
   ```

---

## ✅ Features

* 33 dynamic input fields in a responsive HTML form
* Predicts and displays disease class (number and name)
* Real-time inference using trained ML model
* Render-hosted Flask app

---

## ✨ Example Prediction

> **Predicted Disease Class: 3 (Lichen planus)**
> Based on input features provided by the user.

---

## 🙋‍♂️ Author

**Krishna Dhiman**
🔗 [GitHub Profile](https://github.com/KrishnaDhiman17)

---
