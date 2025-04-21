# Generated from ArduScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArduScriptParser import ArduScriptParser
else:
    from ArduScriptParser import ArduScriptParser

# This class defines a complete listener for a parse tree produced by ArduScriptParser.
class ArduScriptListener(ParseTreeListener):

    # Enter a parse tree produced by ArduScriptParser#EveryLine.
    def enterEveryLine(self, ctx:ArduScriptParser.EveryLineContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#EveryLine.
    def exitEveryLine(self, ctx:ArduScriptParser.EveryLineContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#function.
    def enterFunction(self, ctx:ArduScriptParser.FunctionContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#function.
    def exitFunction(self, ctx:ArduScriptParser.FunctionContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Compound.
    def enterCompound(self, ctx:ArduScriptParser.CompoundContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Compound.
    def exitCompound(self, ctx:ArduScriptParser.CompoundContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Assignment.
    def enterAssignment(self, ctx:ArduScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Assignment.
    def exitAssignment(self, ctx:ArduScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Skip.
    def enterSkip(self, ctx:ArduScriptParser.SkipContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Skip.
    def exitSkip(self, ctx:ArduScriptParser.SkipContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#If.
    def enterIf(self, ctx:ArduScriptParser.IfContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#If.
    def exitIf(self, ctx:ArduScriptParser.IfContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#While.
    def enterWhile(self, ctx:ArduScriptParser.WhileContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#While.
    def exitWhile(self, ctx:ArduScriptParser.WhileContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#For.
    def enterFor(self, ctx:ArduScriptParser.ForContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#For.
    def exitFor(self, ctx:ArduScriptParser.ForContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#SetPin.
    def enterSetPin(self, ctx:ArduScriptParser.SetPinContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#SetPin.
    def exitSetPin(self, ctx:ArduScriptParser.SetPinContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#TogglePin.
    def enterTogglePin(self, ctx:ArduScriptParser.TogglePinContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#TogglePin.
    def exitTogglePin(self, ctx:ArduScriptParser.TogglePinContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Wait.
    def enterWait(self, ctx:ArduScriptParser.WaitContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Wait.
    def exitWait(self, ctx:ArduScriptParser.WaitContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Print.
    def enterPrint(self, ctx:ArduScriptParser.PrintContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Print.
    def exitPrint(self, ctx:ArduScriptParser.PrintContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#CallFunction.
    def enterCallFunction(self, ctx:ArduScriptParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#CallFunction.
    def exitCallFunction(self, ctx:ArduScriptParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Global.
    def enterGlobal(self, ctx:ArduScriptParser.GlobalContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Global.
    def exitGlobal(self, ctx:ArduScriptParser.GlobalContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Pin.
    def enterPin(self, ctx:ArduScriptParser.PinContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Pin.
    def exitPin(self, ctx:ArduScriptParser.PinContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#High.
    def enterHigh(self, ctx:ArduScriptParser.HighContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#High.
    def exitHigh(self, ctx:ArduScriptParser.HighContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Not.
    def enterNot(self, ctx:ArduScriptParser.NotContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Not.
    def exitNot(self, ctx:ArduScriptParser.NotContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#ROp.
    def enterROp(self, ctx:ArduScriptParser.ROpContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#ROp.
    def exitROp(self, ctx:ArduScriptParser.ROpContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Or.
    def enterOr(self, ctx:ArduScriptParser.OrContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Or.
    def exitOr(self, ctx:ArduScriptParser.OrContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Low.
    def enterLow(self, ctx:ArduScriptParser.LowContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Low.
    def exitLow(self, ctx:ArduScriptParser.LowContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#And.
    def enterAnd(self, ctx:ArduScriptParser.AndContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#And.
    def exitAnd(self, ctx:ArduScriptParser.AndContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#True.
    def enterTrue(self, ctx:ArduScriptParser.TrueContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#True.
    def exitTrue(self, ctx:ArduScriptParser.TrueContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#False.
    def enterFalse(self, ctx:ArduScriptParser.FalseContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#False.
    def exitFalse(self, ctx:ArduScriptParser.FalseContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#BParen.
    def enterBParen(self, ctx:ArduScriptParser.BParenContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#BParen.
    def exitBParen(self, ctx:ArduScriptParser.BParenContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#ReadPin.
    def enterReadPin(self, ctx:ArduScriptParser.ReadPinContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#ReadPin.
    def exitReadPin(self, ctx:ArduScriptParser.ReadPinContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#AOp.
    def enterAOp(self, ctx:ArduScriptParser.AOpContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#AOp.
    def exitAOp(self, ctx:ArduScriptParser.AOpContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Var.
    def enterVar(self, ctx:ArduScriptParser.VarContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Var.
    def exitVar(self, ctx:ArduScriptParser.VarContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#Num.
    def enterNum(self, ctx:ArduScriptParser.NumContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#Num.
    def exitNum(self, ctx:ArduScriptParser.NumContext):
        pass


    # Enter a parse tree produced by ArduScriptParser#AParen.
    def enterAParen(self, ctx:ArduScriptParser.AParenContext):
        pass

    # Exit a parse tree produced by ArduScriptParser#AParen.
    def exitAParen(self, ctx:ArduScriptParser.AParenContext):
        pass



del ArduScriptParser