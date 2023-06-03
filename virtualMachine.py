import sys
import re
import copy
import ply.yacc as yacc
import bixoLexer
import ply.lex as lexer
import bixoParser as bixo


#importa data de parser
functions_table=bixo.functions_table
sQuads=bixo.quadGen
gen_quad = bixo.quadGen.gen_quad
qCounter = bixo.qCounter
globalVarTable = bixo.var_table["global"]

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


globalInt = 4000
globalFloat = 8000 
localInt = 12000
localFloat = 16000
tempInt = 20000
tempFloat = 24000
tempBool = 28000

regexTemp=bixo.regexTemp
#para imprimir quad en posicion 1
#print ("QUADGEN",sQuads.quads[1])

#var que almacena todos los quads = sQuads
#sQuads los imprime enumerados con formato
#sQuads.quads los imprime en una lista (que se puede contabilizar)

hashMap={}

def getFuncVar(var):
    for func in functions_table:
        #print ("FUNC ES:",func)
        if ((var in functions_table[func]["vars_table"]["variables"]["varInt"]) or (var in functions_table[func]["vars_table"]["variables"]["varFloat"])):
            #print("la var", var, "existe en ", func)
            return (func)
    print("ERROR NO EXISTE VARIABLE")    
    sys.exit()

def mapeo():
    global localInt, localFloat, tempInt, tempFloat,globalInt, globalFloat
    print(globalVarTable)
    globalHashMap={}
    #mapeo globales
    #global int
    for gVari, value in globalVarTable["variables"]["int"].items():
        result=""
        print(gVari,globalInt,"RESULT",result)
        globalHashMap[gVari]=(globalInt,result)
        globalInt+=1
    #global float
    for gVarf, value in globalVarTable["variables"]["float"].items():
        result=""
        print(gVarf,globalFloat,"RESULT",result)
        globalHashMap[gVarf]=(globalFloat,result)
        globalFloat+=1
    hashMap["global"]=globalHashMap
    
    #mapeo locales
    for func in functions_table:
        funcHashMap={}
        globalInt = 4000
        globalFloat = 8000 
        localInt = 12000
        localFloat = 16000
        tempInt = 20000
        tempFloat = 24000
        print(func)
        #mapeo varints
        for vari, value in functions_table[func]["vars_table"]["variables"]["varInt"].items():
            result=functions_table[func]["vars_table"]["values"]["varInt"].get(value[0], "")
            print(vari,localInt,"RESULT",result)
            funcHashMap[vari]=(localInt,result)
            localInt+=1
        #mapeo varfloats
        for varf, value in functions_table[func]["vars_table"]["variables"]["varFloat"].items():
            result=functions_table[func]["vars_table"]["values"]["varFloat"].get(value[0], "")
            print(varf,localFloat,"RESULT",result)
            funcHashMap[varf]=(localFloat,result)
            localFloat+=1
        #mapeo tempInts
        for tempi, value in functions_table[func]["vars_table"]["variables"]["tempInt"].items():
            result=functions_table[func]["vars_table"]["values"]["tempInt"].get(value, "")
            print(tempi,tempInt,"RESULT",result)
            funcHashMap[tempi]=(tempInt,result)
            tempInt+=1
        #mapeo tempFloats
        for tempf, value in functions_table[func]["vars_table"]["variables"]["tempFloat"].items():
            result=functions_table[func]["vars_table"]["values"]["tempFloat"].get(value, "")
            print(tempf,tempFloat,"RESULT",result)
            funcHashMap[tempf]=(tempFloat,result)
            tempFloat+=1

        hashMap[func]=funcHashMap
    #print(hashMap)


def getTempValue(temp):
    for func in valueMap:
        for var, val in valueMap[func].items():
            if(temp==var):
                return val[1]


def asignar_valores(hashMap):
    resultHashMap = {}
    #itera en cada funcion
    for func, varMap in hashMap.items():
        funcHashMap = {}
        #revisa cada valorr y si es un temp lo asigna a su valor
        for var, (mem, value) in varMap.items():
            #if (re.match(regexTemp,var)):
                #omito datos temporales
            #    continue
            if isinstance(value, (int, float)):
                #omito numeros
                pass
            else:
                if (re.match(regexTemp,value)):
                    #almaceno valor de temporal en la variable
                    (mem1, value) = varMap[value]

            funcHashMap[var] = (mem, value)

        resultHashMap[func] = funcHashMap

    return resultHashMap






print("----------------INICIA VM-----------------")
mapeo()
valueMap=asignar_valores(hashMap)
print("HASHMAP ORIGINAL",hashMap)
print("VALORES ASIGNADOS",valueMap)
quads=sQuads.quads
print(sQuads)
switch=0
i=0
#while i < qCounter:
#    if switch==10:
#        break
#    if i == 5:
#        i = 0  # Salta a la iteración 10
#        continue  # Salta al siguiente ciclo del bucle
#    elif i == 15:
#        break  # Termina el bucle
#    print(i)
#    i += 1
#    switch+=1


