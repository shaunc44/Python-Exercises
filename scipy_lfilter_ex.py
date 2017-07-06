import pandas as pd
from scipy.signal import lfilter
# import numpy as np


df = pd.DataFrame( [1, 7, 9, 5], columns = ['A'] )
print (df)

df['B'] = lfilter( [1], [1, 3], df['A'].astype(float) )
print (df)

