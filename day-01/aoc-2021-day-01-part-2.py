import sys
import string
import doctest

# Checking that all the arguments were entered on the command line, exiting with a message if not.
# Example usage: python3 aoc-2021-day01.py DATA-FILENAME.TXT
def checkStart():
    if len(sys.argv) != 2:
        argumentsNotSet = 'Missing argument(s).\nUsage is like so:\npython3 aoc-2021-day-01.py DATA-FILENAME.TXT'
        print (argumentsNotSet)
        sys.exit(1)
checkStart() # Check the command line arguments were passed

#Initialise variables
#dataFile = 'demo-data.txt'
dataFile = sys.argv[1]
dataDictionary = {0: 'nope'}
def loadFiles(dataDictionary):
    #dataFile = sys.argv[1] # The file name where the processing will happen.
    #dataFile = "day-01-data.txt"
    dataLine = int
    dataLine = 0 # a counter to keep track of the current line of a text file
    # Open the data file (in read-only mode)
    with open(dataFile) as f:
        for line in f:
            dataLine = dataLine + 1 # counter  to track the number of lines processed
            # Add the line to the dictionary, with a numbered index
            dataDictionary[dataLine] = line
            dataDictionary[dataLine] = ( dataDictionary[dataLine].rstrip() )
        #print (dataDictionary)
    # Send back the data dictionary to the main program
    return dataDictionary

loadFiles(dataDictionary)

def processDepthTripletIncreases(dataDictionary):
    # Starting at line 4, because we need at least four lines to get our two 3-value windows.
    sampleCounter = int(4)
    currentValue = 0
    increaseCount = 0
    for i in range(5000):
        try:
            windowB3 = ( dataDictionary[sampleCounter] )
        except:
            print ('End of file.\n')
            break
        windowB3 = int(windowB3)
        windowB2 = ( dataDictionary[sampleCounter - 1] )
        windowB2 = int(windowB2)
        windowB1 = ( dataDictionary[sampleCounter - 2] )
        windowB1 = int(windowB1)
        windowA3 = ( dataDictionary[sampleCounter - 1] )
        windowA3 = int(windowA3)
        windowA2 = ( dataDictionary[sampleCounter - 2] )
        windowA2 = int(windowA2)
        windowA1 = ( dataDictionary[sampleCounter - 3] )
        windowA1 = int(windowA1)
        sliderwindowA = (windowA1+windowA2+windowA3)
        sliderwindowB = (windowB1+windowB2+windowB3)
        printValue = (f"Trying line: {sampleCounter}, with value {windowB3} (and the four values before that). Is {sliderwindowB} bigger than {sliderwindowA} ?.")
        print (printValue)
        if (sliderwindowB > sliderwindowA):
            increaseCount = (increaseCount + 1)
            printValue = (f"Yes. Increase counted. {increaseCount} increases counted so far.")
            print (printValue)
        if (sliderwindowB < sliderwindowA):
            print ("No.")
        if (sliderwindowB == sliderwindowA):
            print ("No change.")
        sampleCounter = sampleCounter + 1
    printValue = (f"{sampleCounter} numbers were processed. There were {increaseCount} increases counted.\n")
    print (printValue)
    return dataDictionary

processDepthTripletIncreases(dataDictionary)
