import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6], index=['tak', 'nie', 'AAA', 'bcd', 'da'])
print(s)

print(s['tak'])

# Data frame
data = [['Jabłka', 9], ['Banany', 23], ['Winogona', 23]]
df = pd.DataFrame(data, columns=['Owoce', 'Ilość'])
print(df)
# Lub df.columns = 'Owoce', 'Ilość'
