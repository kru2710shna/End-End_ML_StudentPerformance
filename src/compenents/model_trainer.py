import os 
import sys
from dataclasses import dataclass 
#from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.execption import CustomException
from src.logger import logging
from src.util import save_object
from src.util import evaluate_models
@dataclass
class Model_Trainer_Config:
    trained_model_file_path = os.path.join("artifacts" , "model.pkl")
    
class Model_Trainer:
    def __init__(self) -> None:
        self.mode_trainer_config = Model_Trainer_Config()
        
    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("Spliting training and testing data")
            
            x_train,y_train,x_test,y_test = (
                
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:, :-1],
                test_arr[: ,-1]
            )
            
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Forest" : DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "K Neighbors Regressor": KNeighborsRegressor(),
                "XGB Regressor" : XGBRegressor(),
                #"Cat Boost Regressor" : CatBoostRegressor(),
                "AdaBoostClassifier": AdaBoostClassifier(),
            }
            
            model_report: dict = evaluate_models(X_train = x_train, 
                                                y_train = y_train, 
                                                X_test = x_test,
                                                y_test= y_test,
                                                models = models
                                                )
            
            best_model_score= max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("Best model found on both training and testing dataste")
            
            save_object(
                
                file_path=self.mode_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted=best_model.predict(x_test)
            
            r2_square = r2_score(y_test, predicted)
            return r2_square
        
        except Exception as e:
            raise CustomException(e, sys)
