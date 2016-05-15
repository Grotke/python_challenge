import sys
import re
import lob
import requests
import webbrowser

import civicparse
from address_message import AddressAndMessage
import lob_adapter
import address_error

INPUT_DIR = "./input_files/"

# Argument order should be name, address 1, address 2 (optional), 
# city, state, country, zip, message
def readAddresses():
    numOfArguments = len(sys.argv)
    addresses = []
    if numOfArguments < 2:
        print("Need Address or File.")
    elif numOfArguments == 2:
        inFileName = INPUT_DIR + sys.argv[1]
        inFile = None
        try:
            inFile = open(inFileName, 'r')
            addresses = readAddressesFromFile(inFile)
            inFile.close()
        except IOError as e:
            print("I/O error: {0}".format(e.strerror))
        except:
            print("Unexpected error: ", sys.exc_info()[0])
        finally:
            if inFile != None:
                inFile.close()
    else:
        addresses = readAddressFromCommandLine()

    return addresses


def readAddressFromCommandLine():
    addresses = []
    currentAddress = []
    for line in sys.argv[1:]:
        currentAddress.append(line.strip())
    addresses.append(currentAddress)
    return addresses

"""Reads addresses from a file where each address is separated by a blank line. Returns all addresses."""
def readAddressesFromFile(fileObj):
    addresses = []
    currentAddress = []
    for line in fileObj:
        strippedLine = line.strip()
        if strippedLine == '':
            addresses.append(currentAddress)
            currentAddress = []
        else:
            currentAddress.append(strippedLine)
    if currentAddress:
        addresses.append(currentAddress)
    return addresses



# Argument order should be name, address 1, address 2 (optional), 
# city, state, zip, message

def processAddresses(addresses):
    addressObjects = []
    for address in addresses:
        try:
            addressObjects.append(AddressAndMessage(address))
        except Exception as e:
            print(e)

    return addressObjects
        
def main():
    addresses = processAddresses(readAddresses())
    for address in addresses:
        try:
            official = civicparse.getOfficialAddress(address)
            lob_adapter.createLetter(official, address)
        except requests.exceptions.RequestException as e:
            print(e)

main()