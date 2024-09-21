# End-to-End Machine Learning Project: Understanding Student Performance

## Problem Statement
This project aims to analyze and understand how various factors such as **Gender**, **Ethnicity**, **Parental Level of Education**, **Lunch**, and **Test Preparation Course** affect students' academic performance based on their test scores. By building a predictive model, we can determine the impact of these factors on students’ overall performance.

## Data Collection
- **Dataset Source**: Kaggle - [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Dataset Features**: 
  - Gender
  - Ethnicity
  - Parental Level of Education
  - Lunch (standard/reduced)
  - Test Preparation Course (completed/not completed)
  - Math Score, Reading Score, Writing Score

## Project Setup
- **setup.py**: Manages project configuration and ensures a structured setup.
- **requirements.txt**: Defines and manages all package dependencies, including:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `Flask`
  - `gunicorn`
- **.gitignore**: Excludes unnecessary files such as virtual environments, dataset files, and logs from version control.
- **Logging**: Utilizes Python’s `logging` module for detailed logging and error tracking throughout the project.
- **Exception Handling**: Follows Python's `sys` execution model to implement custom error handling, ensuring the application fails gracefully.

## Notebook Setup
The project includes a **notebook** folder with the following key Jupyter Lab notebooks:
- `dataset.csv`: The raw dataset for analysis.
- **Exploratory Data Analysis (EDA)**: A notebook for in-depth EDA to understand key patterns and distributions in the dataset.
- **Model Training**: A notebook for training and evaluating machine learning models.

## Data Visualization
- **Libraries**: 
  - `numpy`, `pandas`: For data manipulation.
  - `matplotlib`, `seaborn`: For visualizing relationships, trends, and distributions in data.
  
Key visualizations include:
- Distribution of students' scores based on gender, ethnicity, parental education, etc.
- Correlation heatmaps between various features and test scores.

## Model Development
- **Preprocessing**:
  - Utilizes **One-Hot Encoding** for categorical variables (e.g., Gender, Ethnicity).
  - Applies **StandardScaler** to normalize numeric features (e.g., scores).
- **Modeling**:
  - Trains a **Linear Regression** model to predict student scores based on the features.
  - **Evaluation Metrics**: 
    - **Mean Absolute Error (MAE)**
    - **Mean Squared Error (MSE)**
    - **R-squared**
  - Visualizes the predictions versus the actual scores to assess the model performance.

## Pipeline Implementation
- **Pipeline**:
  - Implements a machine learning pipeline using `scikit-learn`'s `Pipeline` module for efficient model development.
  - Assembles multiple preprocessing and training steps in the pipeline for cross-validation and experimentation.

## Web Application
- The project includes a **Flask-based web application** to make predictions accessible via a web interface.
- **app.py**: 
  - Defines the web application and API for predicting student performance.
  - Uses Flask's lightweight framework to serve HTML pages and handle prediction requests.
- **Frontend Components**:
  - `home.html`: Landing page of the application.
  - `index.html`: User interface for inputting student data and displaying predicted performance.

## Git Commands for Users

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kru2710shna/End-End_ML_StudentPerformance.git
