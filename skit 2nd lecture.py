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
# To import the cross validation 
from sklearn.model_selection import cross_val_score




#datasets
model = LogisticRegression()
x,y = load_iris(return_X_y=True)

print(x.shape)
print(y.shape)
#spltting dataset
x_train, x_test , y_train,y_test = train_test_split(x,y,test_size=0.8)


models = [LogisticRegression(),LinearRegression(),DecisionTreeClassifier(),KNeighborsClassifier(),GaussianNB(),]

for model in models:
    #dt=model.fit(x_train,y_train)
    cross_validation = cross_val_score(model,x,y,cv=10)
    print(model.__class__.__name__)
    print(cross_validation.mean())
    print(cross_validation.std())






