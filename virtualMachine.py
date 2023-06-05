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


regexTemp=bixo.regexTemp
regexInt=bixo.regexInt
regexFloat=bixo.regexFloat
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
    #print(globalVarTable)
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
        #print(gVari,globalInt,"RESULT",result)
        globalHashMap[gVari]=(globalInt,result)
        globalInt+=1
    #global float
    for gVarf, value in globalVarTable["variables"]["float"].items():
        result=""
        #print(gVarf,globalFloat,"RESULT",result)
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
        #print(func)
        #mapeo varints
        for vari, value in functions_table[func]["vars_table"]["variables"]["varInt"].items():
            result=functions_table[func]["vars_table"]["values"]["varInt"].get(value[0], "")
            #print(vari,localInt,"RESULT",result)
            funcHashMap[vari]=(localInt,result)
            localInt+=1
        #mapeo varfloats
        for varf, value in functions_table[func]["vars_table"]["variables"]["varFloat"].items():
            result=functions_table[func]["vars_table"]["values"]["varFloat"].get(value[0], "")
            #print(varf,localFloat,"RESULT",result)
            funcHashMap[varf]=(localFloat,result)
            localFloat+=1
        #mapeo tempInts
        for tempi, value in functions_table[func]["vars_table"]["variables"]["tempInt"].items():
            result=functions_table[func]["vars_table"]["values"]["tempInt"].get(value, "")
            #print(tempi,tempInt,"RESULT",result)
            funcHashMap[tempi]=(tempInt,result)
            tempInt+=1
        #mapeo tempFloats
        for tempf, value in functions_table[func]["vars_table"]["variables"]["tempFloat"].items():
            result=functions_table[func]["vars_table"]["values"]["tempFloat"].get(value, "")
            #print(tempf,tempFloat,"RESULT",result)
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
                    #print("VARMAP Y VALUE",varMap,value)
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
#print(sQuads)
currFunc="global"
quadCurrFunc=0
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
#################################
#SECCION DE ML:
units=0
#para ciclos
sBools=[]
#para llamadas
sCalls=[]
sParams=[]
sCallFunc=[]



