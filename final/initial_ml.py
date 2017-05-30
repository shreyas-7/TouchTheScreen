import ml
import pandas as pd 
from sklearn.svm import SVC


svcmodel_x = SVR()
svcmodel_y = SVR()

x_df_app = np.array(x_df.app_x)
y_df_app = np.array(y_df.app_y)

x_df_acc = np.array(x_df.acc_x)
y_df_acc = np.array(y_df.acc_y)

x_df_val = np.array(x_df.x_val)
y_df_val = np.array(y_df.y_val)

svcmodel_x.fit(np.array([x_df_app,x_df_val]),x_df_ans)
svcmodel_y.fit(np.array([y_df_app,y_df_val]),y_df_ans)

def prediction_of(x,y) :
	return svcmodel_x.predict(x) , svcmodel_y.predict(y)
