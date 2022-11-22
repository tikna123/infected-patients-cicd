
from collections import deque
import sys
def parseInput(input):
    inputLines = input.strip().split("\n")
    matrix = []
    for row in inputLines[1:]:
        rowToWrite = []
        for val in row.split(" "):
            rowToWrite.append(int(val))
        matrix.append(rowToWrite)
    return matrix

def isValid(i, j, M, N):
    return (0 <= i < M) and (0 <= j < N)


rowSteps = [-1, 0, 0, 1]
colSteps = [0, -1, 1, 0]

def checkUninfected(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                return True
    return False

def getMinTime(input):
    wardMatrix = parseInput(input)
    # handle base case
    if not wardMatrix or not len(wardMatrix):
        return 0
 
    # `M × N` matrix
    M = len(wardMatrix)
    N = len(wardMatrix[0])
 
    # create a queue to store indices of currently infected patients
    infectedPatientsCurrent = deque()
 
    # enqueue cell coordinates of all infected patients
    for i in range(M):
        for j in range(N):
            if wardMatrix[i][j] ==2:
                infectedPatientsCurrent.append((i, j))
 
    # to keep track of the time taken to make all patients infected
    steps = 0
 
    # loop till all reachable uninfected patients in the wards are processed
    while infectedPatientsCurrent:
 
        
        # copy contents of the original queue `infectedPatientsCurrent` to temp queue `infectedPatientsCurrentTemp` and
        # empty the original queue
        infectedPatientsCurrentTemp = infectedPatientsCurrent.copy()
        infectedPatientsCurrent.clear()
 
        ''' Start of the current pass '''
 
        # process all infected patients in the queue
        while infectedPatientsCurrentTemp:
 
            # pop front value and process it
            x, y = infectedPatientsCurrentTemp.popleft()
 
            # check all four adjacent cells of the current cell
            for k in range(len(rowSteps)):
                # if the current adjacent cell is valid and has a uninfected patients
                if isValid(x + rowSteps[k], y + colSteps[k], M, N) and \
                        wardMatrix[x + rowSteps[k]][y + colSteps[k]] ==1:
                    # make the patient infected
                    wardMatrix[x + rowSteps[k]][y + colSteps[k]] = 2
 
                    # enqueue adjacent cell
                    infectedPatientsCurrent.append((x + rowSteps[k], y + colSteps[k]))
 
        ''' End of the current pass '''
 
        # increment number of steps by 1
        steps = steps + 1
 
    # return number of steps or
    # -1 if the matrix has an unreachable uninfected patients
    if checkUninfected(wardMatrix):
        return -1 
    else: 
        return steps - 1



if __name__ == '__main__':
    unitTestFile = sys.argv[1]
    fr = open(unitTestFile)
    input = fr.read()
    print(getMinTime(input))





