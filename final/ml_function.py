#import functions
#import main
import pandas as pd 
from sklearn.svm import SVR
import numpy as np
from ast import literal_eval

svrmodel_x = SVR()
svrmodel_y = SVR()

print "made model"

x_df = pd.read_csv('x_data.csv', index_col = False)
y_df = pd.read_csv('y_data.csv', index_col = 0)

print "read the csv"

# def convert_to_np_arr(im_as_str):
#     im = [int(i) for i in im_as_str.split()]
#     im = np.asarray(im)
#     im = im.reshape((96, 96))
#     return im


# x_df_app = np.array(x_df.app_x)
# y_df_app = np.array(y_df.app_y)

x_df_acc = np.array(x_df.acc_x)
y_df_acc = np.array(y_df.acc_y)

# # x_df1 = convert_to_np_arr(str(x_df.val_x))
# # y_df1 = convert_to_np_arr(str(y_df.val_y))

# XM2 = np.array(x_df.xm2)
# XM1 = np.array(x_df.xm1)
# X   = np.array(x_df.x)
# XP1 = np.array(x_df.xp1)
# XP2 = np.array(x_df.xp2)

# print XM2

# YM2 = y_df.ym2
# YM1 = y_df.ym1
# Y   = y_df.y 
# YP1 = y_df.yp1
# YP2 = y_df.yp2

# x_df1 = np.array([XM2,XM1,X,XP1,XP2])
# y_df1 = np.array([YM2,YM1,Y,YP1,YP2])

# x_df1 = np.transpose(x_df1)
# y_df1 = np.transpose(y_df1)

A = x_df.drop('acc_x',1).values
print A

B = []

print len(A)
for i in range(len(A)) :

	B.append(A[i][1:-1])

print B

print "took values"

X = svrmodel_x.fit(B,x_df_acc)
Y = svrmodel_y.fit(B,y_df_acc)

print "fit successful"

def x_prediction_of(x) :
	return svrmodel_x.predict(x)

def y_prediction_of(y) :
	return svrmodel_y.predict(y)

