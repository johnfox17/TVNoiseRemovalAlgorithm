import numpy as np

##################################################################################################
#Total Variation Based Noise Removal
##################################################################################################
class totalVariation:
    def __init__(self, numNodes, coords, dx, dy, dt, deltaX, deltaY, diffOrder, bVec10, bVec01):
        self.numNodes = numNodes
        self.coords = coords
        self.dx = dx
        self.dy = dy
        self.dt = dt
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.diffOrder = diffOrder
        self.bVec10 = bVec10
        self.bVec01 = bVec01


    def solve(self, tf, initialCondition):
        numNodes = self.numNodes
        coords = self.coords
        dt = self.dt
        numTimeSteps =int(tf/dt)
        time = []
        t = 0
        numNodes = self.numNodes
        coords = self.coords
        print(self.dx)
        print(self.dy) 
        print(self.dt)
        print(self.deltaX)
        print(self.deltaY)
        print(self.diffOrder)
        print(self.bVec10)
        print(self.bVec01)
        '''for i in range(numTimeSteps+3):
            time.append(t)
            t = t + dt
        '''
        np.savetxt('/home/doctajfox/Documents/Thesis_Research/TVNoiseRemovalAlgorithm/data/coords.csv', coords, delimiter=",")
        #a = input('').split(" ")[0]
        #self.SOL_PDDO = 
        self.time = np.array(time)
        #print('Done')
        #a = input('').split(" ")[0]

