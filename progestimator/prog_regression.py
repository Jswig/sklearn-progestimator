# Author: Anders Poirel
# 
# Efficient implementation of shift by 
# gzc: https://stackoverflow.com/a/42642326

import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class ProgressiveRegression(BaseEstimator, RegressorMixin):
    """Wraps an estimator to faciliate problems with time correlation in 
    the targets.  This is done by having
    - fit(X,y) append y with a lag of 1 to x. 
    - predict(X) append to each sample the prediction on the previous sample.
   
    Parameters
    ----------
    base_estimator : estimator, default=LinearRegression()
        The base scikit-learn compatible estimator used for prediction.

    Attributes
    ----------
    base_estimator_ : estimator
        The base estimator used for prediction.
    """

    def __init__(self, base_estimator = LinearRegression()):
        self.base_estimator = base_estimator
    
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
        X : {ndarray} of shape (n_samples, n_features)
            Training data
        y : ndarray of shape (n_samples,)
            Target values

        Returns
        -------
        self : return an instance of self.
        """
        X, y = check_X_y(X, y, ensure_min_features = 0)

        y_lag1 = self._shift(y, 1)
        y_lag1[0] = y[0]
        self.last_target = y[-1]
        X_new = np.column_stack((X, y_lag1))
        self.base_estimator.fit(X_new, y)

        self.is_fitted_ = True
        return self
    
    def predict(self, X):
        """Predict regression value for X.

        The predicted regression value for each point is computed using
        the predicted value for the previous point as a feature

        Parameters
        ----------
        X : {array-like} of shape (n_samples, n_features)
            The training input samples. 

        Returns
        -------
        y : ndarray of shape (n_samples,)
            The predicted regression values.
        """
        check_is_fitted(self)        
        X = check_array(X, ensure_min_features = 0)
        X_new = np.column_stack((X, np.zeros((len(X), 1))))
        X_new[0,-1] = self.last_target
        y_pred = np.zeros((len(X),1))
        
        for i in range(len(X)-1):
            # need to reshape individual passed to estimator so that they 
            # are 2D arrays 
            y_pred[i] = self.base_estimator.predict(X_new[i,:].reshape(1, -1))
            X_new[i+1,-1] = y_pred[i]
        y_pred[-1] = self.base_estimator.predict(X_new[-1,:].reshape(1,-1)) 
        
        return y_pred
