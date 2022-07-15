from random import randint
import sys
import os
from os.path import exists
import numpy as np

#A basic data structure to store the parameters from the verilog file as well as their bit sizes.
data = {
    "inputList": [],
    "iBitsList": [],
    "outputList": [],
    "oBitsList": [],
    "totalList": [],
    "randList": []
}

fileName = [] #Stores every filename input as an argument.
file = [] #Stores each file path that needs to be opened.
fileNum = 0 #Keeps track of which file is being accessed at a given time.
PATH = "/home/edvenson/Icarus-Tests/Tests/" #CHANGE THIS TO THE LOCAL PATH TO YOUR VERILOG DESIGN DIRECTORY
SAMPLE_PATH = "/home/edvenson/Icarus-Tests/sample_tb.v" #CHANGE THIS TO WHERE THE SAMPLE_TB.V FILE IS STORED

#A function that will reset all data inside the data structure for future files to fill up.
def refresh(data):
    data.clear()
    data = {
        "inputList": [],
        "iBitsList": [],
        "outputList": [],
        "oBitsList": [],
        "totalList": [],
        "randList": []
    }
    return data

#Returns the sizes of input, output, and the total list.
def inputNum():
    return(len(data["inputList"]))

def outputNum():
    return(len(data["outputList"]))

def totalNum():
    return(len(data["inputList"]) + len(data["outputList"]))

#A function to parse the arguments passed into the file and then open the files they point to. 
def openFiles():
    i = 0
    for x in sys.argv:
        if(i != 0):
            fileName.append(x)
        i = i + 1
    
    for x in fileName:
        file.append(open(PATH + str(x) + "/" + str(x) + ".v"))

#A function for retrieving part of the line.
def appendLine(line, start, num, stop):
    return((line[line.index(start) + num : line.index(stop)]))

#A function to confirm where the parser needs to stop getting the input/output name.
def checkEndChar(line, start, num, isInput, oneBit):
    if isInput:
        if ";" in line:
            data["inputList"].append(appendLine(line, start, num, ";"))
        elif "," in line:
            data["inputList"].append(appendLine(line, start, num, ","))
        else:
            data["inputList"].append(appendLine(line, start, num, "\n"))
        if oneBit:
            data["iBitsList"].append(0)
        else:
            data["iBitsList"].append(appendLine(line, "[", 1, ":"))  
        data["totalList"].append(data["inputList"][inputNum()-1])
    else:
        if ";" in line:
            data["outputList"].append(appendLine(line, start, num, ";"))
        elif "," in line:
            data["outputList"].append(appendLine(line, start, num, ","))
        else:
            data["outputList"].append(appendLine(line, start, num, "\n"))
        if oneBit:
            data["oBitsList"].append(0)
        else:
            data["oBitsList"].append(appendLine(line, "[", 1, ":"))  
        data["totalList"].append(data["outputList"][outputNum()-1])

#A function to find out what the input/output name is and at which index to start finding the name.
def findType(line, isInput):
    if "]" in line:
        if(line[line.index("]")+1].isspace()):
            checkEndChar(line, "]", 2, isInput, False)
        else:
            checkEndChar(line, "]", 1, isInput, False)
    
    elif "wire" in line:
        checkEndChar(line, "e", 2, isInput, True)

    elif "reg" in line:
        checkEndChar(line, "g", 2, isInput, True)

    else:
        if(isInput):
            checkEndChar(line, "input", 6, isInput, True) 
        else:
            checkEndChar(line, "output", 6, isInput, True) 

#A function that checks whether the line is a comment or not, then finds if inputs or outputs are in the line.
#If they are, it calls the other functions to fully parse the line for the names of the inputs/outputs. 
def parseLine(line):
    if (line.find("//", 0, 2) == -1):
        if "input" in line:
            findType(line, True)
        if "output" in line:
            findType(line, False)

