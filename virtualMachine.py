import sys
import re
import copy
import ply.yacc as yacc
import bixoLexer
import ply.lex as lexer
import bixoParser as bixo
import numpy as np
import tensorflow as tf


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
    #mapeo valor de cada func
    for func  in functions_table:
        returnType=functions_table[func]["return_type"]
        returnVar=functions_table[func]["return_value"]
        if(returnType=="int"):
            returnValMem=functions_table[func]["vars_table"]["variables"]["varInt"][returnVar]
            returnValTemp=functions_table[func]["vars_table"]["values"]["varInt"][returnValMem[0]]
            returnTempMem=functions_table[func]["vars_table"]["variables"]["tempInt"][returnValTemp]
            returnVal=functions_table[func]["vars_table"]["values"]["tempInt"][returnTempMem]
            #print("RETURNVAL",returnVal)
            globalHashMap[func]=[globalInt,returnVal]
            globalInt+=1
        elif(returnType=="float"):
            returnValMem=functions_table[func]["vars_table"]["variables"]["varFloat"][returnVar]
            returnValTemp=functions_table[func]["vars_table"]["values"]["varFloat"][returnValMem[0]]
            returnTempMem=functions_table[func]["vars_table"]["variables"]["tempFloat"][returnValTemp]
            returnVal=functions_table[func]["vars_table"]["values"]["tempFloat"][returnTempMem]
            #print("RETURNVAL",returnVal)
            globalHashMap[func]=[globalFloat,returnVal]
            globalFloat+=1

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
                    print("VARMAP Y VALUE",varMap,value)
                    if value in varMap:
                        (mem1, value) = varMap[value]

            funcHashMap[var] = (mem, value)

        resultHashMap[func] = funcHashMap

    return resultHashMap






print("----------------INICIA VM-----------------")
mapeo()
print("HASHMAP ORIGINAL",hashMap)
valueMap=asignar_valores(hashMap)
print("VALORES ASIGNADOS",valueMap)
quads=sQuads.quads
print(sQuads)
switch=0
lArray=[]
arrays={}
lMatrix=[]
auxiliar = []
ordered_values = []
matrixes={}
mRows=0
mColumns=0
s2=0
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
        if(res in arrays):
            print(arrays[res])
        elif(res in matrixes):
            print(matrixes[res])
        else:
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
        toF=getTempValue(arg1)
        if(toF==0 or switch == 1):
            i=res-1
        else:
            switch = 1
    elif(op=="ASSIGNFUNC"):
        val=valueMap["global"][arg1][1]
        #print("ASSIGNFUNC VAL ",val)
        mem=21000
        valueMap[arg2][res]=(mem,val)
        #print (valueMap)

        for value in valueMap[arg2]:
            currVal=valueMap[arg2][value]
            if(currVal[1]==res):
                #print("CURRVAL, RES",currVal, res, "ESTA EN ", value)
                valorTemp=valueMap["global"][arg1][1]
                #print("valorTEMP ES:",valorTemp)
                currValMem=currVal[0]
                valueMap[arg2][value]=(mem, valorTemp)
        #print(valueMap)
        

    elif(op=="ERA"):
        if (res in valueMap["global"]):
            pass
        else:
            print("ERROR NO EXISTE FUNCION A LLAMAR")
            sys.exit()
    elif(op=="PARAM"):
        pass
    elif(op=="GOSUB"):
        #if para saltar goto al main mientras testeo
        if(s2==0):
            i=res-1
        s2=1
    elif(op=="ARRAY"):
        lArray=[]
        #array=np.array()
    elif(op=="ARRAYSTART"):
        pass
        #while
    elif(op=="ARRAYFILL"):
        currVal=valueMap["main"][arg2][1]
        lArray.append(currVal)
    elif(op=="ARRAYEND"):
        arrays[res]=np.array(lArray)
    elif(op=="MATRIX"):
        mRows=arg2
        mColumns=res
        lMatrix=[]
        auxiliar = []
        ordered_values = []
    elif(op=="MATRIXSTART"):
        pass
    elif(op=="MATRIXFILL"):
        pass
        #print(valueMap)
        currVal=valueMap["main"][arg2][1]
        lMatrix.append(currVal)
    elif(op=="MATRIXEND"):
        auxiliar = []
        # Vaciar la pila y almacenar los elementos en la lista auxiliar en orden inverso
        while lMatrix:
            e = lMatrix.pop()
            auxiliar.append(e)
        pass
        for m in range(mRows+1):
            row = []
            for j in range(mColumns+1):
                value = auxiliar.pop()
                row.append(value)
            ordered_values.append(row)
        mat=np.array(ordered_values)
        matrixes[res]=mat
        #print("MATRICES:", matrixes)
        
    #elif(op=="MEAN"):
    #elif(op=="LAYERS"):
    #elif(op=="SEQUENTIAL"):
    #elif(op=="COMPILE"):
    #elif(op=="FIT"):
    #elif(op=="PREDICT"):
    #elif(op=="FIBONACCI"):
    
        

    i+=1
    print("Quad",i,quad)
    #print(i)
    

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


