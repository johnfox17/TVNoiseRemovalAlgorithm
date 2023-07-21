import numpy as np
from sklearn.neighbors import KDTree

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
        self.horizon = (deltaX**2+deltaY**2)**0.5
        self.diffOrder = diffOrder
        self.bVec10 = bVec10
        self.bVec01 = bVec01

    def findFamilyMembers(self):
        coords = self.coords
        numNodes = self.numNodes
        horizon = self.horizon
        tree = KDTree(coords, leaf_size=2)
        familyMembers = tree.query_radius(coords, r = horizon)
        self.familyMembers = familyMembers
    
    def solve(self, tf, initialCondition):
        numNodes = self.numNodes
        coords = self.coords
        dt = self.dt
        numTimeSteps =int(tf/dt)
        time = []
        t = 0
        totalVariation.findFamilyMembers(self)
        '''for i in range(numTimeSteps+3):
            time.append(t)
            t = t + dt
        '''
        #np.savetxt('/home/doctajfox/Documents/Thesis_Research/TVNoiseRemovalAlgorithm/data/familyMembers.csv', self.familyMembers[1], delimiter=",")
        print('Done')
        #a = input('').split(" ")[0]
        #self.SOL_PDDO = 
        self.time = np.array(time)
        #print('Done')
        #a = input('').split(" ")[0]

