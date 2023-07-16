import numpy as np

##################################################################################################
#Total Variation Based Noise Removal
##################################################################################################
class totalVariation:
    def __init__(self, numNodes, coords, dt):
        self.numNodes = numNodes
        self.coords = coords
        self.dt = dt


    def solve(self, tf, initialCondition):
        numNodes = self.numNodes
        dt = self.dt
        numTimeSteps =int(tf/dt)
        time = []
        t = 0
        for i in range(numTimeSteps+3):
            print(t)
            time.append(t)
            t = t + dt
        #self.SOL_PDDO = 
        self.time = np.array(time)
        #print('Done')
        #a = input('').split(" ")[0]