while (i< qCounter):
    quad=sQuads.quads[i]
    #print("CUADRUPLO",quad)
    #print("QUAD POS 0", quad[0])
    op=quad[0]
    arg1=quad[1]
    arg2=quad[2]
    res=quad[3]
    if(op=="+" or op=="-" or op=="*" or op=="/"):
        pass
    elif(op=="="):
        #para asignar variables globales
        if(res in valueMap["global"]):
            val=arg1
            mem=valueMap["global"][res][0]
            if isinstance(val, (int, float)):
                #omito numeros
                pass
            else:
                if (re.match(regexTemp,val)):
                   print("ERROR asignar temporal a global")
                   sys.exit()
            valueMap["global"][res]=(mem,val)
    elif(op=="print"):
        func=getFuncVar(res)
        val=valueMap[func][res][1]
        print(val)
    elif(op=="read"):
        func=getFuncVar(res)
        val=input()
        mem=valueMap[func][res][0]
        valueMap[func][res]=(mem,val)
    elif(op=="GOTO"):
        #if para saltar goto al main mientras testeo
        if(i>0):
            i=res-1
    elif(op=="GOTOF"):
        print("ENTRO GOTOF")
        toF=getTempValue(arg1)
        print("TOF ES: ",toF)
        if(toF==0):
            i=res-1
        else:
            pass
        

    i+=1
    print(quad)
    print(i)
    

print(valueMap)

#for i in range(qCounter):
#    print(i)
#    quad=sQuads.quads[i]
#    print("CUADRUPLO",quad)
#    print("QUAD POS 0", quad[0])
#    op=quad[0]
#    arg1=quad[1]
#    arg2=quad[2]
#    res=quad[3]
#    if(op=="+" or op=="-" or op=="*" or op=="/"):
#        pass
#    elif(op == "="):
#        func=getFuncVar(res)
#        if (res in functions_table[func]["vars_table"]["variables"]["varInt"]):
#            memoria=functions_table[func]["vars_table"]["variables"]["varInt"][res]
#            value = functions_table[func]["vars_table"]["values"]["varInt"][memoria[0]]
#        elif(res in functions_table[func]["vars_table"]["variables"]["varFloat"]):
#            memoria=functions_table[func]["vars_table"]["variables"]["varFloat"][res]
#            value = functions_table[func]["vars_table"]["values"]["varFloat"][memoria[0]]
#
#
#    if(op == "print"):
#        func=getFuncVar(res)
#        if (res in functions_table[func]["vars_table"]["variables"]["varInt"]):
#            memoria=functions_table[func]["vars_table"]["variables"]["varInt"][res]
#            value = functions_table[func]["vars_table"]["values"]["varInt"][memoria[0]]
#        elif(res in functions_table[func]["vars_table"]["variables"]["varFloat"]):
#            memoria=functions_table[func]["vars_table"]["variables"]["varFloat"][res]
#            value = functions_table[func]["vars_table"]["values"]["varFloat"][memoria[0]]
#        print(value)
#    elif(op=="read"):
#        func=getFuncVar(res)
#        value=input()
#        if (res in functions_table[func]["vars_table"]["variables"]["varInt"]):
#            memoria=functions_table[func]["vars_table"]["variables"]["varInt"][res]
#            functions_table[func]["vars_table"]["values"]["varInt"][memoria[0]]=value
#        elif(res in functions_table[func]["vars_table"]["variables"]["varFloat"]):
#            memoria=functions_table[func]["vars_table"]["variables"]["varFloat"][res]
#            functions_table[func]["vars_table"]["values"]["varFloat"][memoria[0]]=value
#        print(functions_table)
#        
#
#    elif(op == "GOTO"):
#        print("Hay goto aca")
#        i = res
#        
#        print(i,res)
#        print("GOTO NOS LLEVA A",res)
#       
#    elif(op == "era"):
#        print("Hay goto aca")
#    #if(op == "goto" or "GOTO"):
#     #   print("Hay goto aca")
    #if(op == "read"):
    #    print("hay read aca")
    #    print(res)
        



#def run(self):
    #memoria del main
   # self.sCall.append(mainMem)
    #run quads

    


#def runQuads(self, quad):
#        op, arg1, arg2, res = quad
#    if op == "goto":
#        self.goto(res)
#    elif op == "=":
#        self.assign(arg1, res)
#    elif op in ["+", "-", "/", "*", "&&", "||", ">", "<", ">=", "<=", "==", "!="]:
#        self.operation(op, arg1, arg2, res)
#    elif op == "print":
#        self.print(arg1)
#    elif op == "gotoF":
#        self.gotoF(arg1, res)
#    elif op == "era":
#        self.era(arg1)
##    elif op == "parameter":
##        self.param(arg1)
##    elif op == "gosub":
##        self.gosub(res)
#
#    def goto(self, arg1, res):
#        #asignamos el num de quad en res
#        self.iIp[-1] = res
#    
#def assign(self, arg1, res):
#    value = self.get_value(arg1)
#    self.set_value(res, value)
#
#def operation(self, op, arg1, arg2, res):
#    value1 = self.get_value(arg1)
#    value2 = self.get_value(arg2)
#
#    if op == "+":
#        result = value1 + value2
#    elif op == "-":
#        result = value1 - value2
#    elif op == "*":
#        result = value1 * value2
#    elif op == "/":
#        result = value1 / value2
#    elif op == "&&":
#        result = value1 and value2
#    elif op == "||":
#        result = value1 or value2
#    elif op == ">":
#        result = value1 > value2
#    elif op == "<":
#        result = value1 < value2
#    elif op == ">=":
#        result = value1 >= value2
#    elif op == "<=":
#        result = value1 <= value2
#    elif op == "==":
#        result = value1 == value2
#    elif op == "!=":
#            result = value1 != value2
#
#    self.set_value(res, result)
#
#def print(self, arg1):
#    value = self.get_value(arg1)
#    print(value)
#
#def gotoF(self, arg1, res):
#    value = self.get_value(arg1)
#    if not value:
#        self.sIp[-1] = res


