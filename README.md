# K-Means Clustering Algorithm
This program implements the k-means clustering algorithm on birth rate & life expectancy data. This unsupervised learning algorithm groups the most closely related data points into clusters. 

## Prerequisites
* Python 3.7
* NumPy

## Getting Started
Check the paths of the following directory in the `kmeans.py`:
* `DATA_FILE`: CSV File containing the data to be used for clustering. Data should be in the format: `Countries,BirthRate(Per1000),LifeExpectancy`.

## Using the Program
* Run `kmeans.py`.
* Console output will show cluster data as the program runs
* Optionally adjust the number of iterations or clusters formed by changing the values for `NUM_CLUSTERS` and `NUM_ITERATIONS` at the top of `kmeans.py`
* For each iteration, a graph will be displayed showing the current centroids and color-coded data clusters /
<img src="https://github.com/isabellekazarian/kmeans-algorithm/blob/master/images/iteration1.png" width="400" alt="Sample Iteration 1">
<img src="https://github.com/isabellekazarian/kmeans-algorithm/blob/master/images/iteration4.png" width="400" alt="Sample Iteration 4">

## References
* Data provided by [Hyperion Development](https://www.hyperiondev.com/)