#A function to generate the intitial testbench. This function takes a sample testbench, fills in missing
#portions with data parsed earlier, and then adds in randomly generated data for the inputs to be set
#equal to every 5 ns.
def generateFirstTestbench(tb, line, tests):
    if "TB_NAME;" in line:
        line = ("module " + fileName[0] + "_tb;")
        tb.write(line)
        line = "\n"
    
    if "TB_NAME)" in line:
        line=("    $dumpvars(0," + fileName[0] + "_tb);\n")
    
    if "INPUTS" in line:
        i = 0
        while(i < inputNum()):
            if data["inputList"][i] != "clk":
                line = "reg [" + str(data["iBitsList"][i]) + ":0] " + data["inputList"][i] + " = 0;\n"
                tb.write(line)
            i = i+1
        line = ""

    if "OUTPUTS" in line:
        i = 0
        while(i < outputNum()):
            line = "wire [" + str(data["oBitsList"][i]) + ":0] " + data["outputList"][i] + ";\n"
            tb.write(line)
            i=i+1
        line = ""
    
    if "MODULE_NAME" in line:
        i = 0
        line = fileName[0] + " instanceOf ("
        while(i < totalNum()):
            if(i == totalNum() - 1):
                line = line + data["totalList"][i] + ");\n"
            else:
                line = line + data["totalList"][i] + ", "
            i = i + 1

    if "/*SIGNALS" in line:
        i = 0
        while(i < inputNum()):
            if data["iBitsList"][i] == 0:
                data["randList"].append(np.random.randint(low = 0, high = 2, size = int(tests)))
            else:
                data["randList"].append(np.random.randint(low = 0, high = (2**(int(data["iBitsList"][i]) + 1)-1), size = int(tests)))
            i=i+1
        i = 0
        j = 0
        while(i < int(tests)):
            while(j < inputNum()):
                if(j == 0):
                    line = "    # 5 " + str(data["inputList"][j]) + " = " + str(data["randList"][j][i]) + ";\n"
                else:
                    line = "    " + str(data["inputList"][j]) + " = " + str(data["randList"][j][i]) + ";\n"
                j=j+1
                tb.write(line)
            j=0
            i=i+1
            tb.write("\n")
        line = "    # 5 $finish;"

    tb.write(line)

#This function takes the last test bench generated and changes all references to inputs, outputs, and everything else to
#what was found in the most recent file. This is done to preserve the random numbers from the first testbench so that
#each file can be compared to each other. The instanceOf module is fixed because reversed-netlists and golden-netlists
#can have different patterns for inputs and outputs, so this makes sure they will still work properly. 
def generateTestbench(tb, line):
    if fileName[fileNum-1] + "_tb;" in line:
        line = line.replace(fileName[fileNum-1], fileName[fileNum])
    
    if fileName[fileNum-1] + "_tb);" in line:
        line = "    $dumpvars(0," + fileName[fileNum] + "_tb);\n"
    
    if fileName[fileNum-1] + " instanceOf (" in line:
        line = fileName[fileNum] + " instanceOf ("
        i = 0
        while(i < totalNum()):
            if(i == totalNum() - 1):
                line = line + data["totalList"][i] + ");\n"
            else:
                line = line + data["totalList"][i] + ", "
            i = i + 1

    tb.write(line)

def generateFirstTCL():
    if(exists(PATH + fileName[fileNum] + "/" + fileName[fileNum] + ".tcl")):
        os.remove(PATH + fileName[fileNum] + "/" + fileName[fileNum] + ".tcl")
    TCL = open(PATH + fileName[fileNum] + "/" + fileName[fileNum] + ".tcl", "x")
    i=0
    line = "set filter [list "
    while(i < totalNum()):
        line = line + fileName[fileNum] + "_tb." + str(data["totalList"][i]).strip() + " "
        i=i+1
    line = line + "]\n"
    TCL.write(line)
    TCL.write("gtkwave::addSignalsFromList $filter\n")
    TCL.write('gtkwave::/File/Export/Write_VCD_File_As "' + str(PATH) + fileName[fileNum] + "/" + fileName[fileNum] + '.vcd"\n')
    TCL.write("gtkwave::File/Quit")

def generateTCL():
    if(exists(PATH + fileName[fileNum] + "/" + fileName[fileNum] + ".tcl")):
        os.remove(PATH + fileName[fileNum] + "/" + fileName[fileNum] + ".tcl")   
    TCL = open(PATH + fileName[fileNum] + "/" + fileName[fileNum] + ".tcl", "x")
    sample = open(PATH + fileName[fileNum-1] + "/" + fileName[fileNum-1] + ".tcl")
    for line in sample:
        if fileName[fileNum-1] in line:
            line = line.replace(fileName[fileNum-1], fileName[fileNum])
        TCL.write(line)

        

#The main function that calls all of the functions above and generates the testbench.

openFiles() 

for x in file:
    for line in x:
        parseLine(line)

    if(exists(PATH + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v")): #Removes the previously generated testbench if it exists.
        os.remove(PATH + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v")

    if fileNum == 0: #Number of tests is only asked once because all future testbenches generated must have the same number of tests w/ the same values
        tests = input("How many tests would you like to run?\nPlease enter a number: ")
        sample = open(SAMPLE_PATH)
    else:
        sample = open(PATH + fileName[fileNum-1] + "/" + fileName[fileNum-1] + "_tb.v")
    tb = open(PATH + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v", "x")

    for line in sample:
        if(fileNum == 0):
            generateFirstTestbench(tb, line, tests)
        else:
            generateTestbench(tb, line)

    sample.close()
    tb.close()
    if (fileNum == 0):
        generateFirstTCL()
    else:
        generateTCL()
    data = refresh(data) #Sets the data structure back to it's initial state so the next file parsed can store data there.
    fileNum = fileNum + 1 #Increments to the next file.
