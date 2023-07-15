# load and display an image with Matplotlib
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():

    # load image as pixel array
    image = cv2.imread('C:\\Users\\docta\\Documents\\Thesis\\TVNorm\\data\\Lena.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # summarize shape of the pixel array
    print(image.dtype)
    print(image.shape)
    
    #Create white gaussian noise 
    mean = 0
    std = 50 
    num_samples = 262144
    noise = np.random.normal(mean, std, size=num_samples).reshape((512, 512))
    #a = input('').split(" ")[0]
    noisyImage = np.add(image,noise) 
    # display the array of pixels as an image
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
    ax1.set_title('Original Image')
    ax2.imshow(noisyImage, cmap='gray', vmin=0, vmax=255)
    ax2.set_title('Noise Image')
    plt.show()
if __name__=="__main__":
    main()

