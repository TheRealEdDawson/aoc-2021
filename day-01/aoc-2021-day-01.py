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

def processDepthPairIncreases(dataDictionary):
    #print (dataDictionary)
    sampleCounter = int(1)
    currentValue = 0
    increaseCount = 0
    for i in range(5000):
        try:
            currentValue = ( dataDictionary[sampleCounter] )
            currentValue = int(currentValue)
            #print ( type(currentValue) )
            printValue = (f"Trying line: {sampleCounter}, with value {currentValue}. Is it bigger than {dataDictionary[sampleCounter - 1]} ?.")
            print (printValue)
            if (sampleCounter > 1):
                previousValue = ( dataDictionary[sampleCounter - 1] )
                previousValue = int(previousValue)
                #print ( type(previousValue) )
                if (currentValue > previousValue):
                    increaseCount = (increaseCount + 1)
                    printValue = (f"Yes. Increase counted. {increaseCount} increases counted so far.")
                    print (printValue)
                if (currentValue < previousValue):
                    print ("No.")
            if (sampleCounter == 1):
                print ("We don't count this line, because it would be comparing against a non-value.")
        except:
            print ('End of file.\n')
            break
        sampleCounter = sampleCounter + 1
    printValue = (f"{sampleCounter-1} numbers were processed. There were {increaseCount} increases counted.\n")
    print (printValue)
    return dataDictionary

processDepthPairIncreases(dataDictionary)
