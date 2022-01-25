from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
import math
from sklearn.metrics import mean_squared_error
from numpy import array
import seaborn as sns
import time
import datetime

def ai(df, flag):
    df2 = df.groupby(['lat','lng','variable_1_name'])['variable_1'].count()
    df2 = df2.reset_index()
    if flag%2 == 1:
        X = df2.drop('variable_1_name', axis=1)
    else:
        X = df2.drop(['lat','lng','variable_1_name'], axis = 1)
    
    X_scaled = MinMaxScaler().fit_transform(X)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X_scaled)
    kmeans.labels_
    label_list = list(kmeans.labels_)
    df2['labels'] = label_list
    return df2