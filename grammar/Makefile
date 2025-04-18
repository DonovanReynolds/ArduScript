all: ArduScript.py 

ArduScript.py:	ArduScript.g4
		antlr4 -Dlanguage=Python3 -visitor $<

clean:
		rm -f ArduScript.interp ArduScriptLexer.interp ArduScriptLexer.py ArduScriptLexer.tokens ArduScriptListener.py ArduScriptVisitor.py ArduScriptParser.py ArduScript.tokens
