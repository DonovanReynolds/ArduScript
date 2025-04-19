# Generated from ArduScript.g4 by ANTLR 4.13.2
from antlr4 import *
import ast
if "." in __name__:
    from .ArduScriptParser import ArduScriptParser
else:
    from ArduScriptParser import ArduScriptParser

# This class defines a complete generic visitor for a parse tree produced by ArduScriptParser.



class ArduScriptVisitor(ParseTreeVisitor):
    
    def __init__(self):
        self.globalCounter = 0
        self.pinStates = {}
        self.variables = set()
        self.scopedVars = set()
        self.globalVars = set()
        self.usedPins = {}
        self.outputText = ""

    #Numbers for iterator variables in loops
    def freshNumber(self):
        self.globalCounter = self.globalCounter+1
        return self.globalCounter
    
    def visitGlobal(self,ctx:ArduScriptParser.GlobalContext):
        self.globalVars.add(ctx.ID().getText())
    
    def visitFunction(self,ctx:ArduScriptParser.FunctionContext):
        for i,argument in enumerate(ctx.ID()):
            if i == 0:
                self.outputText += f"int {argument} ("    
            elif i == 1:
                self.outputText += f"int {argument}"
            else:
                self.outputText += f", int {argument}"
        self.outputText += f")\n"
        self.visit(ctx.block())
        
    
    def visitCallFunction(self,ctx:ArduScriptParser.CallFunctionContext):
        for i,argument in enumerate(ctx.ID()):
            if i == 0:
                self.outputText += f"{argument} ("    
            elif i == 1:
                self.outputText += f"{argument}"
            else:
                self.outputText += f",{argument}"
        self.outputText += f");\n"

    # Visit a parse tree produced by ArduScriptParser#EveryLine.
    def visitEveryLine(self, ctx:ArduScriptParser.EveryLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduScriptParser#block.
    def visitCompound(self, ctx:ArduScriptParser.BlockContext):
        self.scopedVars.update(self.variables)  #Make a set holding onto the currently scoped variables
        self.outputText += ('{\n')
        self.visitChildren(ctx)
        self.outputText += ('}\n')
        self.variables = self.variables & self.globalVars #Take the intersection

        


    # Visit a parse tree produced by ArduScriptParser#Assignment.
    def visitAssignment(self, ctx:ArduScriptParser.AssignmentContext):
        if ctx.ID().getText() in self.variables:
            self.outputText += (f'{ctx.ID()} = {self.visit(ctx.a())};\n')
        else:
            self.outputText += (f'int {ctx.ID()} = {self.visit(ctx.a())};\n')
        self.variables.add(ctx.ID().getText())


            
        


    # Visit a parse tree produced by ArduScriptParser#Skip.
    def visitSkip(self, ctx:ArduScriptParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduScriptParser#If.
    def visitIf(self, ctx:ArduScriptParser.IfContext):
        self.outputText += (f"if ({self.visit(ctx.b())})")
        self.visit(ctx.block(0))
        if (len(ctx.children) > 3):
            self.outputText += (f"else")
            self.visit(ctx.block(1))


    # Visit a parse tree produced by ArduScriptParser#While.
    def visitWhile(self, ctx:ArduScriptParser.WhileContext):
        
        self.outputText += (f"while({self.visit(ctx.b())})")
        self.visitChildren(ctx)


    # Visit a parse tree produced by ArduScriptParser#For.
    def visitFor(self, ctx:ArduScriptParser.ForContext):
        condition = str(self.visit(ctx.a()))
        
        if (condition.isnumeric()):
            iterationTime = int(condition)
            iterVar = f"ITERVAR{self.freshNumber()}"
            self.variables.add(iterVar)
            
            self.outputText += (f'for(int {iterVar} = 0; {iterVar}<{iterationTime};{iterVar}++)')
            self.visitChildren(ctx)
        else:
            iterVar = f"ITERVAR{self.freshNumber()}"
            self.variables.add(iterVar)
            self.outputText += (f'for(int{iterVar} = 0; {iterVar}<{condition};{iterVar}++)')
            self.visitChildren(ctx)


    # Visit a parse tree produced by ArduScriptParser#SetPin.
    def visitSetPin(self, ctx:ArduScriptParser.SetPinContext):
        try:
            if (self.visit(ctx.b())):
                self.outputText += (f'digitalWrite({self.visit(ctx.a())},HIGH);\n')
                self.pinStates[self.visit(ctx.a())] = True
            else:
                self.outputText += (f'digitalWrite({self.visit(ctx.a())},LOW);\n')
                self.pinStates[self.visit(ctx.a())] = False
            self.usedPins[self.visit(ctx.a())] = 'Write'
        except:
            self.outputText += ('Syntax error on setPin make sure to use formate setPin PIN#,high/low')
            exit(1)

    # Visit a parse tree produced by ArduScriptParser#TogglePin.
    def visitTogglePin(self, ctx:ArduScriptParser.TogglePinContext):
        
        self.outputText += (f'digitalWrite({self.visit(ctx.a())},!digitalRead({self.visit(ctx.a())}));\n')
        
        if (self.visit(ctx.a()) not in self.pinStates.keys()):
            self.pinStates[self.visit(ctx.a())] = True
            self.usedPins[self.visit(ctx.a())] = 'Write'

            return
                
        if (self.pinStates[self.visit(ctx.a())]):
            self.pinStates[self.visit(ctx.a())] = False
        else:
            self.pinStates[self.visit(ctx.a())] = True
        self.usedPins[self.visit(ctx.a())] = 'Write'

            
            


    # Visit a parse tree produced by ArduScriptParser#Wait.
    def visitWait(self, ctx:ArduScriptParser.WaitContext):
        self.outputText += (f'delay({self.visit(ctx.a())});\n')


    # Visit a parse tree produced by ArduScriptParser#self.outputText += .
    def visitPrint(self, ctx:ArduScriptParser.PrintContext):
        if (ctx.getChild(1).getText()[0] == '"'):
            self.outputText += (f'Serial.println({ctx.getChild(1)});\n')
        else:
            self.outputText += (f'Serial.println({self.visit(ctx.a())});\n')


    # Visit a parse tree produced by ArduScriptParser#ReadPin.
    def visitReadPin(self, ctx:ArduScriptParser.ReadPinContext):
        self.usedPins[self.visit(ctx.a())] = 'Read'

        return f'digitalRead({self.visit(ctx.a())})'


    # Visit a parse tree produced by ArduScriptParser#High.
    def visitHigh(self, ctx:ArduScriptParser.HighContext):
        return True


    # Visit a parse tree produced by ArduScriptParser#Not.
    def visitNot(self, ctx:ArduScriptParser.NotContext):
        return f"!({self.visit(ctx.b())})"


    # Visit a parse tree produced by ArduScriptParser#ROp.
    def visitROp(self, ctx:ArduScriptParser.ROpContext):
        
        if (ctx.a(1) == None):
            if (self.visit(ctx.b())):
                return f'{self.visit(ctx.a(0))} {ctx.op.text} true'
            else:
                return f'{self.visit(ctx.a(0))} {ctx.op.text} false'
            
        else:
            return f'{self.visit(ctx.a(0))} {ctx.op.text} {self.visit(ctx.a(1))}'


    # Visit a parse tree produced by ArduScriptParser#Or.
    def visitOr(self, ctx:ArduScriptParser.OrContext):
        return f'{self.visit(ctx.b(0))} || {self.visit(ctx.b(1))}'


    # Visit a parse tree produced by ArduScriptParser#Low.
    def visitLow(self, ctx:ArduScriptParser.LowContext):
        return False


    # Visit a parse tree produced by ArduScriptParser#And.
    def visitAnd(self, ctx:ArduScriptParser.AndContext):
        return f'{self.visit(ctx.b(0))} && {self.visit(ctx.b(1))}'


    # Visit a parse tree produced by ArduScriptParser#True.
    def visitTrue(self, ctx:ArduScriptParser.TrueContext):
        return True


    # Visit a parse tree produced by ArduScriptParser#False.
    def visitFalse(self, ctx:ArduScriptParser.FalseContext):
        return False


    # Visit a parse tree produced by ArduScriptParser#BParen.
    def visitBParen(self, ctx:ArduScriptParser.BParenContext):
        return f'({self.visit(ctx.b())})'


    # Visit a parse tree produced by ArduScriptParser#AOp.
    def visitAOp(self, ctx:ArduScriptParser.AOpContext):
        return f'{self.visit(ctx.a(0))} {ctx.op.text} {self.visit(ctx.a(1))}'


    # Visit a parse tree produced by ArduScriptParser#Var.
    def visitVar(self, ctx:ArduScriptParser.VarContext):
        return f'{ctx.ID().getText()}'


    # Visit a parse tree produced by ArduScriptParser#Num.
    def visitNum(self, ctx:ArduScriptParser.NumContext):
        return f'{ctx.NUM()}'


    # Visit a parse tree produced by ArduScriptParser#AParen.
    def visitAParen(self, ctx:ArduScriptParser.AParenContext):
        return f'({self.visit(ctx.a())})'



del ArduScriptParser