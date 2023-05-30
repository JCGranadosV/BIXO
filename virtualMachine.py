import sys
import re

class VirtualMachine:
    def __init__(self, code, quads, varTable):
        self.code = code
        self.quads = quads
        self.varTable = varTable

    def memory(self,localMem, globalMem, tempMem):
        self.localMem = localMem
        self.globalMem = globalMem
        self.tempMem = tempMem

    def initType(type: str):
        if type == 'int':
            return 0
        if type == 'float':
            return 0.0
        if type == 'string':
            return ""
        
    
# Example usage
code = [
    {'opcode': 'ASSIGN', 'operands': ['x', 10]},
    {'opcode': 'ASSIGN', 'operands': ['y', 20]},
    {'opcode': 'ADD', 'operands': ['x', 'y', 'z']},
    {'opcode': 'PRINT', 'operands': ['z']},
    {'opcode': 'GOTO', 'operands': [6]},
    {'opcode': 'PRINT', 'operands': ['x']},
]

vm = VirtualMachine(code)
vm.run()