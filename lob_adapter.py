import lob
import sys
import webbrowser
import requests.exceptions

lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
easyStates = {}

def setUpStatesLookup():
	states = lob.State.list()
	for state in states["data"]:
	    easyStates[state["name"].upper()] = state["short_name"]
	    easyStates[state["short_name"]] = 0

def createLetter(toAddress, fromAddress):
    letter = lob.Letter.create(
        description = 'Coding Challenge Letter',
        to_address = {
              'name': toAddress.name,
              'address_line1': toAddress.address1,
              'address_line2': toAddress.address2,
              'address_city': toAddress.city,
              'address_state': toAddress.state,
              'address_zip': toAddress.zip,
              'address_country': 'US'
          },
          from_address = {
              'name': fromAddress.name,
              'address_line1': fromAddress.address1,
              'address_line2': fromAddress.address2,
              'address_city': fromAddress.city,
              'address_state': fromAddress.state,
              'address_zip': fromAddress.zip,
              'address_country': 'US'
          },
          file = '<html style="padding-top: 3in; margin: .5in;">{{message}}</html>',
          data = {
            'message': fromAddress.msg
          },
          color = True)
    webbrowser.open(letter["url"])  

try:
	setUpStatesLookup()
except requests.exceptions.RequestException as e:
	print("Couldn't connect: {0}".format(e.strerror))
	sys.exit(1) 