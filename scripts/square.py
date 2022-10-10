from envtest import square
import numpy as np
import pandas as pd

x = square(3.14)
s = pd.Series([1, 3, 5, np.nan, 6, x])
print(s)