# script to verify the correlation of the encoded hastags

##################################################
## A data visualisation script investigating the 
## correlation between features for the original 
## dataset and the new dataset 
##################################################
## Author: Paul Houssel
## Last Updated: Nov 19 2022, 21:22
##################################################

# import packages
import pandas as pd
from scipy.interpolate import Rbf
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords 

from pipeline import featurePipeline

# Load the training data
train_data = pd.read_csv("hashtahs_encoded.csv", index_col=False)

# COMPUTE CORRELATION MATRIX 

# run correlation matrix and plot
f, ax = plt.subplots(figsize=(10, 10))
corr = train_data.corr()
sns.heatmap(corr,annot=True, mask=np.zeros_like(corr, dtype=np.bool),
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)

f.suptitle('Correlation Matrix between features in the orginal Dataset', fontsize=16)
plt.savefig('../figs/hashtags/correlation-matrix.png')