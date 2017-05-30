import pandas as pd
import numpy as np

x_columns = np.array(['app_x','val_x','acc_x'])
y_columns = np.array(['app_y','val_y','acc_y'])

x_df = pd.DataFrame({}, index = None, columns = x_columns)
y_df = pd.DataFrame({}, index = None, columns = y_columns)

x_df.to_csv('x_data.csv')
y_df.to_csv('y_data.csv')

print x_df
print y_df
