#NOTE: This file is an extremely rough draft. It's more a proof of concept rather than what will actually be included with bfasst. 
#Assumptions made by this script: Every input is defined in a new line. In other words, THIS is not allowed:
# input wire [5:0] input1, input2;
# We also assume that the bit range ends at 0, so we wouldnt see something like [6:1] or [15:12].

from random import randint
import time
import sys
import os
from os.path import exists
import numpy as np

fileName = []
increment = 0
for x in sys.argv:
    if(increment != 0):
        fileName.append(x)
    increment = increment + 1

file = []
for x in fileName:
    file.append(open("/home/edvenson/Icarus-Tests/Tests/" + str(x) + "/" + str(x) + ".v"))
inputNum = 0
outputNum = 0
totalNum = 0
fileNum = 0
inputList = []
outputList = []
bitsList = []
oBitsList = []
setList = []

#This logic will read in the inputs from the file.
#note: Logic can be added later to parse for if there is a ',' in the line. 
for y in file:
    totalList = []
    for line in y:
        if (line.find("//",0,2) == -1):
            if "input" in line:
                if "]" in line:
                    if(line[line.index("]")+1] == " "):
                        print(line)
                        if ";" in line:
                            inputList.append(line[line.index("]") + 2 : line.index(";")])
                            totalList.append(line[line.index("]") + 2 : line.index(";")])
                        elif "," in line:
                            inputList.append(line[line.index("]") + 2 : line.index(",")])
                            totalList.append(line[line.index("]") + 2 : line.index(",")])
                        else:
                            inputList.append(line[line.index("]") + 2 : line.index("\n")])
                            totalList.append(line[line.index("]") + 2 : line.index("\n")])                                                 
                    else:
                        if ";" in line:
                            inputList.append(line[line.index("]") + 1 : line.index(";")])
                            totalList.append(line[line.index("]") + 1 : line.index(";")])
                        elif "," in line:
                            inputList.append(line[line.index("]") + 1 : line.index(",")])
                            totalList.append(line[line.index("]") + 1 : line.index(",")])
                        else:
                            inputList.append(line[line.index("]") + 1 : line.index("\n")])
                            totalList.append(line[line.index("]") + 1 : line.index("\n")])                                           
                    bitsList.append(int(line[line.index("[") + 1 : line.index(":")]))
                    print("Input: " + inputList[inputNum] + " has " + str(bitsList[inputNum] + 1) + " bits.")
                    inputNum = inputNum + 1
                    totalNum = totalNum + 1
                elif "wire" in line:
                    if ";" in line:
                        inputList.append(line[line.index("e") + 2 : line.index(";")])
                        totalList.append(line[line.index("e") + 2 : line.index(";")])
                    elif "," in line:
                        inputList.append(line[line.index("e") + 2 : line.index(",")])
                        totalList.append(line[line.index("e") + 2 : line.index(",")]) 
                    else:
                        inputList.append(line[line.index("e") + 2 : line.index("\n")])
                        totalList.append(line[line.index("e") + 2 : line.index("\n")])    
                    bitsList.append(0)
                    print("Input: " + inputList[inputNum] + " has " + str(bitsList[inputNum] + 1) + "bits.")
                    inputNum = inputNum + 1
                    totalNum = totalNum + 1
                elif "reg" in line:
                    if ";" in line:
                        inputList.append(line[line.index("g") + 2 : line.index(";")])
                        totalList.append(line[line.index("g") + 2 : line.index(";")])
                    elif "," in line:
                        inputList.append(line[line.index("g") + 2 : line.index(",")])
                        totalList.append(line[line.index("g") + 2 : line.index(",")]) 
                    else:
                        inputList.append(line[line.index("g") + 2 : line.index("\n")])
                        totalList.append(line[line.index("g") + 2 : line.index("\n")])                                         
                    bitsList.append(0)
                    print("Input: " + inputList[inputNum] + " has " + str(bitsList[inputNum] + 1) + " bits.")
                    totalNum = totalNum + 1
                    inputNum = inputNum + 1 
                else:
                    if ";" in line:
                        inputList.append(line[line.index("input") + 6 : line.index(";")])
                        totalList.append(line[line.index("input") + 6 : line.index(";")])
                    elif "," in line:
                        inputList.append(line[line.index("input") + 6 : line.index(",")])
                        totalList.append(line[line.index("input") + 6 : line.index(",")])
                    else:
                        inputList.append(line[line.index("input") + 6 : line.index("\n")])
                        totalList.append(line[line.index("input") + 6 : line.index("\n")])                                    
                    bitsList.append(0)
                    print("Input: " + inputList[inputNum] + " has " + str(bitsList[inputNum] + 1) + "bits.")
                    inputNum = inputNum + 1
                    totalNum = totalNum + 1

            elif "output" in line:
                if "]" in line:
                    if(line[line.index("]")+1] == " "):
                        if ";" in line:
                            outputList.append(line[line.index("]") + 2 : line.index(";")])
                            totalList.append(line[line.index("]") + 2 : line.index(";")]) 
                        elif "," in line:
                            outputList.append(line[line.index("]") + 2 : line.index(",")])
                            totalList.append(line[line.index("]") + 2 : line.index(",")])
                        else:
                            outputList.append(line[line.index("]") + 2 : line.index("\n")])
                            totalList.append(line[line.index("]") + 2 : line.index("\n")])                                                 
                    else:
                        if ";" in line:
                            outputList.append(line[line.index("]") + 1 : line.index(";")])
                            totalList.append(line[line.index("]") + 1 : line.index(";")]) 
                        elif "," in line:
                            outputList.append(line[line.index("]") + 1 : line.index(",")])
                            totalList.append(line[line.index("]") + 1 : line.index(",")])
                        else:
                            outputList.append(line[line.index("]") + 1 : line.index("\n")])
                            totalList.append(line[line.index("]") + 1 : line.index("\n")]) 
                    oBitsList.append(int(line[line.index("[") + 1 : line.index(":")]))
                    print("Output: " + outputList[outputNum] + " has " + str(oBitsList[outputNum] + 1) + " bits.")
                    totalNum = totalNum + 1
                    outputNum = outputNum + 1
                elif "wire" in line:
                    if ";" in line:
                        outputList.append(line[line.index("e") + 2 : line.index(";")])
                        totalList.append(line[line.index("e") + 2 : line.index(";")]) 
                    elif "," in line:
                        outputList.append(line[line.index("e") + 2 : line.index(",")])
                        totalList.append(line[line.index("e") + 2 : line.index(",")])   
                    else:
                        outputList.append(line[line.index("e") + 2 : line.index("\n")])
                        totalList.append(line[line.index("e") + 2 : line.index("\n")])                      
                    oBitsList.append(0)
                    print("Output: " + outputList[outputNum] + " has " + str(oBitsList[outputNum] + 1) + " bits.")
                    totalNum = totalNum + 1
                    outputNum = outputNum + 1
                elif "reg" in line:
                    if ";" in line:
                        outputList.append(line[line.index("g") + 2 : line.index(";")])
                        totalList.append(line[line.index("g") + 2 : line.index(";")]) 
                    elif "," in line:
                        outputList.append(line[line.index("g") + 2 : line.index(",")])
                        totalList.append(line[line.index("g") + 2 : line.index(",")])  
                    else:
                        outputList.append(line[line.index("g") + 2 : line.index("\n")])
                        totalList.append(line[line.index("g") + 2 : line.index("\n")])                       
                    oBitsList.append(0)
                    print("Output: " + outputList[outputNum] + " has " + str(oBitsList[outputNum] + 1) + " bits.")
                    totalNum = totalNum + 1
                    outputNum = outputNum + 1            

                else:
                    print(line)
                    if ";" in line:
                        outputList.append(line[line.index("output") + 7 : line.index(";")])
                        totalList.append(line[line.index("output") + 7 : line.index(";")]) 
                    elif "," in line:
                        outputList.append(line[line.index("output") + 7 : line.index(",")])
                        totalList.append(line[line.index("output") + 7 : line.index(",")])
                    else:
                        outputList.append(line[line.index("output") + 7 : line.index("\n")])
                        totalList.append(line[line.index("output") + 7 : line.index("\n")])                                      
                    oBitsList.append(0)
                    print("Output: " + outputList[outputNum] + " has " + str(oBitsList[outputNum] + 1) + " bits.")
                    totalNum = totalNum + 1
                    outputNum = outputNum + 1

    index = 0
    testIndex = 0

    if(exists("/home/edvenson/Icarus-Tests/Tests/" + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v")):
        print("File already exists!")
        delete = input("Create a new one?\n0 for no, 1 for yes")
        if(int(delete)):
            os.remove("/home/edvenson/Icarus-Tests/Tests/" + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v")
            index = 0
            testIndex = 0
            inputIndex = 0
            outputIndex = 0
            if fileNum == 0:
                tests = input("How many tests would you like to run?\nPlease input a number")
            tb = open("/home/edvenson/Icarus-Tests/Tests/" + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v", "x")
            if fileNum == 0:
                sample = open("/home/edvenson/Icarus-Tests/sample_tb.v")
            else:
                sample = open("/home/edvenson/Icarus-Tests/Tests/" + fileName[fileNum-1] + "/" + fileName[fileNum-1] + "_tb.v")
            if fileNum == 0:
                for line in sample:

                    if "TB_NAME;" in line:
                        line = ("module " + fileName[0] + "_tb;")
                        tb.write(line)
                        line = "\n"

                    if "TB_NAME)" in line:
                        line =("    $dumpvars(0," + fileName[0] + "_tb);")
                        tb.write(line)
                        line = ""

                    if "INPUTS" in line:
                        while(index < inputNum):
                            line = "    reg [" + str(bitsList[index]) + ":0] " + inputList[index] + " = 0;\n"
                            tb.write(line)
                            index = index+1
                        line = ""
                        index = 0

                    if "OUTPUTS" in line:
                        while(index < outputNum):
                            line = "    wire [" + str(oBitsList[index]) + ":0] " + outputList[index] + ";\n"
                            tb.write(line)
                            index = index + 1
                        line = ""
                        index = 0

                    if "MODULE_NAME" in line:
                        line = fileName[fileNum] + " instanceOf ("
                        while(index < totalNum):
                            if(index == totalNum -1):
                                line = line + totalList[index] + ");"
                            else:
                                line = line + totalList[index] + ", "
                            index = index + 1
                        index = 0

                    if "/*SIGNALS" in line:
                        while(index < inputNum):
                            setList.append(np.random.randint(low = 0, high = (2**((bitsList[index])+1)-1), size = int(tests)))
                            index = index + 1
                        index = 0
                        textIndex = 0
                        tb.write("\n")
                        while(testIndex < int(tests)):
                            while(index < inputNum):
                                if(index == 0):
                                    line = "    # 5 " + str(inputList[index]) + " = " + str(setList[index][testIndex]) + ";\n"
                                else:
                                    line = "    " + str(inputList[index]) + " = " + str(setList[index][testIndex]) + ";\n"
                                index = index+1
                                tb.write(line)       
                            index = 0
                            testIndex = testIndex+1
                            tb.write("\n")
                        line = "    # 5 $finish;"         

                    tb.write(line)
                fileNum = fileNum + 1
                inputNum = 0
                outputNum = 0
                totalNum = 0
                inputList.clear
                outputList.clear
                del totalList
                bitsList.clear
                oBitsList.clear
                setList.clear
                sample.close()
                tb.close()    
            else:
                for line in sample:
                    if fileName[fileNum-1] + "_tb;" in line:
                        line = ("module " + fileName[fileNum] + "_tb;\n")

                    if fileName[fileNum-1] + "_tb);" in line:
                        line =("    $dumpvars(0," + fileName[fileNum] + "_tb);\n")

                    if "    reg [" in line:
                        line = "    reg [" + str(bitsList[inputIndex]) + ":0] " + inputList[inputIndex] + " = 0;\n"
                        inputIndex = inputIndex + 1
                        tb.write(line)
                        line = ""

                    if "    wire [" in line:
                        line = "    wire [" + str(oBitsList[outputIndex]) + ":0] " + outputList[outputIndex] + ";\n"
                        outputIndex = outputIndex + 1
                        tb.write(line)
                        line = ""

                    if fileName[fileNum-1] + " instanceOf (" in line:
                        print(totalList)
                        line = fileName[fileNum] + " instanceOf ("
                        while(index < totalNum):
                            if(index == totalNum -1):
                                line = line + totalList[index] + ");"
                            else:
                                line = line + totalList[index] + ", "
                            index = index + 1
                        index = 0
                        tb.write(line)
                        line = "\n"
                    tb.write(line)
                fileNum = fileNum + 1
                inputNum = 0
                outputNum = 0
                totalNum = 0
                inputIndex = 0
                outputIndex = 0
                inputList.clear
                outputList.clear
                del totalList
                bitsList.clear
                oBitsList.clear
                setList.clear
                sample.close()
                tb.close()   
        else:
            print("Ok")
    else:
        index = 0
        testIndex = 0
        if fileNum == 0:
            tests = input("How many tests would you like to run?\nPlease input a number")
        tb = open("/home/edvenson/Icarus-Tests/Tests/" + fileName[fileNum] + "/" + fileName[fileNum] + "_tb.v", "x")
        if fileNum == 0:
            sample = open("/home/edvenson/Icarus-Tests/sample_tb.v")
        else:
            sample = open("/home/edvenson/Icarus-Tests/Tests/" + fileName[fileNum-1] + "/" + fileName[fileNum-1] + "_tb.v")
        if fileNum == 0:
            for line in sample:

                if "TB_NAME;" in line:
                    line = ("module " + fileName[0] + "_tb;")

                if "TB_NAME)" in line:
                    line =("    $dumpvars(0," + fileName[0] + "_tb);")

                if "INPUTS" in line:
                    while(index < inputNum):
                        line = "    reg [" + str(bitsList[index]) + ":0] " + inputList[index] + " = 0;\n"
                        tb.write(line)
                        index = index+1
                    line = ""
                    index = 0

                if "OUTPUTS" in line:
                    while(index < outputNum):
                        line = "    wire [" + str(oBitsList[index]) + ":0] " + outputList[index] + ";\n"
                        tb.write(line)
                        index = index + 1
                    line = ""
                    index = 0

                if "MODULE_NAME" in line:
                    line = fileName[fileNum] + " instanceOf ("
                    while(index < totalNum):
                        if(index == totalNum -1):
                            line = line + totalList[index] + ");"
                        else:
                            line = line + totalList[index] + ", "
                        index = index + 1
                    index = 0

                if "/*SIGNALS" in line:
                    while(index < inputNum):
                        setList.append(np.random.randint(low = 0, high = (2**((bitsList[index])+1)-1), size = int(tests)))
                        index = index + 1
                    index = 0
                    textIndex = 0
                    tb.write("\n")
                    while(testIndex < int(tests)):
                        while(index < inputNum):
                            if(index == 0):
                                line = "    # 5 " + str(inputList[index]) + " = " + str(setList[index][testIndex]) + ";\n"
                            else:
                                line = "    " + str(inputList[index]) + " = " + str(setList[index][testIndex]) + ";\n"
                            index = index+1
                            tb.write(line)       
                        index = 0
                        testIndex = testIndex+1
                        tb.write("\n")
                    line = "    # 5 $finish;"         

                tb.write(line)
            fileNum = fileNum + 1
            inputNum = 0
            outputNum = 0
            totalNum = 0
            inputList.clear
            outputList.clear
            totalList.clear
            bitsList.clear
            oBitsList.clear
            setList.clear
            sample.close()
            tb.close()    
        else:
            for line in sample:
                if fileName[fileNum-1] + "_tb;" in line:
                    line = ("module " + fileName[fileNum] + "_tb;")

                if fileName[fileNum-1] + "_tb);" in line:
                    line =("    $dumpvars(0," + fileName[fileNum] + "_tb);")

                if "    reg [" in line:
                    while(index < inputNum):
                        line = "    reg [" + str(bitsList[index]) + ":0] " + inputList[index] + " = 0;\n"
                        tb.write(line)
                        index = index+1
                    line = ""
                    index = 0

                if "    wire [" in line:
                    while(index < outputNum):
                        line = "    wire [" + str(oBitsList[index]) + ":0] " + outputList[index] + ";\n"
                        tb.write(line)
                        index = index + 1
                    line = ""
                    index = 0

                if fileName[fileNum-1] + " instanceOf (" in line:
                    line = fileName[fileNum] + " instanceOf ("
                    while(index < totalNum):
                        if(index == totalNum -1):
                            line = line + totalList[index] + ");"
                        else:
                            line = line + totalList[index] + ", "
                        index = index + 1
                    index = 0
                tb.write(line)
            fileNum = fileNum + 1
            inputNum = 0
            outputNum = 0
            totalNum = 0
            inputList.clear
            outputList.clear
            totalList.clear
            bitsList.clear
            oBitsList.clear
            setList.clear
            sample.close()
            tb.close()    
