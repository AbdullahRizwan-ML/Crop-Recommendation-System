# 🌾 Crop Recommendation System

This is a machine learning project that predicts the best crop to grow based on environmental and soil conditions.

## 📁 Structure
- `ML/`: Contains the dataset, trained model, and label encoder
- `backend/`: FastAPI backend to serve predictions
- `frontend/`: Streamlit app for user interface

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run backend: `uvicorn backend.main:app --reload`
3. Run frontend: `streamlit run frontend/app.py`

## 🧠 Models
Trained using: Random Forest, SVM, Logistic Regression, etc.

## 🛠️ Tools
- MLflow
- FastAPI
- Streamlit
- Scikit-learn
- Pandas

