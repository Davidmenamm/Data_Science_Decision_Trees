""" Apply ID3 decision tree for binary classification"""

# imports
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


# ID3 decision tree
# receives: features and target
# returns: accuracy, testY, predY, ... other metrics for later graphing...
def id3_tree(X_train, X_test, y_train, y_test, randomState):
    # decision tree
    tree = DecisionTreeClassifier(
        criterion="entropy", random_state=randomState)
    # fit train
    tree.fit(X_train, y_train)
    # predict
    y_pred = tree.predict(X_test)
    # acuracy
    acc = metrics.accuracy_score(y_test, y_pred)
    # returns
    return y_test, y_pred, acc


# Good base info
# https://www.kaggle.com/kashnitsky/topic-3-decision-trees-and-knn
