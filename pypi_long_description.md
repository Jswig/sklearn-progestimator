A scikit-learn estimator which wraps another estimator to provide facilities for time series problems where previous predictions are used
as features.

## Description

When calling `model.fit(X,y)`, `y` with time lag 1 is appended to `X`
before fitting the model.
When calling `model.predict(X)`, for each sample in `X`, the prediction uses the previous known value for `y` (either true or predicted) as an additional feature.

## Usage

This estimator implements the standard `estimator` API. As
such, it should play nice with other scikit-learn objects

Example of wrapping an existing estimator:
```python
>>> from sklearn.linear_model import LinearRegression
    from progestimator.prog_regression import ProgressiveRegression

    y = np.array([[1.0], [3.0], [4.0], [7.0], [15.0], [31.0]])
    X = np.ones(([1.0], [1.0], [1.0], [1.0], [1.0], [1.0]])
    model = ProgressiveRegression(LinearRegression()) 
    model.fit(X,y)

>>> model.predict(([1.0], [1.0], [1.0], [1.0], [1.0], [1.0]]))

array([[  64.98224852],
       [ 137.08896047],
       [ 290.09172322],
       [ 614.74728963],
       [1303.63182285],
       [2765.37143003]])
```