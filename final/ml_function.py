import ml
import pandas as pd 
from sklearn.svm import SVC

svcmodel_x = SVR()
svcmodel_y = SVR()

x_df_ans = np.array(x_df.x_pos)
y_df_ans = np.array(y_df.y_pos)

x_df_val = np.array(x_df.x_values)
y_df.val = np.array(y_df.y_values)

svcmodel_x.fit(x_df_val,x_df_ans)
svcmodel_y.fit(y_df_val,y_df_ans)

def prediction_of(x,y) :
	return svcmodel_x.predict(x) , svcmodel_y.predict(y)

