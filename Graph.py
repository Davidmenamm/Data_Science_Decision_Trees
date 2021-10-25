""" For all graphing functions """

# imports
import matplotlib.pyplot as plt
import os
from sklearn import metrics


# graph auc
def graphCurve(y_true, y_pred_proba, algorithmName, functionName, fileName, basePath):
  	# base folder
	baseFolder = basePath+f'\_{fileName}'
	# check if already exists
	if not os.path.exists(baseFolder):
		os.makedirs(baseFolder)
	# algorithm graphs
	filePath = f'{baseFolder}\\_{algorithmName}_{functionName}.png'
	# give values
	fig = plt.figure(f'{fileName}-{algorithmName}-{functionName}')
	plt.title(f'{fileName} - {functionName}')
	# manage cases
	graph = None
	if(functionName == 'ROC'):
  		graph = metrics.RocCurveDisplay.from_predictions(y_true, y_pred_proba, name=algorithmName, ax=plt.gca())
	else:
  		graph = metrics.PrecisionRecallDisplay.from_predictions(y_true, y_pred_proba, name=algorithmName, ax=plt.gca())
	# plot
	fig.savefig(filePath, dpi=fig.dpi)
	# plt.show()