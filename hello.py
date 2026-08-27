import numpy as np
import pandas as pd



def test(a, b):
    c = a*b
    return c

result = test(5, 3)
print(result)

arr = np.array([1, 2, 3, 4, 5])
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(df)