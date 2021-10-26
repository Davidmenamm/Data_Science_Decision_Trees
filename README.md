# Data_Science_Decision_Trees

Implementing binary classification for id3, c45 and cart trees.
Saving important metrics of the models to text files.
Displaying roc auc and prec vs recall graphs
Uses statistical over sampling, in order to combat class imbalance
Runs trees under 3 different datasets, which are all hypothesis datasets of a base dataset.


Using chefboost library, modified the base file so that it could return class predictions instead of classification
This is important in order to be able to make the roc auc and pre vs recall graphs, which depend on thresholds.


Modifications where made in the libary chefboost file Training.py, at line 242.
Replace the if statements by the following.

if enableGBM == True and root >= max_depth: #max depth
		final_decision = subdataset['Decision'].mean()
		terminateBuilding = True
	elif enableAdaboost == True:
		#final_decision = subdataset['Decision'].value_counts().idxmax()
		final_decision = functions.sign(subdataset['Decision'].mean()) #get average
		terminateBuilding = True
		enableParallelism = False
	elif len(subdataset['Decision'].value_counts().tolist()) == 1:
		leaf_classes_count = subdataset['Decision'].value_counts()
		leaf_pos_prob = 0
		if '1' in leaf_classes_count:
			leaf_pos_prob = leaf_classes_count['1']/leaf_classes_count.sum()
		final_decision = leaf_pos_prob
		# final_decision = subdataset['Decision'].value_counts().keys().tolist()[0] #all items are equal in this case
		terminateBuilding = True
	elif subdataset.shape[1] == 1: #if decision cannot be made even though all columns dropped
		leaf_classes_count = subdataset['Decision'].value_counts()
		leaf_pos_prob = 0
		if '1' in leaf_classes_count:
			leaf_pos_prob = leaf_classes_count['1']/leaf_classes_count.sum()
		final_decision = leaf_pos_prob
		# final_decision = subdataset['Decision'].value_counts().idxmax() #get the most frequent one
		terminateBuilding = True
	elif algorithm == 'Regression' and subdataset.shape[0] < 5: #pruning condition
	#elif algorithm == 'Regression' and subdataset['Decision'].std(ddof=0)/global_stdev < 0.4: #pruning condition
		final_decision = subdataset['Decision'].mean() #get average
		terminateBuilding = True

This makes the output of classification return a probability.
Works fine, without using boosting methods offered by the libary, like gbm.
