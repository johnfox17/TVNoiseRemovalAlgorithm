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
dx = 0.001
dy = 0.001
dt = 0.001
deltaX = 0.2015
deltaY = 0.2015

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
        pathToLena = 'C:\\Users\\docta\\Documents\\Thesis\\TVNorm\\data\\Lena.png'

    # load image as pixel array
    image = cv2.imread(pathToLena)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # summarize shape of the pixel array
    rows, columns = image.shape
    print(rows, columns) 
    #Create white gaussian noise 
    mean = 0
    std = 50 
    numNodes = rows*columns
    noise = np.random.normal(mean, std, size=numNodes).reshape((rows, columns))
    #a = input('').split(" ")[0]
    noisyImage = np.add(image,noise) 
    
    #Denoise by using TV
    TV = tv.totalVariation(numNodes, coords, dt)
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

