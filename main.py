import numpy as np
import math
import timeit
import time

SECONDS_TO_NANOSECONDS = 1000 * 1000000

def computeEucledianDistance(v1, v2):
    squareDiff = 0
    for i in range(len(v1)):
        squareDiff += (v1[i] - v2[i]) * (v1[i] - v2[i])
    return math.sqrt(squareDiff)

def computeEucledianDistanceUsingNumpy(v1, v2):
    aux = v1 - v2
    return math.sqrt(sum(aux * aux))

def readNumbersFromFile(fileName):
    inn = []
    f = open(fileName, "r")

    for x in f:
        inn.append(x[:-1].split(" "))
        inn[len(inn) - 1] = [float(numeric_string) for numeric_string in inn[len(inn) - 1]]
    
    f.close();
    return inn;


numbers = readNumbersFromFile("test.in")
######################################################## WARMUP ########################################################
start = time.time()
allResults = []
for k in range(1000):
    index = 0
    while index < len(numbers) - 1:
        allResults.append(computeEucledianDistance(numbers[index], numbers[index + 1]))
        allResults.append(computeEucledianDistanceUsingNumpy(np.array(numbers[index]), np.array(numbers[index + 1])))
        index += 2
end = time.time()
print("Warmup finished in ", ((end - start) * SECONDS_TO_NANOSECONDS) , " nanoseconds ", len(allResults), "\n\n\n")

##################################################### MEASUREMENTS #####################################################
testRuns = 10
index = 0
while index < len(numbers) - 1:
    execTime = timeit.Timer(lambda: computeEucledianDistance(numbers[index], numbers[index + 1])).timeit(number=testRuns) / testRuns
    print("computeEucledianDistance             ", len(numbers[index]), testRuns, execTime * SECONDS_TO_NANOSECONDS)
    index += 2

index = 0

print ("\n\n\n")

while index < len(numbers) - 1:
    npX1 = np.array(numbers[index])
    npX2 = np.array(numbers[index + 1])
    execTimeNumpy = timeit.Timer(lambda: computeEucledianDistanceUsingNumpy(npX1, npX2)).timeit(number=testRuns) / testRuns

    print("computeEucledianDistanceUsingNumpy   ", len(npX1), testRuns, execTimeNumpy * SECONDS_TO_NANOSECONDS)
    index += 2