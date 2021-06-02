# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:23:39 2021

@author: Kulsum
"""

import pandas as pd
dataset=pd.read_excel("2.Factor Analysis.xlsx",sheet_name=0)

dataset.head()
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

