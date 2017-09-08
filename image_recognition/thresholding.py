from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            #print str(eachNum) + '.' + str(eachVer)
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + '.png'
            exampleImage = Image.open(imgFilePath)
            exampleImageArray = np.array(exampleImage)
            exampleImageArray1 = str(exampleImageArray.tolist())

            lineToWrite = str(eachNum) + '::' + exampleImageArray1 + '\n'
            numberArrayExamples.write(lineToWrite)


def threshold(imageArray):
    balanceArray = []
    newArray = imageArray

    for eachRow in imageArray:
        for eachPixel in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPixel[:3])/len(eachPixel[:3])
            balanceArray.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceArray)/len(balanceArray)

    for eachRow in newArray:
        for eachPixel in eachRow:
            if reduce(lambda x, y: x + y, eachPixel[:3])/len(eachPixel[:3]) > balance:
                eachPixel[0] = 255
                eachPixel[1] = 255
                eachPixel[2] = 255
                eachPixel[3] = 255
            else:
                eachPixel[0] = 0
                eachPixel[1] = 0
                eachPixel[2] = 0
                eachPixel[3] = 255

    return newArray

def whatNumIsThis(filePath):
    matchedArray = []
    loadExamples = open('numArEx.txt', 'r').read()
    loadExamples = loadExamples.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamples:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNumber = splitEx[0]
            currentArray = splitEx[1]

            eachPixExample = currentArray.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixExample):
                if eachPixExample[x] == eachPixInQ[x]:
                    matchedArray.append(int(currentNumber))

                x += 1

    print matchedArray
    x = Counter(matchedArray)
    print x

whatNumIsThis('images/test3.png')
