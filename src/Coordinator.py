""" Manage All the Program """

# imports
from classification import classify, definePaths

# input paths
mainInputPath = r'data\input'

# output paths
mainOutputPath = r'data\output'
# path


# Coordinator
def coordinate():
    # apply binary classification
    # provide paths
    definePaths(mainInputPath, mainOutputPath)
    # with id3
    classify('id3')
    # with CART
    classify('cart')
    # with c4.5
    classify('c45')
