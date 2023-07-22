# load and display an image with Matplotlib
import sys
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import totalVariation as tv

#Defining constants
l1=1
l2=1
#N = 100
dx = 1/512
dy = 1/512
dt = 1/512
deltaX = 0.008
deltaY = 0.008

t0 = 0
tf = 5
numTimeSteps =int(tf/dt)
xCoords = np.linspace(0.5/512,1+0.5/512,512)#create the discrete x and y grids
yCoords = np.linspace(0.5/512,1+0.5/512,512) #create the discrete x and y grids
indexing = 'xy'
xCoords, yCoords = np.meshgrid(xCoords, yCoords, indexing=indexing)
xCoords = xCoords.reshape(-1, 1)
yCoords = yCoords.reshape(-1, 1)
coords = np.array([np.round(xCoords[:,0],3), np.round(yCoords[:,0],3)]).T
numNodes = len(xCoords)

def main():

    if sys.platform.startswith('linux'):
        pathToLena = \
                '/home/doctajfox/Documents/Thesis_Research/TVNoiseRemovalAlgorithm/data/Lena.png'
    else:
        pathToLena = 'C:\\Users\\docta\\Documents\\Thesis\\TVNoiseRemovalAlgorithm\\data\\Lena.png'

    # load image as pixel array
    image = cv2.imread(pathToLena)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # summarize shape of the pixel array
    rows, columns = image.shape
    #Create white gaussian noise 
    mean = 0
    std = 50 
    numNodes = rows*columns
    noise = np.random.normal(mean, std, size=numNodes).reshape((rows, columns))
    #a = input('').split(" ")[0]
    noisyImage = np.add(image,noise) 
    
    ##############################
    #PDDO Setup
    ##############################
    horizon = 3.015
    delta = horizon * dx
    bVec10 = np.array([0,1,0])
    bVec01 = np.array([0,0,1])
    diffOrder = 1
    #numBC = 1
    #boundaries = np.array([0.0, 1.0, 0.0, 1.0])
    #BCY = np.array([dy/2,l2-dy/2])
    #diffOrderBC = np.array([1])
    #bVecBC = np.array([0,1,0])
    #nodesBC = np.array([numNodes-1])

    #Denoise by using TV
    TV = tv.totalVariation(numNodes, coords, dx, dy, dt, deltaX, deltaY, diffOrder, bVec10, bVec01)
    TV.solve(5, noisyImage)
    # display the array of pixels as an image
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
    ax1.set_title('Original Image')
    ax2.imshow(noisyImage, cmap='gray', vmin=0, vmax=255)
    ax2.set_title('Noise Image')
    plt.show()
if __name__=="__main__":
    main()

