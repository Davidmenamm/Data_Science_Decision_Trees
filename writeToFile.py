""" Write to files """


# imports
import os


# Write text file dinamically
def writeTextFile(fileName, basePath, data, algorithm):
	# base folder
	baseFolder = basePath+f'\_{fileName}'
	# check if already exists
	if not os.path.exists(baseFolder):
		os.makedirs(baseFolder)
	# algorithm details and metrics
	filePath = f'{baseFolder}\\_{algorithm}.txt'
	# write data
	with open(filePath, 'w') as fileAlgorithm:
		# metrics
		fileAlgorithm.write(f'Algorithm is: {algorithm}\n\n\n')
		fileAlgorithm.write(f'Accurracy avg: {data["acc_avg"]}\n\n')
		fileAlgorithm.write(f'Acurracy std: {data["acc_std"]}\n\n')
		fileAlgorithm.write(f'Precission avg: {data["prec_avg"]}\n\n')
		fileAlgorithm.write(f'Precission std: {data["prec_std"]}\n\n')
		fileAlgorithm.write(f'Recall avg: {data["rec_avg"]}\n\n')
		fileAlgorithm.write(f'Recall std: {data["rec_std"]}\n\n')
		fileAlgorithm.write(f'AUC avg: {data["auc_avg"]}\n\n')
		fileAlgorithm.write(f'AUC std: {data["auc_std"]}\n\n')
		# confusion matrix
		confMat = [[data["tn"], data["fp"]], [data["fn"], data["tp"]]]
		conMatInd = ['TN', 'FP', 'FN','TP']
		fileAlgorithm.write(f'Confusion matrix sum:\n{conMatInd}\n{confMat}\n\n')
		# predictions
		fileAlgorithm.write(
			f'Predicted Target Prob:\n{str(data["y_pred_prob_list"])}\n\n')
		fileAlgorithm.write(
			f'Predicted Target Categ:\n{str(data["y_pred_categ_list"])}\n\n')
		fileAlgorithm.write(
			f'Real Target:\n{str(data["y_true"])}\n\n\n')