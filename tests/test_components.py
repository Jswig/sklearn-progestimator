import pytest
import numpy as np
from progestimator.prog_regression import ProgressiveRegression

class TestShift:
    def test_normal(self):
        exp = np.array([np.nan, 1.0, 2.0])
        res = ProgressiveRegression._shift(
            np.array([1.0, 2.0, 3.0]), 1)
        assert np.allclose(exp, res, equal_nan = True)
 
    def test_fillnans(self):
        exp = np.array([1.0, 1.0, np.nan])
        res = ProgressiveRegression._shift(
            np.array([np.nan, np.nan, np.nan]), 2, 1.0)
        assert np.allclose(exp, res, equal_nan = True)
        
    def test_empty(self):
        exp = np.array([])
        res = ProgressiveRegression._shift(
            np.array([]), 2, 1.0)
        assert np.allclose(exp, res, equal_nan = True)
 
