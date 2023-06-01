import sys
import re
import ply.yacc as yacc
import bixoLexer
import ply.lex as lexer
import bixoParser

class VirtualMachine:
    def __init__(self, code, quads, varTable):
        self.code = code
        self.quads = quads
        self.varTable = varTable
        self.sCall = []
        self.sIp = [1]
        self.localMem = None
        self.globalMem = None
        self.tempMem = None
        self.stack = []

    def memory(self,localMem, globalMem, tempMem):
        self.localMem = localMem
        self.globalMem = globalMem
        self.tempMem = tempMem

quadGen = bixoParser.quadGen.gen_quad

globalInt = 4000
globalFloat = 8000 
localInt = 12000
localFloat = 16000
tempInt = 20000
tempFloat = 24000
tempBool = 28000

def run(self):
    #memoria del main
   # self.sCall.append(mainMem)
    #run quads
    while self.sIp[-1] <= len(self.quads):
        quad = self.quads[self.sIp[-1] - 1]
        self.runQuads(quad)
        self.sIp[-1] += 1

def runQuads(self, quad):
    op, arg1, arg2, res = quad

    if op == "goto":
        self.goto(res)
    elif op == "=":
        self.assign(arg1, res)
    elif op in ["+", "-", "/", "*", "&&", "||", ">", "<", ">=", "<=", "==", "!="]:
        self.operation(op, arg1, arg2, res)
    elif op == "print":
        self.print(arg1)
    elif op == "gotoF":
        self.gotoF(arg1, res)
    elif op == "era":
        self.era(arg1)
    elif op == "parameter":
        self.param(arg1)
    elif op == "gosub":
        self.gosub(res)

def goto(self, arg1, res):
    #asignamos el num de quad en res
    self.iIp[-1] = res
    
def assign(self, arg1, res):
    value = self.get_value(arg1)
    self.set_value(res, value)

def operation(self, op, arg1, arg2, res):
    value1 = self.get_value(arg1)
    value2 = self.get_value(arg2)

    if op == "+":
        result = value1 + value2
    elif op == "-":
        result = value1 - value2
    elif op == "*":
        result = value1 * value2
    elif op == "/":
        result = value1 / value2
    elif op == "&&":
        result = value1 and value2
    elif op == "||":
        result = value1 or value2
    elif op == ">":
        result = value1 > value2
    elif op == "<":
        result = value1 < value2
    elif op == ">=":
        result = value1 >= value2
    elif op == "<=":
        result = value1 <= value2
    elif op == "==":
        result = value1 == value2
    elif op == "!=":
            result = value1 != value2

    self.set_value(res, result)

def print(self, arg1):
    value = self.get_value(arg1)
    print(value)

def gotoF(self, arg1, res):
    value = self.get_value(arg1)
    if not value:
        self.sIp[-1] = res


