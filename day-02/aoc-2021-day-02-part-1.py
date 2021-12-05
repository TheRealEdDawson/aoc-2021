import sys
import string
import doctest

# Checking that all the arguments were entered on the command line, exiting with a message if not.
# Example usage: python3 aoc-2021-day02-part-1.py DATA-FILENAME.TXT
def checkStart():
    if len(sys.argv) != 2:
        argumentsNotSet = 'Missing argument(s).\nUsage is like so:\npython3 aoc-2021-day-02-part-1.py DATA-FILENAME.TXT'
        print (argumentsNotSet)
        sys.exit(1)
checkStart() # Check the command line arguments were passed.

# Initialise variables
dataFile = sys.argv[1]
dataDictionary = {0: 'nope'}

# Load the data file
def loadFile(dataDictionary):
    #dataFile = sys.argv[1] # The file name where the processing will happen.
    dataLine = int(0) # a counter to keep track of the current line of a text file
    # Open the data file.
    with open(dataFile) as f:
        for line in f:
            dataLine = dataLine + 1 # Counter to track the number of lines processed.
            # Add the line to the dictionary, with a numbered index.
            dataDictionary[dataLine] = line
            dataDictionary[dataLine] = ( dataDictionary[dataLine].rstrip() )
    # Send back the data dictionary to the main program.
    return dataDictionary

loadFile(dataDictionary) # Load the data file

def processNavigationJourney(dataDictionary):
    stepCounter = int(1)
    horizontalPosition = int(0)
    verticalPosition = int(0)
    for i in range(5000):
        try:
            stepText = ( dataDictionary[stepCounter] )
        except:
            print ('End of file.\n')
            break
        stringBits = stepText.split()
        # stringBits[0] is the command word.
        # stringBits[1] is the magnitude of the move action.
        moveSize = int(stringBits[1])
        if (stringBits[0] == "forward"):
            horizontalPosition = (horizontalPosition + moveSize)
        if (stringBits[0] ==  "back"):
            horizontalPosition = (horizontalPosition - moveSize)
        if (stringBits[0] ==  "down"):
            verticalPosition = (verticalPosition + moveSize)
        if (stringBits[0] ==  "up"):
            verticalPosition = (verticalPosition - moveSize)
        printValue = (f"Step {stepCounter}, with value '{stepText}'. Position is now horizonal: {horizontalPosition} and depth: {verticalPosition}.")
        print (printValue)
        stepCounter = stepCounter + 1
    printValue = (f"We made {stepCounter-1} moves. Final position: horizonal {horizontalPosition} and depth {verticalPosition}.\nDoing a ridiculous calculation, we can do {horizontalPosition} times {verticalPosition}, giving {horizontalPosition * verticalPosition}.\n")
    print (printValue)
    return dataDictionary

processNavigationJourney(dataDictionary)
