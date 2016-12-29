import numpy as np
import matplotlib.pyplot as plt
import itertools as t
from mpl_toolkits.mplot3d import Axes3D


givenFilePath = 'C:/Users/Anuj/Desktop/Given_Reduced.txt'
resultFilePath = 'C:/Users/Anuj/Desktop/Clustered_Reduced.txt'
colors = ['b','g','r','c', 'm','y','k','w','bg','rw', 'cr', 'yk', 'cb', 'gc']

print ("Running for given data set 3D")
inputFile = np.genfromtxt(givenFilePath, delimiter='\t')[:,:-1]
clusterIds = np.unique(inputFile[:,0])
#colors = ['b','g','r','c', 'm','y','k','w','bg','rw', 'cr', 'yk', 'cb', 'gc']
fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Graph for given Data')
for i in range (0, clusterIds.shape[0]):
    cluster = inputFile[inputFile[:,0] == clusterIds[i]]
    dimensions = ['X']*(cluster.shape[1]-1)
    for j in range (1,inputFile.shape[1]):
        dimensions[j-1] = cluster[:,j]
    print (" : color : " + str(colors[i]) + " : clusterID : " + str(clusterIds[i]))
    ax.scatter(dimensions[0],dimensions[1], color=colors[i])
plt.show()

print     

print ("Running for given data set 2D")
inputFile = np.genfromtxt(givenFilePath, delimiter='\t')[:,:-1]
clusterIds = np.unique(inputFile[:,0])
#colors = ['b','g','r','c', 'm','y','k','w','bg','rw', 'cr', 'yk', 'cb', 'gc']
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax = fig.add_subplot(111, projection='3d')
ax.set_title('2D Graph for given Data')
for i in range (0, clusterIds.shape[0]):
    cluster = inputFile[inputFile[:,0] == clusterIds[i]]
    dimensions = ['X']*(cluster.shape[1]-1)
    for j in range (1,inputFile.shape[1]):
        dimensions[j-1] = cluster[:,j]
    print (" : color : " + str(colors[i]) + " : clusterID : " + str(clusterIds[i]))
    ax.scatter(dimensions[0],dimensions[1], color=colors[i])
plt.show()

print 
########################################## for clustered dataset #################################################

print("Running for clustered data set 3D")         
inputFile = np.genfromtxt(resultFilePath, delimiter='\t')[:,:-1]
clusterIds = np.unique(inputFile[:,0])
#colors = ['b','g','r','c', 'm','y','k','w','bg','rw', 'cr', 'yk', 'cb', 'gc']
fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Graph for Clustered Data')
for i in range (0, clusterIds.shape[0]):
    cluster = inputFile[inputFile[:,0] == clusterIds[i]]
    dimensions = ['X']*(cluster.shape[1]-1)
    for j in range (1,inputFile.shape[1]):
        dimensions[j-1] = cluster[:,j]
    print (" : color : " + str(colors[i]) + " : clusterID : " + str(clusterIds[i]))
    ax.scatter(dimensions[0],dimensions[1], color=colors[i])
plt.show()    

print

print("Running for clustered data set 2D")         
inputFile = np.genfromtxt(resultFilePath, delimiter='\t')[:,:-1]
clusterIds = np.unique(inputFile[:,0])
#colors = ['b','g','r','c', 'm','y','k','w','bg','rw', 'cr', 'yk', 'cb', 'gc']
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax = fig.add_subplot(111, projection='3d')
ax.set_title('2D Graph for Clustered Data')
for i in range (0, clusterIds.shape[0]):
    cluster = inputFile[inputFile[:,0] == clusterIds[i]]
    dimensions = ['X']*(cluster.shape[1]-1)
    for j in range (1,inputFile.shape[1]):
        dimensions[j-1] = cluster[:,j]
    print (" : color : " + str(colors[i]) + " : clusterID : " + str(clusterIds[i]))
    ax.scatter(dimensions[0],dimensions[1], color=colors[i])
plt.show()  



    
        