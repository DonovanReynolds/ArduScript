import sys
import os
from antlr4 import *


# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Insert the parent directory into sys.path at index 1 (after the script's directory)
sys.path.insert(1, parent_dir)

sys.path.append('./')  # if you want to avoid PYTHONPATH
from grammar.ArduScriptLexer import ArduScriptLexer
from grammar.ArduScriptParser import ArduScriptParser
from grammar.ArduScriptVisitor import ArduScriptVisitor

#Read in the input and make sure there are no syntax errors
input_stream = StdinStream()
lexer = ArduScriptLexer(input_stream) 
stream = CommonTokenStream(lexer) 
parser = ArduScriptParser(stream) 
tree = parser.start()
if parser.getNumberOfSyntaxErrors() > 0: 
    print("syntax errors") 
printer = ArduScriptVisitor()
finalText = ""


#First pass over the tree to get declarations 
#This is mostly to be able to initialze pinmodes in the setup stage and global variables
result = printer.visit(tree)

for globalVar in printer.globalVars:
    finalText += f'int {globalVar} = {printer.globalVars[globalVar]};\n'
    

    
    

#Print all of the functions
for child in tree.getChildren():
    if type(child) != ArduScriptParser.FunctionContext:
        continue
    functionPrinter = ArduScriptVisitor()
    functionResult = functionPrinter.visit(child)
    finalText += functionPrinter.outputText


#All of the initial setup before the "main" or "loop" stage
finalText+=("void setup(){\n")
finalText+=("Serial.begin(9600);\n")
#Make the pins their correct modes
for x in printer.usedPins.keys():
    if (printer.usedPins[x] == "Write"):
        finalText += f'pinMode({x},OUTPUT);\n'
    else:
        finalText += f'pinMode({x},INPUT);\n'
finalText+=("}\n")
finalText+=("void loop() {\n")

#Here is main or "loop" in arduino
mainPrinter = ArduScriptVisitor()
mainPrinter.variables.update(printer.globalVars.keys())



for child in tree.getChildren():
    if type(child) == ArduScriptParser.FunctionContext:
        continue
    mainPrinter.visit(child)
finalText+= mainPrinter.outputText
finalText+= '\n}'


print(finalText)
