import pandas as pd
import numpy as np

x_columns = np.array(['app_x','xm2','xm1','x','xp1','xp2','acc_x'])
y_columns = np.array(['app_y','xm2','xm1','x','xp1','xp2','acc_y'])

x_df = pd.DataFrame({}, columns = x_columns)
y_df = pd.DataFrame({}, columns = y_columns)

x_df.to_csv('x_data.csv')
y_df.to_csv('y_data.csv')

print x_df
print y_df
