""" Manage All the Program """

# imports
from classification import classify, definePaths
import timeit

# input paths
mainInputPath = r'data\input'

# output paths
mainOutputPath = r'data\output'
# path


# Coordinator
def coordinate():
    # time init
    tic = timeit.default_timer()
    # apply binary classification
    # provide paths
    definePaths(mainInputPath, mainOutputPath)
    # CART
    classify('CART')
    # ID3
    classify('ID3')
    # C45
    classify('C4.5')
    # time end
    toc = timeit.default_timer()
    elapsed = toc-tic
    print(f'Time elapsed is aproximately {elapsed} seconds o {elapsed/60} minutes')  # seconds
