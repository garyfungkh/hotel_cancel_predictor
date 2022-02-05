import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("https://drive.google.com/u/1/uc?id=17a2cEAPpkQc7hXwnmBr4_6xSAbSmNsMp&export=download")
df

X_train, X_test, y_train, y_test = train_test_split(df[["lead_time",'stays_in_week_nights']],df["is_canceled"], test_size=0.5, random_state=None, shuffle=True, stratify=None)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Your code here
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"%(X_test.shape[0], (y_test != y_pred).sum()))

#accurance
(y_pred == y_test).sum()
(y_pred == y_test).mean()

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
model.predict_proba(X_test)

from sklearn.metrics import roc_curve, auc
fpr, tpr, _ = roc_curve(y_test.values, y_pred[:,1])