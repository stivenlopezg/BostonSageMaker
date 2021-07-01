import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class RegressionEvaluator:
    def __init__(self, observed: pd.Series or list, predicted: pd.Series or list):
        self.observed = observed
        self.predicted = predicted
        self.metrics = None

    def calculate_metrics(self):
        self.metrics = {
            "mae": round(mean_absolute_error(y_true=self.observed, y_pred=self.predicted), 2),
            "mse": round(mean_squared_error(y_true=self.observed, y_pred=self.predicted), 2),
            "r2": round(r2_score(y_true=self.observed, y_pred=self.predicted), 2)
        }
        return self

    def print_metrics(self):
        print(f"El MAE es: {self.metrics['mae']}")
        print(f"El MSE es: {self.metrics['mse']}")
        print(f"El RMSE es: {round(np.sqrt(self.metrics['mse']), 2)}")
        print(f"El R2 es: {self.metrics['r2']}")