while (i< qCounter):
    quad=sQuads.quads[i]
    #print("CUADRUPLO",quad)
    #print("QUAD POS 0", quad[0])
    op=quad[0]
    arg1=quad[1]
    arg2=quad[2]
    res=quad[3]
    print("Quad",i,quad)
    if(op=="+" or op=="-" or op=="*" or op=="/"):
        if isinstance(arg1, (int, float)):
            val1=arg1
        else:
            val1=valueMap[currFunc][arg1][1]
        if isinstance(arg2, (int, float)):
            val2=arg2
        else:
            val2=valueMap[currFunc][arg2][1]
        if(re.match(regexInt,str(arg1))):
            val1=arg1
        if(op=="+"):
            val=val1+val2
        elif(op=="-"):
            val=val1-val2
        elif(op=="*"):
            val=val1*val2
        elif(op=="/"):
            val=val1/val2
        
        mem=valueMap[currFunc][res][0]
        valueMap[currFunc][res]=(mem,val)
        #print("VAL SUMA VA A ,",val, res)
        #print(valueMap)
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
        else:
            if isinstance(arg1, (int,float)):
                val=arg1
            else:
                val=valueMap[currFunc][arg1][1]

            mem=valueMap[currFunc][res][0]
            valueMap[currFunc][res]=(mem,val)
            #print("aqui a ", res, "le asigno el valor de",mem, val)
            
    elif(op=="=="):
        if(re.match(regexInt,str(arg1))):
            val1=arg1
        else:
            val1=valueMap["main"][arg1][1]
        if(re.match(regexInt,str(arg2))):
            val2=arg2
        else:
            val2=valueMap["main"][arg2][1]
        if(val1==val2):
            sBools.append(1)
        else:  sBools.append(0)
        #("Meti a sBools", sBools)
    elif(op=="!="):
        if(re.match(regexInt,str(arg1))):
            val1=arg1
            #print("VAL1:",val1)
        else:
            val1=valueMap["main"][arg1][1]
        if(re.match(regexInt,str(arg2))):
            val2=arg2
        else:
            val2=valueMap["main"][arg2][1]
        if(val1!=val2):
            sBools.append(1)
        else:  sBools.append(0)
        #print("Meti a sBools", sBools)

    elif(op==">"):
        if(re.match(regexInt,str(arg1))):
            val1=arg1
        else:
            val1=valueMap["main"][arg1][1]
        if(re.match(regexInt,str(arg2))):
            val2=arg2
        else:
            val2=valueMap["main"][arg2][1]
        if(val1>val2):
            sBools.append(1)
        else:  sBools.append(0)
        #print("Meti a sBools", sBools)

    elif(op=="<"):
        if(re.match(regexInt,str(arg1))):
            val1=arg1
        else:
            val1=valueMap["main"][arg1][1]
        if(re.match(regexInt,str(arg2))):
            val2=arg2
        else:
            val2=valueMap["main"][arg2][1]
        if(val1<val2):
            sBools.append(1)
        else:  sBools.append(0)
        #print("Meti a sBools", sBools)

    elif(op=="AND"):
        a2=sBools.pop(-1)
        a1=sBools.pop(-1)
        #print("A1 y A2 EN AND", a1,a2)
        if(a1==1 and a2==1):
            sBools.append(1)
        else: sBools.append(0)
        #print("Meti a sBools", sBools)


    elif(op=="OR"):
        a2=sBools.pop(-1)
        a1=sBools.pop(-1)
        #print("A1 y A2 EN OR", a1,a2)
        if(a1==1 or a2==1):
            sBools.append(1)
        else: sBools.append(0)
        #print("Meti a sBools", sBools)
        
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
        i=res-1
    elif(op=="GOTOF"):
        #print(valueMap)
        toF=sBools.pop()
        #print("TOF ES ", toF)
        #if(toF==0 or switch == 1):
        if(toF==0):
            i=res-1
        #else:
        #    switch = 1
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
    elif(op=="FUNCSTART"):
        currFunc=arg1
        quadCurrFunc=res
        lInt=12000
        lFloat=16000

        while(sParams):
            param=sParams.pop()
            #print("PARAM RECIBIDO", param)
            if(re.match(regexFloat,str(param))):
                for variable, datos in valueMap[currFunc].items():
                    if datos[0] == lFloat:
                        nombre_variable = variable
                        lFloat+=1
                        break
            elif(re.match(regexInt,str(param))):
                for variable, datos in valueMap[currFunc].items():
                    if datos[0] == lInt:
                        nombre_variable = variable
                        lInt+=1
                        break
            
                
            mem=valueMap[currFunc][nombre_variable][0]
            valueMap[currFunc][nombre_variable]=(mem,param)
            #print(nombre_variable,"=",param)



    elif(op=="ERA"):
        pass
        #if (res in valueMap["global"]):
        #    pass
        #else:
        #    print("ERROR NO EXISTE FUNCION A LLAMAR")
        #    sys.exit()
    elif(op=="PARAM"):
        if isinstance(arg1, (int, float)):
            val=arg1
        else:
            val=valueMap[currFunc][arg1][1]
        
        #print("PARAMVALUE=", arg1,val)
        sParams.append(val)
    elif(op=="GOSUB"):
        #if para evitar recursion mientras testeo
        #if(s2==0):
        sCalls.append(i+1)
        sCallFunc.append(currFunc)
        i=res-1

        #s2=1

    elif(op=="FUNCEND"):
        if(res!=None):
            retValue=res

        if(sCalls):
            jump=sCalls.pop()
            f=sCallFunc.pop()
            currFunc=f
            i=jump-1

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
    elif(op=="MEAN"):
        if(arg1 in matrixes):
            mat=matrixes[arg1]
            mean=np.mean(mat)
            print("Mean de",arg1,"=",mean)
        elif(arg1 in arrays):
            arr=arrays[arg1]
            mean=np.mean(arr)
            print("Mean de",arg1,"=",mean)
    elif(op=="MATRIXMULT"):
        if(arg1 in matrixes):
            mat1=np.array(matrixes[arg1])
        else: 
            print("ERROR NO EXISTE MATRIX", arg1)
            sys.exit()
        if(arg2 in matrixes):
            mat2=np.array(matrixes[arg2])
        else: 
            print("ERROR NO EXISTE MATRIX", arg2)
            sys.exit()
        mult=np.matmul(mat1,mat2)
        print("MULTIPLICACION DE",arg1,"*",arg2,"ES =",mult)
    elif(op=="LAYERS"):
        capa = tf.keras.layers.Dense(units=arg1, input_shape=[1])
    elif(op=="SEQUENTIAL"):
        modelo = tf.keras.Sequential([capa])
    elif(op=="COMPILE"):
        modelo.compile(
            optimizer = tf.keras.optimizers.Adam(arg1),
            loss='mean_squared_error'
        )
    elif(op=="FIT"):
        print("Comenzando entrenamiento...")
        arr1=arrays[arg1]
        arr2=arrays[arg2]
        historial = modelo.fit(arr1, arr2, epochs=res, verbose=False)
        print("Modelo entrenado!")
    elif(op=="PREDICT"):
        print("Hagamos una predicción!")
        resultado = modelo.predict([arg1])
        print("El resultado es: "+ str(resultado))
    elif(op=="FIBONACCI"):
        n=arg1
        if n<=0:
            print("ERROR NUMERO DEBE SER MAYOR A 0")
            sys.exit()
        elif n == 1:
            print(0)
        else:
            a, b = 0, 1
            print(a)  
            print(b)  
            for _ in range(2, n):
                a, b = b, a + b
                print(b)  
    elif(op=="FACTORIAL"):    
        n=arg1
        fact = 1
        for k in range(1, n + 1):
            fact *= k
        print("FACTORIAL DE",n,"=",fact)

    i+=1
    
    #print(i)
    

print(valueMap)



    



