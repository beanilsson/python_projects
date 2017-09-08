from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

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


createExamples()


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



i1 = Image.open('images/numbers/0.1.png')
i1Array = np.array(i1)

i2 = Image.open('images/numbers/y0.4.png')
i2Array = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
i3Array = np.array(i3)

i4 = Image.open('images/sentdex.png')
i4Array = np.array(i4)

# threshold(i2Array)
# threshold(i3Array)
# threshold(i4Array)

# fig = plt.figure()
# ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
# ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
# ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

# ax1.imshow(i1Array)
# ax2.imshow(i2Array)
# ax3.imshow(i3Array)
# ax4.imshow(i4Array)

# plt.show()
