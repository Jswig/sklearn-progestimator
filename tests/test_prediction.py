import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from progestimator.prog_regression import ProgressiveRegression
from numpy.testing import assert_array_almost_equal_nulp


class TestPredictions():
    def test_simple(self):
        y = np.array([[1.0], [3.0], [4.0], [7.0], [15.0], [31.0]])
        X = np.ones((6,1))
        model = ProgressiveRegression(LinearRegression)
        model.fit(X,y)