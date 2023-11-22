# End-to-End Machine Learning Project: Understanding Student Performance

## Problem Statement:
This project aims to analyze and understand how various factors, such as Gender, Ethnicity, Parental Level of Education, Lunch, and Test Preparation Course, affect students' academic performance based on their test scores.

## Data Collection:
- **Dataset Source:** [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
- **Setup:**
  - Utilizes Python with a structured setup using `setup.py`.
  - Manages package dependencies through `requirements.txt`.
  - Implements a `.gitignore` file to exclude certain files from version control.
- Utilizes the Python `logging` module for effective logging and error tracking.
- Implements exception and error handling using `sys` and follows Python's execution model.

## Notebook Setup:
- The project includes a `notebook` folder containing Jupyter Lab files, including:
  - The raw dataset (`dataset.csv`).
  - Exploratory Data Analysis (EDA) notebooks.
  - Model Training notebooks.

## Data Visualization:
- Utilizes libraries such as `numpy`, `pandas`, `matplotlib`, and `seaborn` for data visualization during the EDA phase.

## Model Development:
- Implements Model Training, Validation, and Preprocessing.
- Utilizes One-Hot Encoding and StandardScaler for preprocessing.
- Evaluates models using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
- The primary model used is Linear Regression.
- Visualizes predictions to gain insights into model performance.

## Pipeline Implementation:
- Implements a machine learning pipeline using `scikit-learn`'s `Pipeline` module.
- The pipeline helps assemble and cross-validate multiple steps, making it efficient for experimentation.

## Web Application:
- The project includes a Flask-based web application in `app.py`.
- Uses Flask, a lightweight WSGI web application framework, to create a web interface.
- Implements `home.html` and `index.html` as frontend components for user interaction.

*Note: The project description will be continually updated as the project progresses further.*
