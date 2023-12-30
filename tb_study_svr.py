#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:04:20 2023

@author: mandefro
Using Support Vector Regression
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# read the dataset
dataset = pd.read_csv('./data/tb_detection_rate_eth_who.csv')
dataset['Year'] = list(range(2000,2022))

X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

# let us reshape the dependent variable so that it will have similar shape
# with the dependent one
y = y.reshape(len(y), 1)

# Let us do feature scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Create an instance of SVR model
regressor = SVR(kernel='rbf')
regressor.fit(X, y)

print(y)