""" Apply binary classification with different decision trees """

# imports
import pandas as pd
import numpy as np
from os import listdir, path
from sklearn import model_selection as ms
from tree import run_tree
from writeToFile import writeTextFile
from Graph import graphCurve


# define paths
def definePaths(inputPath, outputPath):
    definePaths.baseInPath = inputPath
    definePaths.baseOutPath = outputPath


# classify
def classify(algorithm, nFolds=10, randomSeed=100):
    # find input files
    baseInPath = definePaths.baseInPath
    fileNames = [f.replace('.csv', '') for f in listdir(
        baseInPath) if path.isfile(path.join(baseInPath, f))]
    filePaths = [path.join(baseInPath, f) for f in listdir(
        baseInPath) if path.isfile(path.join(baseInPath, f))]
    fileInformation = zip(fileNames, filePaths)
    # loop files
    for info in fileInformation:
        # read csv
        df = pd.read_csv(info[1], engine='c')
        # only features
        X = df.iloc[:, 1: len(df.columns)]
        # only target
        y = df.iloc[:, 0]
        # stratified cross validation
        skf = ms.StratifiedKFold(
            n_splits=nFolds, random_state=randomSeed, shuffle=True)
        stratified_indices = skf.split(X, y)
        # results
        results = dict()
        # stratify k-fold cross
        count = 0
        for trainIndices, testIndices in stratified_indices:
            X_train, X_test = X.iloc[trainIndices, :], X.iloc[testIndices, :]
            y_train, y_test = y.iloc[trainIndices], y.iloc[testIndices]
            # apply selected classification
            infoTree = run_tree(X_train, X_test, y_train, y_test, algorithm)
            # join metrics for all cross validations, for each tree
            # initial values
            if(len(results)==0):
                # list extending
                results['y_true'] = []
                results['y_pred_categ_list'] = []
                results['y_pred_prob_list'] = []
                # scalar sum
                results['tn'] = 0
                results['fp'] = 0
                results['fn'] = 0
                results['tp'] = 0
                # scalar avg
                results['acc'] = []
                results['prec'] = []
                results['rec'] = []
                results['auc'] = []
            else:
                # target
                results['y_true'].extend(infoTree['y_true'])
                results['y_pred_categ_list'].extend(infoTree['y_pred_categ_list'])
                results['y_pred_prob_list'].extend(infoTree['y_pred_prob_list'])
                # confusion matrix
                results['tn'] += infoTree['tn']
                results['fp'] += infoTree['fp']
                results['fn'] += infoTree['fn']
                results['tp'] += infoTree['tp']
                # metrics avg
                results['acc'].append(infoTree['acc'])
                results['prec'].append(infoTree['prec'])
                results['rec'].append(infoTree['rec'])
                results['auc'].append(infoTree['auc'])
            # add counter
            count += 1
        # avg metrics
        acc_np = np.array(results['acc'])
        prec_np = np.array(results['prec'])
        rec_np = np.array(results['rec'])
        auc_np = np.array(results['auc'])
        # mean
        results['acc_avg'] = np.mean(acc_np)
        results['prec_avg'] = np.mean(prec_np)
        results['rec_avg'] = np.mean(rec_np)
        results['auc_avg'] = np.mean(auc_np)
        # std
        results['acc_std'] = np.std(acc_np)
        results['prec_std'] = np.std(prec_np)
        results['rec_std'] = np.std(rec_np)
        results['auc_std'] = np.std(auc_np)
        # write results to file
        writeTextFile(info[0], definePaths.baseOutPath, results, algorithm)
        # Graphics
        plotName = f'{info[0]}'
        function1 = 'ROC'
        function2 = 'PrecRecall'
        # auc
        graphCurve(results['y_true'], results['y_pred_prob_list'], algorithm, function1, info[0], definePaths.baseOutPath)
        # prec vs recall
        graphCurve(results['y_true'], results['y_pred_prob_list'], algorithm, function2, info[0], definePaths.baseOutPath)
