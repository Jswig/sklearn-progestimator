# sklearn-progestimator
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/scikit-learn-progestimator)](https://pypi.python.org/pypi/scikit-learn-progestimator/)
[![PyPI version fury.io](https://badge.fury.io/py/scikit-learn-progestimator.svg)](https://pypi.python.org/pypi/scikit-learn-progestimator/)
[![PyPI license](https://img.shields.io/pypi/l/scikit-learn-progestimator)](https://pypi.python.org/pypi/scikit-learn-progestimator/)



A scikit-learn estimator which wraps a base estimator to provide facilities for 
time series problems where previous predictions are used as features.

---

My other goal here is to use this as a toy project for learning standard 
tools for Python development (`pytest`, `tox`, `setuptools`, `pdb`)

## Installation

Using `pip`:
```bash
pip install scikit-learn-progestimator
```

Using `conda`:
```
WIP
```

## Usage

When calling `estimator.fit(X,y)`, `y` with time lag 1 is appended to `X`
before fitting the model.
When calling `estimator.predict(X)`, for each sample in `X`, the prediction uses the previous known value for `y` (either true or predicted) as an additional feature.

This wrapper implements the standard `estimator` API. As such, it should play well with the rest of scikit-learn.
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

## Development

### Environment
 
Create the development environment and activate it
```bash
conda env create -f environment.yml
conda activate progregressor-dev
```
Alternatively, the environment can be replciated with `pip` and
`requirements.txt`

### Tests

In `tests`
```bash
python -m pytest
```
