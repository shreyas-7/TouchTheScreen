import pandas as pd
import numpy as np

x_columns = np.array(['approx_x', 'x_values', 'accurate_x'])
y_columns = np.array(['approx_y', 'y_values', 'accurate_x'])

x_df = pd.DataFrame({}, index = None, columns = x_columns)
y_df = pd.DataFrame({}, index = None, columns = y_columns)

x_df.to_csv('x_data.csv')
y_df.to_csv('y_data.csv')

print x_df
print y_df