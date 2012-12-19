#!/usr/bin/python

import sys
import re


errorM, filename, linenumber, colnumber = "", "", "", ""

for line in sys.stdin:
    EMflag = re.search(r'^(Warning|Error|Fatal Error):', line)
    fileLineColflag = re.search(r'^(.+?):(\d+?)\.(\d+):\s*', line)

    if EMflag != None:
        errorM = line.strip('\n')

    if fileLineColflag != None:
        filename, linenumber, colnumber = fileLineColflag.groups()

    if errorM != "" and filename != "" and linenumber != "" and colnumber != "":
        print( "%s:%s: %s (ch.%s)" % (filename, linenumber, errorM, colnumber))
        errorM, filename, linenumber, colnumber = "", "", "", ""
