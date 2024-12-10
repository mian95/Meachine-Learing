"""
Q#3: Import Naive Bayes classifier. Calculate Training and testing accuracies for at least three different datasets. The split size should be 60/40.
"""


from sklearn.datasets import load_wine,load_breast_cancer,load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB



data_sets = [load_wine,load_breast_cancer,load_digits]  

for data_set in data_sets:
    x,y=data_set(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

    model = GaussianNB()
    """ to train the model"""
    model.fit(x_train, y_train)
    
    """ Calculate accuracies"""
    train_accuracy = accuracy_score(model.predict(x_train),y_train)
    test_accuracy = accuracy_score(model.predict(x_test),y_test)
    
    """ Print results """
    print("----------------------------")
    print(f"Training Accuracy: {train_accuracy}")
    print(f"Testing Accuracy: {test_accuracy}")

