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
    
    
    def calcXis(self):
        coords = self.coords
        numNodes = self.numNodes
        familyMembers = self.familyMembers

        xXis = []
        yXis = []
        for iNode in range(numNodes):
            family = familyMembers[iNode]
            currentXXis = []
            currentYXis = []
            for iFamilyMember in range(len(family)):
                currentXXis.append(coords[family[iFamilyMember]][0] - coords[iNode][0])
                currentYXis.append(coords[family[iFamilyMember]][1] - coords[iNode][1])
            xXis.append(currentXXis)
            yXis.append(currentYXis)
        self.xXis = xXis
        self.yXis = yXis

    def solve(self, tf, initialCondition):
        numNodes = self.numNodes
        coords = self.coords
        dt = self.dt
        numTimeSteps =int(tf/dt)
        time = []
        t = 0
        totalVariation.findFamilyMembers(self)
        totalVariation.calcXis(self)
        '''for i in range(numTimeSteps+3):
            time.append(t)
            t = t + dt
        '''
        #np.savetxt('/home/doctajfox/Documents/Thesis_Research/TVNoiseRemovalAlgorithm/data/familyMembers.csv', self.familyMembers[1], delimiter=",")
        for i in range(7):
            print(self.xXis[i])
            a = input('').split(" ")[0]
        #self.SOL_PDDO = 
        self.time = np.array(time)
        #print('Done')
        #a = input('').split(" ")[0]

