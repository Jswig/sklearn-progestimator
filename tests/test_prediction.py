import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, TimeSeriesSplit
from progestimator.prog_regression import ProgressiveRegression
from numpy.testing import assert_array_almost_equal_nulp


class TestPredictions():
    def test_simple(self):
        y = np.array([[1.0], [3.0], [4.0], [7.0], [15.0], [31.0]])
        X = np.array([[1.0], [1.0], [1.0], [1.0], [1.0], [1.0]])
        model = ProgressiveRegression(LinearRegression())
        model.fit(X,y)

    # test that this is compatible with the rest of the sklearn API
    def test_crossval(self):
        y = np.arange(1.0, 1001, 5.0)
        X = np.ones((200,1))
        model = ProgressiveRegression(LinearRegression())
        score = cross_val_score(
            model, X, y,
            scoring = 'neg_mean_squared_error',
            cv = TimeSeriesSplit()
        )
        print(score)