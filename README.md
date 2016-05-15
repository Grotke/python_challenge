# Command Line Legislator Letter Creator
Author: Joseph Montgomery


Tested on Windows 7, Windows 8 and Ubuntu 14.04. Written in Python 3.5.1.

## Assumptions

This program doesn't work with addresses outside the United States since the Google Representatives API only works with US addresses. So it assumes all input refers to the US.

## Setup
	
This program requires Python 3 to be installed on the machine. 
While in the project's root, the dependencies can be installed on Windows using

            pip install -r requirements.txt

Ubuntu may require pip3 and you'd install dependencies using

		sudo pip3 install -r requirements.txt


## Input Formatting

You can input an address using a file or the command line. With a file you can input multiple addresses.

Both the command line and file expects arguments in this order:

    NAME - required
    ADDRESS 1 - required
    ADDRESS 2 - *optional*
    CITY - required
    STATE - required
    ZIP (xxxxx-xxxx or xxxxxx) - required
    MESSAGE (less than 200 words) - required

State can be either the full state name or its two-letter code. Case doesn't matter.


### Files

Input files must be put into the input\_files folder. They can then be referenced without the file path in the command line tool as the program will automatically search in input_files. 

Separate multiple addresses in a file by a single blank line. Look at input_files/manytests.txt for an example.


## Use

A browser tab will open automatically with the finished letter on successful completion.

#### Windows

##### From a file:

`py -3 challenge.py <base_file_name>`

Ex:
`py -3 challenge.py sampleinput.txt`

##### On command line 
Sections with multiple words need to be surrounded by quotes, single words don't.

`py -3 challenge.py "name" "address 1" "address 2" "city" "state" "zip" "message"`

Ex:
`py -3 challenge.py "Joe Schmoe" "185 Berry Street" "Suite 170" "San Francisco" California 94107 "This is a message."`

##### Ubuntu:

Replace the `py -3` in the above examples with `python3`.



