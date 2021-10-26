""" Run tree models for binary classification and numerical features """

# Good base info
# https://sefiks.com/2018/08/27/a-step-by-step-cart-decision-tree-example/
# https://github.com/serengil/chefboost


# imports
import numpy as np
from chefboost import Chefboost as chef
from sklearn import metrics


# Run tree
# receives: features (numerical) and target (binary)
# returns: information and metrics of classification
def run_tree(X_train, X_test, y_train, y_test, algorithm, randomState=100):
    # test list
    y_test_list = y_test.tolist()
    # join dataset, target column must be named "Decision"
    df = X_train.assign(Decision=y_train.astype(str).values)
    # decision tree
    config = {'algorithm': algorithm,
              'enableParallelism': True, 'max_depth': 7, 'num_cores': 4} # max depth not working on 26/10/2021, due to library bug
    # fit train
    model = chef.fit(df, config)
    # predict
    y_pred_prob_list = [] # positive probability ('1')
    for index in range(len(X_test)):
        newInstance = X_test.iloc[index, :].values
        prediction = chef.predict(model, newInstance)
        y_pred_prob_list.append(float(prediction))
    # y pred categorical
    y_pred_categ_list = list( map(lambda a : 1 if a > 0.5 else 0, y_pred_prob_list) )
    # results    
    resultDict = {}
    # save test y pred
    resultDict['y_true'] = y_test_list
    resultDict['y_pred_categ_list'] = y_pred_categ_list    
    resultDict['y_pred_prob_list'] = y_pred_prob_list    
    # Calculate metrics
    # confusion matrix
    confMat = metrics.confusion_matrix(y_test_list, y_pred_categ_list)
    tn, fp, fn, tp = metrics.confusion_matrix(y_test_list, y_pred_categ_list).ravel()
    resultDict['tn'] = tn
    resultDict['fp'] = fp
    resultDict['fn'] = fn
    resultDict['tp'] = tp
    # accuracy
    acc = metrics.accuracy_score(y_test_list, y_pred_categ_list)
    resultDict['acc'] = acc
    # precission
    precission = metrics.precision_score(y_test_list, y_pred_categ_list)
    resultDict['prec'] = precission
    # recall
    recall = metrics.recall_score(y_test_list, y_pred_categ_list)
    resultDict['rec'] = recall
    # auc
    auc = metrics.roc_auc_score(y_test_list, y_pred_prob_list) 
    resultDict['auc'] = auc
    # returns
    return resultDict
    
