import re

import address_error
import lob_adapter

NUM_REQUIRED_FIELDS = 6

class AddressAndMessage:
    def __init__(self, addressLines = []):
        numOfLines = len(addressLines)
        includeAddress2 = True
        if numOfLines < NUM_REQUIRED_FIELDS:
            raise address_error.InvalidAddressError("Missing required fields. Expected at least {0} arguments, got {1}.".format(NUM_REQUIRED_FIELDS, numOfLines))
        elif numOfLines == NUM_REQUIRED_FIELDS:
            includeAddress2 = False


        self.addressLines = addressLines
        self.currentLine = 0
        self.name = self.getNextAddressLine()
        self.address1 = self.getNextAddressLine()
        if includeAddress2:
            self.address2 = self.getNextAddressLine()
        else:
            self.address2 = ""
        self.city = self.getNextAddressLine()
        self.getAndValidateState()
        self.getAndValidateZipCode()
        self.getAndValidateMessage()

    def getNextAddressLine(self):
        if self.addressLines and self.currentLine < len(self.addressLines): 
            returnStr = self.addressLines[self.currentLine]
            self.currentLine += 1
            return returnStr
        else:
            return ""

    def getAndValidateZipCode(self):
        self.zip = self.getNextAddressLine()
        compiledRegex = re.compile("^\d{5}(-\d{4})?$")
        if not compiledRegex.match(self.zip):
            raise address_error.InvalidAddressError("Invalid US Zip Code", self.zip)
            self.zip = ""

    def getAndValidateState(self):
        self.state = self.getNextAddressLine().upper()
        try:
            shortCode = lob_adapter.easyStates[self.state]
            if shortCode:
                self.state = shortCode
        except:
            raise address_error.InvalidAddressError("Invalid US State", self.state)

    def getAndValidateMessage(self):
        self.msg = self.getNextAddressLine()
        msgLen = len(self.msg.split())
        if msgLen > 200:
            raise address_error.InvalidInputError("Message needs to be under 200 words. At {0} words.".format(msgLen))

    def __str__(self):
        return "name: {0}\naddress1: {1}\naddress2: {6}\ncity: {2}\nstate: {3}\nzip: {4}\nmsg: {5}\n" \
            .format(self.name, self.address1, self.city, self.state, self.zip, self.msg, self.address2)

    def formatForSearching(self):
        return "{0},{1},{2},{3},{4}".format(self.address1, self.address2, self.city, self.state, self.zip)