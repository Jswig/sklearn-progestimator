from setuptools import setup

setup(
    name = "scikit-learn-progestimator",
    version = "0.1.0",
    description = "Scikit-learn estimator wrapper for facilitating time series problems",
    author = "Anders Poirel",
    packages=['progestimator'],
    install_requires = [
        "sklearn>=0.22"
    ],
    classifiers = [
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux', 
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
)