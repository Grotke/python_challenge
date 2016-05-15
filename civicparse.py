import requests

from address_message import AddressAndMessage

def getCivicJson(formattedAddress):
    payload = {"address": formattedAddress, "key":"AIzaSyDtCedJfTLa9wv62z6-gXJpnPu0NTgnxV0"}
    response = requests.get("https://www.googleapis.com/civicinfo/v2/representatives", params=payload)
    response.raise_for_status()
    return response.json()

def getOfficialJson(response):
    offices = response["offices"]
    officials = response["officials"]
    officialIndices = []
    for office in offices:
        name = office["name"]
        if name == "Governor" or name == "United States Senate":
            officialIndices.extend(office["officialIndices"])
    if officialIndices:
        return officials[officialIndices[0]]
    else:
        raise InvalidInputError("No governor or senator found representing that address.")

def convertOfficialJsonToAddress(officialJson):
    address = []
    address.append(officialJson["name"])
    addressObj = officialJson["address"][0]
    address.append(addressObj["line1"])
    if officialJson.get("line2"):
        address.append(addressObj["line2"])
    address.append(addressObj["city"])
    address.append(addressObj["state"])
    address.append(addressObj["zip"])
    address.append("")
    return AddressAndMessage(address)

def getOfficialAddress(searchAddress):
    civicJson = getCivicJson(searchAddress.formatForSearching())
    officialJson = getOfficialJson(civicJson)
    return convertOfficialJsonToAddress(officialJson)