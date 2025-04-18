import sys
from antlr4 import *
sys.path.insert(0,'/home/donovan/gitRepos/scriptToArduino/grammar')
sys.path.append('./')  # if you want to avoid PYTHONPATH
from grammar.ArduScriptLexer import ArduScriptLexer
from grammar.ArduScriptParser import ArduScriptParser
from grammar.ArduScriptVisitor import ArduScriptVisitor
import logging
from textwrap import indent, dedent






input_stream = StdinStream()
lexer = ArduScriptLexer(input_stream) 
stream = CommonTokenStream(lexer) 
parser = ArduScriptParser(stream) 
tree = parser.start()
if parser.getNumberOfSyntaxErrors() > 0: 
    print("syntax errors") 

printer = ArduScriptVisitor()

finalText = ""



result = printer.visit(tree)



for x in printer.variables:
    finalText+= f'int {x};\n'

finalText+=("void setup(){\n")
finalText+=("Serial.begin(9600);\n")
for x in printer.usedPins.keys():
    if (printer.usedPins[x] == "Write"):
        finalText += f'pinMode({x},OUTPUT);\n'
    else:
        finalText += f'pinMode({x},INPUT);\n'
finalText+=("}\n")

finalText+=("void loop() {\n")
finalText+= printer.outputText
finalText+= '\n}'

print(finalText)
