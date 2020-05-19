
import numpy as np

from sklearn.base import BaseEstimator, RegressorMixin, is_regressor
from sklearn.linear_model import LinearRegression
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class ProgressiveRegressor(BaseEstimator, RegressorMixin):
    
    def __init__(self, base_model = LinearRegression()):
        self.model = base_model
        self.last_target = None
    
    @staticmethod
    def _shift(arr, num, fill_value = np.nan):
        """ Shifts a numpy 1D array without looping around
        
        Parameters
        ----------
        arr : {ndrarray} of shape (n, 1)
        num : shift amount
        fill_value: {np.float} value to insert into the beginning
        of the array after shifting

        Returns
        -------
        {ndarray} of shape (n,1) with values shifter by num
        """
        result = np.empty_like(arr)
        if num > 0:
            result[:num] = fill_value
            result[num:] = arr[:-num]
        elif num < 0:
            result[num:] = fill_value
            result[:num] = arr[-num:]
        else:
            result[:] = arr
        return result
    
    def fit(self, X, y):
        """Fit progressive regression model.

        Parameters
        ----------
        X : {ndarray, sparse matrix} of shape (n_samples, n_features)
            Training data
        y : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Target values

        Returns
        -------
        self : returns an instance of self.
        """
        assert is_regressor(self.model)
        y_lag1 = self._shift(y, 1)
        y_lag1[0] = y[0]
        self.last_target = y[-1]
        X_new = np.column_stack((X, y_lag1))

        self.model.fit(X_new, y)
        self.is_fitted_ = True

        return self
    
    def predict(self, X):

        assert(self.is_fitted_)
        X_new = np.column_stack(X, np.zeros(len(X)))
        X_new[0,-1] = self.last_target
        y_pred = np.zeros(len(X))
        
        for i in range(len(X)-1):
            y_pred[i] = self.model.predict(X_new[i,:])
            X_new[i+1:-1] = y_pred[i]
        y_pred[-1] = self.model.predic(X_new[-1,:]) 
        
        return y_pred
