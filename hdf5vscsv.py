#!/usr/bin/env python3
import string
import random
import pandas as pd
import numpy as np

matrix=np.random.random((3000,10))
my_cols=[random.choice(string.ascii_uppercase) for x in range(matrix.shape[1])]
mydf=pd.DataFrame(matrix)
mydf['test']='test'
store=pd.HDFStore('test.h5',complevel=9,complib='bzip2')
store['test']=mydf
store.close()
mydf.to_csv('test.csv',sep=';')
