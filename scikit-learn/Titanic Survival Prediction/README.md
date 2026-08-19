# Titanic Survival Prediction

A Machine Learning classification project that predicts whether a passenger survived the Titanic disaster using multiple classification algorithms.

## Overview

This project demonstrates a complete Machine Learning workflow for a binary classification problem using the Titanic dataset.

The main goal is to understand how different classification algorithms perform on the same dataset and identify the best-performing model based on multiple evaluation metrics.

## Objective

- Understand the Titanic dataset
- Perform data cleaning and preprocessing
- Handle missing values
- Perform Exploratory Data Analysis (EDA)
- Perform feature engineering
- Encode categorical features
- Split the dataset into training and testing sets
- Apply feature scaling
- Train multiple classification models
- Evaluate model performance
- Compare different classification algorithms
- Identify the best-performing model

## Dataset

The Titanic dataset contains information about passengers and their survival status.

### Features

- Pclass — Passenger class
- Sex — Passenger gender
- Age — Passenger age
- SibSp — Number of siblings/spouses aboard
- Parch — Number of parents/children aboard
- Fare — Passenger fare
- Embarked — Port of embarkation
- Alone — Whether the passenger was travelling alone

### Target

Survived

- 0 — Did not survive
- 1 — Survived

## Machine Learning Workflow

Data Loading
→ Data Understanding
→ Data Cleaning
→ Exploratory Data Analysis
→ Feature Engineering
→ Encoding
→ Train-Test Split
→ Feature Scaling
→ Model Training
→ Prediction
→ Model Evaluation
→ Model Comparison

## Data Preprocessing

The following preprocessing techniques were applied:

- Removed unnecessary columns
- Checked dataset information and data types
- Identified missing values
- Filled missing Age values using the mean
- Removed rows with missing Embarked values
- Applied Label Encoding to binary categorical features
- Applied One-Hot Encoding to multi-class categorical features
- Converted boolean features into numerical values
- Separated features and target variable
- Split data into training and testing sets
- Applied StandardScaler for feature scaling

## Exploratory Data Analysis

The dataset was explored using statistical analysis and visualizations to understand:

- Survival distribution
- Survival based on gender
- Survival based on passenger class
- Age distribution
- Fare distribution
- Relationships between different features and survival

## Classification Models

The following Machine Learning classification algorithms were implemented:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Gaussian Naive Bayes
4. Decision Tree
5. Support Vector Machine (SVM)

## Model Evaluation

Each model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

These metrics were used to compare the performance of the different classification algorithms.

## Model Comparison

| Model | Accuracy | F1-Score (Survived) |
|---|---:|---:|
| Logistic Regression | 79.78% | 0.75 |
| KNN (k=19) | 81.46% | 0.76 |
| Gaussian Naive Bayes | 79.78% | 0.75 |
| Decision Tree | 75.28% | 0.70 |
| SVM (RBF) | 81.46% | 0.76 |

## Best Performing Models

KNN and SVM achieved the highest test accuracy of 81.46% on the current train-test split.

Both models produced the same classification performance on the test dataset.

KNN was implemented with k = 19, while SVM used the RBF kernel.

The results are based on the current train-test split and do not necessarily indicate that these models will perform best on every split or dataset.

## Conclusion

This project provided practical experience with multiple supervised classification algorithms and the complete Machine Learning workflow.

Among the tested models, KNN and SVM achieved the best performance on the current test dataset with an accuracy of 81.46%.

The project also demonstrated that model performance should not be judged using accuracy alone. Precision, recall, F1-score, and the confusion matrix provide additional insight into classification performance.

## Key Learnings

Through this project, I strengthened my understanding of:

- Binary Classification
- Logistic Regression
- K-Nearest Neighbors
- Naive Bayes
- Decision Trees
- Support Vector Machines
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Train-Test Split
- Model Training
- Model Prediction
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report
- Model Comparison

## Future Improvements

- Apply Cross-Validation
- Perform Hyperparameter Tuning
- Improve Feature Engineering
- Compare additional classification algorithms
- Implement Ensemble Learning
- Try Random Forest and Gradient Boosting
- Optimize the best-performing models
- Deploy the final model

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Structure

Titanic-Survival-Prediction/
│
├── main.ipynb
├── README.md
└── dataset/
    └── Titanic-Dataset.csv

## Author

Rahul Mondal

B.Tech CSE (AIML)