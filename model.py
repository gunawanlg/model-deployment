# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

german = pd.read_csv('german_credit.csv')

german_prep = german

target = german_prep['default']
temp = german_prep.drop(['default'], axis = 1)

german_model = pd.concat([temp, target], axis = 1)

X = german_model.iloc[:,0:len(german_model.columns)-1]
y = german_model.iloc[:,len(german_model.columns)-1]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) # test size 20% from train test

X_train_ori = X_train
X_test_ori = X_test

X_train_ori

# Categorical boolean mask
categorical_feature_mask = german_model.dtypes==object
numerical_feature_mask = german_model.dtypes!=object

# filter categorical columns using mask and turn it into a list
categorical_cols = german_model.columns[categorical_feature_mask]
numerical_cols = german_model.columns[numerical_feature_mask]

from sklearn.preprocessing import LabelEncoder
temp = {}
for col in categorical_cols:
    le = LabelEncoder()
    le.fit(X_train[col])
    temp[col] = dict(zip(le.classes_, le.transform(le.classes_)))

temp

type(temp)

dict(zip(le.classes_, le.transform(le.classes_)))

class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)

X_train = MultiColumnLabelEncoder(columns=categorical_cols).fit_transform(X_train).to_numpy()
X_test = MultiColumnLabelEncoder(columns=categorical_cols).fit_transform(X_test).to_numpy()

# Fitting Random Forest to the Training set
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Predicting the Test set results
y_pred = rf.predict(X_test)

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

rf_acc = accuracy_score(y_test, rf.predict(X_test))
print(accuracy_score(y_test, rf.predict(X_test)))

rf_auc = roc_auc_score(y_test, rf.predict(X_test))
print(roc_auc_score(y_test, rf.predict(X_test)))

print(rf.feature_importances_)

plt.bar(range(len(rf.feature_importances_)), rf.feature_importances_)
plt.show()

rf_feat = rf.feature_importances_

rf_mod = rf_feat.argsort()[-5:][::-1]

rf_mod

type(X_train)

X_train = X_train[:, rf_mod]

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

X_test = X_test[:, rf_mod]

# Predicting the Test set results
y_pred = rf.predict(X_test)

rf_acc = accuracy_score(y_test, rf.predict(X_test))
print(accuracy_score(y_test, rf.predict(X_test)))

rf_auc = roc_auc_score(y_test, rf.predict(X_test))
print(roc_auc_score(y_test, rf.predict(X_test)))

# Saving model using pickle
pickle.dump(rf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[1.8]]))

fin = X_train_ori.iloc[:, rf_mod]

fin

fin.dtypes

# Categorical boolean mask
categorical_feature_mask = fin.dtypes==object
numerical_feature_mask = fin.dtypes!=object

# filter categorical columns using mask and turn it into a list
categorical_cols = fin.columns[categorical_feature_mask]
numerical_cols = fin.columns[numerical_feature_mask]

temp = {}
for col in categorical_cols:
    le = LabelEncoder()
    le.fit(X_train_ori[col])
    temp[col] = dict(zip(le.classes_, le.transform(le.classes_)))

temp

X_train_ori['credit_amount'].describe()

X_train_ori['age'].describe()

X_train_ori['duration_in_month'].describe()

