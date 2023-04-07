import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

main_data = pd.read_excel('data/imiona.xlsx')
year = main_data['Rok'].unique()

print(year.tail(2))