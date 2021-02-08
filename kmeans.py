
import matplotlib.pyplot as plt
import numpy
import csv
import random
from collections import defaultdict


DATA_FILE = './dataBoth.csv'
NUM_CLUSTERS = 4
NUM_ITERATIONS = 4

# returns distance between two data points
def distance (x1, y1, x2, y2):
    square = pow((x2 - x1), 2) + pow((y2 - y1), 2)
    return pow(square, 0.5)

# returns data from the csv file as a list of values
# 2D list  with values: [country, birth_rate, life_expectancy]
def readCsv(file_name):

    data = []
    with open(file_name) as csvFile:

        readCSV = csv.reader(csvFile, delimiter=',')
        next(readCSV)

        # create point and add to data dict
        for row in readCSV:
            country = row[0]
            birth_rate = float(row[1])
            life_expectancy = float(row[2])

            data.append([country, birth_rate, life_expectancy])

    return data

# returns index of centroid in centroid list closest to the given point
# takes a 2D array of centroids and a point as an (x,y) array
def getClosestCentroid(centroids, point):

    if(point in centroids):
        return point

    px, py = point[1], point[2]
    distances = []

    # calculate each distance
    for centroid in centroids:

        cx, cy = centroid[0], centroid[1]
        distances.append(distance(px,py,cx,cy))

    # find min distance & return centroid
    min_distance = numpy.amin(distances)
    dist_sum = pow(min_distance, 2)
    min_index = (numpy.where(distances == min_distance))[0][0]

    return centroids[min_index], dist_sum

# returns randomly generated list of centroids
def initializeCentroids(data):

    samples = random.sample(list(data), NUM_CLUSTERS)
    centroids = []

    # create xy point for each data sample
    for sample in samples:
        centroids.append([sample[1], sample[2]])

    #return centroid list
    return centroids

# returns mean-calculated list of centroids
def calculateNewCentroidsFromMean(clusters):

    centroids = []

    # for each cluster, calculate mean of all points
    for cluster in clusters:

        x_sum, y_sum = 0, 0
        size = len(cluster)

        # points are an array list item for each cluster
        for point in cluster:
            x_sum += point[1]
            y_sum += point[2]

        mean_point = [(x_sum / size), (y_sum / size)]
        centroids.append(mean_point)


    return centroids

# scatter plot of all clusters
def plotClusters(clusters, centroids):

    points = [[] for i in range(0, NUM_CLUSTERS)]
    colors = ["Blue", "Green", "Pink", "Red", "Orange", "Purple", "Gray"]

    # plot each point by cluster
    for cluster in range(0, len(clusters)):

        for point in clusters[cluster]:
            plt.scatter(point[1], point[2], c = colors[cluster])

    # Plot centroids
    centroids_x, centroids_y = zip(*centroids)
    plt.scatter(centroids_x, centroids_y, s=80, c='black')

    plt.show()



# read data file
data = readCsv(DATA_FILE)

# initialize
centroids = initializeCentroids(data)
clusters = [[] for x in range(NUM_CLUSTERS)]


# run iterations
for i in range(0, NUM_ITERATIONS):

    # initialize
    clusters = [[] for x in range(NUM_CLUSTERS)]
    dist_sum = 0

    # for each point find closest centroid and add to cluster
    for point in data:

        # get closest centroid index
        closest_centroid, dist_sq = getClosestCentroid(centroids, point)
        dist_sum += dist_sq

        # add point to the cluster for corresponding centroid
        closest_centroid_index = centroids.index(closest_centroid)
        clusters[closest_centroid_index].append(point)

    # visualize clusters
    plotClusters(clusters, centroids)


    # print distance sum
    print("Sum of distances: " + str(dist_sum))

    # get new centroids
    centroids = calculateNewCentroidsFromMean(clusters)


# print results ---------------------------------

for cluster in range(0, len(clusters)):
    countries = []
    num_points = 0
    sum_life_expectancy = 0
    sum_birth_rate = 0

    for point in clusters[cluster]:
        num_points += 1

        sum_birth_rate += point[1]
        sum_life_expectancy += point[2]

        countries.append(point[0])

    print()
    print("Cluster: " + str(cluster))
    print("Mean life expectancy: " + str(sum_life_expectancy / num_points))
    print("Mean birth rate:      " + str(sum_birth_rate / num_points))
    print("Number of countries:  " + str(num_points))
    print()
    print("Countries:")
    for country in countries:
        print(country)
