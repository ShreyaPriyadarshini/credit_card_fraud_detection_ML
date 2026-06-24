# Project Description
This project uses machine learning models to predict fraud transactions from a set of genuine transactions. Several models from baseline to ensemble were used and the best model for the task is found.
# Dataset
The dataset contains anonymized credit card transactions with the following features:
-> Time
-> Amount
-> V1 to V28 (PCA-transformed features)
-> Class (Target Variable)
-- 0 = Genuine Transaction
-- 1 = Fraudulent Transaction
Dataset source: Kaggle Credit Card Fraud Detection Dataset
# Project Workflow
1. Data loading and exploration
2. Data preprocessing
3. Exploratory data analysis
4. Train test split
5. Imbalance data management
6. Training models on sample dataset
7. Model evaluation and best model selection
8. Training model on complete balanced dataset
9. Evaluating all metrics
10. Streamlit deployment
# Machine learning models used:
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost
# Best model:
RandomForestClassifier
# Results:
Accuracy score is : 0.9970218165157015
Precision score is : 0.32599118942731276
Recall score is : 0.8222222222222222
F1 score is : 0.4668769716088328
Roc auc curve score is : 0.9676103737174055
# Streamlit Application
The Streamlit application allows users to upload transaction data in CSV format and predicts fraudulent transactions.
# Technologies Used
1. Python
2. Pandas
3. NumPy
4. Scikit-Learn
5. Imbalanced-Learn (SMOTE)
6. XGBoost
7. Matplotlib
8. Seaborn
9. Streamlit
# Future Improvements:
1. Hyperparameter Tuning
2. Cross validation
