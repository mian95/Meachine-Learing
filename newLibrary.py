import pandas as pd
# To import the dataset
from sklearn.datasets import load_iris
# To split the dataset
from sklearn.model_selection import train_test_split
# To calculate the accuracy
from sklearn.metrics import accuracy_score
# To import the linear model
from sklearn.linear_model import LinearRegression
# To import the tree model
from sklearn.tree import DecisionTreeClassifier
# To import the logistic model
from sklearn.linear_model import LogisticRegression
# To import the knn model
from sklearn.neighbors import KNeighborsClassifier
# To import the naive bayes model
from sklearn.naive_bayes import GaussianNB

# To import the svm model
from sklearn import svm







# To upload Dataset on x and Y
x,y = load_iris(return_X_y=True)
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
print(x_train.shape)
print(x_test.shape)
print(y_train)
print(y_test)

# To create the model
dt = DecisionTreeClassifier()
dt2 = KNeighborsClassifier()
dt3 = GaussianNB()
dt4 = svm.SVC()

# To train the model
dt.fit(x_train,y_train)
dt2.fit(x_train,y_train)
dt3.fit(x_train,y_train)
dt4.fit(x_train,y_train)    

# To calculate the accuracy
print("To Calculate the accuracy of the model\n")
b = accuracy_score(dt.predict(x_test),(y_test))
print(b)

b2 = accuracy_score(dt2.predict(x_test),(y_test))
print(b2)

b3 = accuracy_score(dt3.predict(x_test),(y_test))
print(b3)

b4 = accuracy_score(dt4.predict(x_test),(y_test))
print(b4)