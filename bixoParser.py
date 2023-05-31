import copy
import sys
import re
import ply.yacc as yacc
import bixoLexer
from cuboSemantico import semantic_cube
from bixoLexer import tokens


class QuadGenerator:
    def __init__(self):
        self.quads = []

    def gen_quad(self, op, arg1, arg2, res):
        quad = [op, arg1, arg2, res]
        self.quads.append(quad)

    def __str__(self):
        result = ""
        for i, quad in enumerate(self.quads):
            result += f"{i}: {QuadGenerator.format_quad(quad)}\n"
        return result

    @staticmethod
    def format_quad(quad):
        return f'[{quad[0]}][{quad[1]}][{quad[2]}][{quad[3]}]'


var_table = {
    "global": {
        "variables": {
            "int": {},
            "float": {}
        },
        "counters": {
            "int": 0,
            "float": 0
        },
        "values": {
            "int": {},
            "float": {}
        }
    }
}

local_var_table = {
    "function": "",
    "variables": {
        "varInt": {},
        "varFloat": {},
        "tempInt":{},
        "tempFloat":{}
    },
    "counters": {
        "int": 0,
        "float": 0
    },
    "values": {
        "varInt": {},
        "varFloat": {},
        "tempInt": {},
        "tempFloat": {}
    }
}

#Funcion que agrega variable local a tabla y asigna memoria
def add_var_local(name, type, currFunc):
     if(type=="int"):
        var_mem = local_var_table["counters"][type] + localInt
        local_var_table["variables"]["varInt"][name] = [var_mem] 
     elif(type=="float"):
        var_mem = local_var_table["counters"][type] + localFloat
        local_var_table["variables"]["varFloat"][name] = [var_mem] 
     #print("memoria:",var_mem)
     local_var_table["function"] = currFunc
     local_var_table["counters"][type] += 1
          
     sTypes.append(type)

#Funcion que agrega variable global a tabla y asigna memoria
def add_var_global(name, type):
     if(type=="int"):
        var_mem = var_table["global"]["counters"][type] + globalInt
     elif(type=="float"):
        var_mem = var_table["global"]["counters"][type] + globalFloat
     #print("memoria:",var_mem)
     var_table["global"]["counters"][type] += 1
     var_table["global"]["variables"][type][name] = [var_mem]      
     sTypes.append(type)

#Funcion que hace una copia de la tabla actual y la mete a el array de tablas locales
def copy_var_local():
    local_var_table_copy = copy.deepcopy(local_var_table)
    global localArray
    localArray.append(local_var_table_copy)

#Funcion que agrega el valor de una variable y su espacio de memoria a la tabla
def add_local_var_value(variable_type,direccion_memoria, var_assign):
    if variable_type=="int":
        local_var_table["values"]["varInt"][direccion_memoria]=var_assign
    elif variable_type=="float":
        local_var_table["values"]["varFloat"][direccion_memoria]=var_assign
    

#Funcion que crea temporales
def getTemp():
    global tempCounter
    temp = "t" + str(tempCounter)
    tempCounter += 1
    sTemp.append(temp)
    return temp

tokens=bixoLexer.tokens

#para if
sBools=[]
hayElse=0
#almacena los tipos de variables
sTypes = [] 
#pila saltos
sJumps = []
qCounter=0
#counter y stack de temporales
tempCounter=1
sTemp=[]
#pila operandos
sOperands = []
#pila operadores
sOperators = []
#almacena el scope actual
scope="global"
#pilavars
sVars=[]
quadGen=QuadGenerator()
#pila de cuadruplos = quadGen.quads
#para imprimir cuadruplos : print(str(quadGen))
#current function
currFunc="ejemplo1"
##########################################################CounterInicioFunc y CurrFuncStartAddress son lo mismo 
currFuncStartAddress=0
currFuncType=""
mainStartAddress=0
localArray=[]
localTypes=[]
contLocal=-1
regexInt=r'\d+'
regexFloat=r'\d+\.\d+'
regexTemp = r't\d+'
paramCounter=1
sCallParams=[]
counterInicioFunc=0
#Counters de temporales
tempCounterInt=0
tempCounterFloat=0
#pilatipos cubo semantico
sTipos=[]
sParams=[]
sReturns=[]
tempIntMemory=20000
tempFloatMemory=24000
#para print
sPrints=[]
currBool=None
#para arrays
cArrayValues=0
sArrayValues=[]
#para matrices
sMatrixSize=[]
sMatrixStart=[]
matrixCounter=0
sMatrixValues=[]
mValues=0


functions_table = {}

def add_function(name, return_type, return_value, start_address, varInt, varFloat, tempInt, tempFloat,local_table):
    functions_table[name] = {
        "return_type": return_type,
        "return_value": return_value,
        "start_address": start_address,
        "resources": {
            "varInt": varInt,
            "varFloat": varFloat,
            "tempInt": tempInt,
            "tempFloat": tempFloat
        },
        "vars_table": local_table
    }

#para acceder a tabla de funciones de alguna funcion
# vars_table = functions_table[function_name]["vars_table"]

def limpiaDatos():
    local_var_table["function"]=""
    local_var_table["variables"]["varInt"]={}
    local_var_table["variables"]["varFloat"]={}
    local_var_table["variables"]["tempInt"]={}
    local_var_table["variables"]["tempFloat"]={}
    local_var_table["counters"]["int"]=0
    local_var_table["counters"]["float"]=0
    local_var_table["values"]["varInt"]={}
    local_var_table["values"]["varFloat"]={}
    local_var_table["values"]["tempInt"]={}
    local_var_table["values"]["tempFloat"]={}
    #print("LOCAL VAR TABLE DESPUES DE EMPTY: ",local_var_table)

def clearMatrixValues():
    sMatrixSize=[]
    sMatrixStart=[]
    matrixCounter=0
    sMatrixValues=[]
    mValues=0


def checkTable():
    return(local_var_table)

def getFuncReturn(func_name):
    funcReturn = functions_table[func_name]["return_value"]
    return funcReturn

def varExist(var):
    if((var in (var_table["global"]["variables"]["int"]) or (var in var_table["global"]["variables"]["float"])) or (var in (local_var_table["variables"]["varInt"]) or (var in local_var_table["variables"]["varFloat"]))):
        return 1
    else: print("ERROR LA VARIABLE",var, "NO EXISTE")
    sys.exit()

    

########################--Rangos de memoria--############################

globalInt = 4000
globalFloat = 8000 
localInt = 12000
localFloat = 16000
tempInt = 20000
tempFloat = 24000
tempBool = 28000
#tempPointer = 28000
#consInt = 32000
#consFloat = 36000
#consString = 40000



precedence = (
   #Checar que precences faltan (left o right)
    ('left','LT','LTE','GT','GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'EQUAL', 'DIFF'),
    ('left','LPAREN','RPAREN'),
    ('left','LBRACE','RBRACE'),
    ('left','LBRACKET','RBRACKET'),
)



#REGLAS ANALIZADOR SINTÁCTICO
    


  ### REVISAR DECLARACION DE MATRIZ#####  


def p_program(p):
    '''program : PROGRAM gotomain ID SEMICOLON decvar modules mainfunction'''
    print("Nombre del programa:", p[3])
    print("TABLA DE FUNCIONES", functions_table)
    print("Cuadruplos: ",str(quadGen))
    print("Counter de cuadruplos: ", qCounter)
    print("Tabla de variables globales", var_table)

def p_gotomain(p):
    '''gotomain : '''
    global qCounter
    #genera cuadruplo goto main
    quadGen.gen_quad("GOTO",None,None,"main")
    #añade valor a tabla de constantes
    qCounter+=1

def p_decvar(p):
    '''decvar : VAR decvarp
              | VAR decvarp decvar
              |'''
    global scope,  sParams
    scope="local"
    #p[0]=p[2]

def p_decvarp(p):
    '''decvarp : type decvarpp SEMICOLON'''

    #print("EL SCOPE ES", scope)

    var_type = p[1]
    var_name = p[2]

    if scope == "local":
        #print("pilavars: ", sVars)
        for vars in sVars:
        #Revisa que la variable no exista ya en la tabla y que no sea un parametro(porque solia marcar error para parametros)
            if (((vars in local_var_table["variables"]["varInt"]) or (vars in local_var_table["variables"]["varFloat"])) and (vars not in sParams)):
                #antes de implementar este error checar la logica 
                print(vars,"ERROR YA EXISTE")
            else:
                add_var_local(vars,var_type,currFunc) 
        #copy_var_local()

    if scope == "global":
        #print("pilavars: ", sVars)
        #Revisa que la variable no exista ya en la tabla 
        for vars in sVars:
            if (vars in var_table["global"]["variables"]["float"]) or (vars in var_table["global"]["variables"]["float"]):
                #antes de implementar este error checar la logica 
                print(vars,"ERROR YA EXISTE ")
            else:
                if var_type == "int":
                     add_var_global(vars,var_type)
                elif var_type == "float":
                    add_var_global(vars,var_type)

    sVars.clear()
    sTypes.clear()
    


def p_decvarpp(p):
    '''decvarpp : ID COMMA decvarpp
                | ID'''
    if len(p)==2:
        sVars.append(p[1])
        p[0]=p[1]
    else:
        sVars.append(p[1])
        p[0]=p[3]
    
def p_type(p):
    '''type : INT
            | FLOAT'''
    p[0] = p[1]
            
def p_function(p):
    '''function : FUNCTION decfunctype decfunc LPAREN param RPAREN LBRACE body RETURN exp SEMICOLON RBRACE'''
    global localArray, currFunc, functions_table, counterInicioFunc, tempCounterFloat, tempCounterInt
    func_type=p[2]
    return_value=p[10]
    copy_var_local()
    #Revisa si existe la función
    if currFunc in functions_table: 
        print("ERROR YA EXISTE ESA FUNCION")
    else:
        #Revisa que si haya algo en su tabla de variables locales
        if(len(localArray)!=0):
            func_var_table=localArray.pop()
        else: func_var_table=local_var_table
        func_var_table_copy = copy.deepcopy(func_var_table)
        #print("FUNC VAR TABLE ES: ",func_var_table_copy)
        varCounterFloat=func_var_table_copy['counters']['float']
        varCounterInt=func_var_table_copy['counters']['int']
        add_function(currFunc, func_type, return_value,counterInicioFunc, varCounterInt,varCounterFloat, tempCounterInt, tempCounterFloat, func_var_table_copy)
        #Reseteo counters despues de guardar para usarlos en la prox funcion
        tempCounterFloat=0
        tempCounterInt=0
        #print("TABLA DE FUNCIONES", functions_table)

def p_decfunctype(p):
    '''decfunctype : type'''
    global currFuncType
    currFuncType=p[1]
    p[0]=p[1]

def p_decfunc(p):
    '''decfunc : ID'''
    limpiaDatos()
    global currFunc,currFuncStartAddress,counterInicioFunc, sParams, tempCounter, sCallParams, tempIntMemory, tempFloatMemory
    currFunc=p[1]
    currFuncStartAddress=qCounter
    counterInicioFunc=qCounter
    #reinicio pila de params y tempCounter para nueva funcion 
    sParams=[]
    sCallParams=[]
    clearMatrixValues()
    tempCounter=1
    tempIntMemory=20000
    tempFloatMemory=24000
    print("CURRENT FUNC", currFunc)

    
def p_voidfunction(p):
    '''voidfunction : FUNCTION VOID decfunc LPAREN param RPAREN LBRACE body RBRACE'''
    global localArray, currFunc, functions_table,counterInicioFunc, tempCounterInt, tempCounterFloat
    func_type=p[2]
    #Revisa si existe la función
    if currFunc in functions_table: 
        print("ERROR YA EXISTE ESA FUNCION")
    else:
        #Revisa que si haya algo en su tabla de variables locales
        if(len(localArray)!=0):
            func_var_table=localArray.pop()
        else: func_var_table=local_var_table
        func_var_table_copy = copy.deepcopy(func_var_table)
        varCounterFloat=func_var_table_copy['counters']['float']
        varCounterInt=func_var_table_copy['counters']['int']
        add_function(currFunc, func_type, None, counterInicioFunc, varCounterInt, varCounterFloat, tempCounterInt, tempCounterFloat, func_var_table_copy)
        #Reseteo counters despues de guardar para usarlos en la prox funcion
        tempCounterFloat=0
        tempCounterInt=0
        #print("TABLA DE FUNCIONES", functions_table)



def p_decfuncmain(p):
    '''decfuncmain : '''
    limpiaDatos()
    global currFunc, tempCounter, sParams, mainStartAddress, sCallParams, tempIntMemory, tempFloatMemory
    currFunc="main"
    mainStartAddress=qCounter
    #reinicio pila de params y tempCounter para nueva funcion 
    sParams=[]
    sCallParams=[]
    clearMatrixValues()
    tempCounter=1
    tempIntMemory=20000
    tempFloatMemory=24000
    #Relleno el quadruplo 1 con la localizacion del main
    quadGen.quads[0] = ("GOTO",None,None, mainStartAddress)
    print("CURRENT FUNC", currFunc)


def p_mainfunction(p):
    '''mainfunction : MAIN decfuncmain LPAREN RPAREN LBRACE body RBRACE'''
    global localArray, currFunc, functions_table,mainStartAddress, tempCounterInt, tempCounterFloat
    func_type="main"
    #Revisa si existe la función
    if currFunc in functions_table: 
        print("ERROR YA EXISTE MAIN")
    else:
        #Revisa que si haya algo en su tabla de variables locales
        if(len(localArray)!=0):
            func_var_table=localArray.pop()
        else: func_var_table=local_var_table
        func_var_table_copy = copy.deepcopy(func_var_table)
        varCounterFloat=func_var_table_copy['counters']['float']
        varCounterInt=func_var_table_copy['counters']['int']
        add_function(currFunc, func_type, None, (mainStartAddress), varCounterInt, varCounterFloat, tempCounterInt, tempCounterFloat, func_var_table_copy)
        #Reseteo counters despues de guardar para usarlos en la prox funcion
        tempCounterFloat=0
        tempCounterInt=0
        #print("TABLA DE FUNCIONES", functions_table)


def p_modules(p):
    '''modules : function modules
               | voidfunction modules
               | function
               | voidfunction'''
    global currFuncType
    currFuncType=""
    if(len(p)==2):
        p[0]=p[1]
    
    
def p_body(p):
    '''body : decvar statements body
            | statements body
            | decvar
            | '''
    
#checar si se puede vacio o epsilon
def p_param(p):
    '''param : type ID
             | type ID COMMA param
             |'''
    global sVars, sTypes, local_var_table
    if len(p)>1:
        sTypes.append(p[1])
        #sVars.append(p[2])
        sParams.append(p[2])
        add_var_local(p[2],p[1],currFunc) 
        #print("LOCAL VAR TABLE",local_var_table)


#AQUI FALTA EL DEL SEGUNDO     
def p_exp(p):
    '''exp : texp 
           | texp OR exp'''
    global qCounter, tempIntMemory, tempCounterInt
    if len(p) == 2:
        p[0]=p[1]
    elif len(p) == 4:
        mem1=local_var_table["variables"]["tempInt"][p[1]]
        mem2=local_var_table["variables"]["tempInt"][p[3]]
        print(p[1],p[2],p[3])
        print("mem1", mem1)
        print("mem2", mem2)
        val1=local_var_table["values"]["tempInt"][mem1]
        val2=local_var_table["values"]["tempInt"][mem2]
        print("val1", val1)
        print("val2", val2)
        print(local_var_table)
        if (val1==1 or val2==1):
            argfinal=1
        else: argfinal=0
        temp=getTemp()
        local_var_table["variables"]["tempInt"][temp]=tempIntMemory
        local_var_table["values"]["tempInt"][tempIntMemory]=argfinal
        quadGen.gen_quad("OR", p[1], p[3], temp)
        qCounter+=1
        tempIntMemory+=1
        tempCounterInt+=1
        p[0]=temp

#AQUI FALTA EL DEL SEGUNDO 
def p_texp(p):
    '''texp : gexp 
            | gexp AND texp'''
    global qCounter, tempIntMemory, tempCounterInt
    if len(p) == 2:
        p[0]=p[1]
    elif len(p) == 4:
        mem1=local_var_table["variables"]["tempInt"][p[1]]
        mem2=local_var_table["variables"]["tempInt"][p[3]]
        print(p[1],p[2],p[3])
        print("mem1", mem1)
        print("mem2", mem2)
        val1=local_var_table["values"]["tempInt"][mem1]
        val2=local_var_table["values"]["tempInt"][mem2]
        print("val1", val1)
        print("val2", val2)
        print(local_var_table)
        if (val1==1 and val2==1):
            argfinal=1
        else: argfinal=0
        temp=getTemp()
        local_var_table["variables"]["tempInt"][temp]=tempIntMemory
        local_var_table["values"]["tempInt"][tempIntMemory]=argfinal
        quadGen.gen_quad("AND", p[1], p[3], temp)
        qCounter+=1
        tempIntMemory+=1
        tempCounterInt+=1
        p[0]=temp

def p_gexp(p):
    '''gexp : mexp 
            | mexp gexpp mexp'''
    global qCounter, tempCounterInt, tempIntMemory, sTipos
    if len(p) == 2:
        p[0]=p[1]
    elif len(p) == 4:
        arg1=None
        arg2=None
        argfinal=None
        var1=None
        var2=None
        resInt=None
        resFloat=None
        memoriaVar1=0
        memoriaVar2=0
        tipo2=sTipos.pop()
        tipo1=sTipos.pop()
        print(tipo1,tipo2)
        comp=p[2]
        sTipos.append("int")
        #guardo el valor de su temp
        temp=getTemp()
        local_var_table["variables"]["tempInt"][temp]=tempIntMemory
        tempIntMemory+=1
        tempCounterInt+=1


        #reviso si lo que recibi ya es un numero
        if re.match(regexInt, str(p[1])):
            arg1=p[1]

        elif re.match(regexFloat, str(p[1])):
            arg1=p[1]

        if re.match(regexInt, str(p[3])):
            arg2=p[3]

        elif re.match(regexFloat, str(p[3])):
            arg2=p[3]

        #si es una variable busco su temporal
        if (var1==None and arg1==None):
            while (memoriaVar1<20000):
                if tipo1=="int":
                    #memoria=local_var_table["variables"]["tempInt"][p[1]]
                    memoriaVar1=local_var_table["variables"]["varInt"][p[1]]
                    memoriaVar1=memoriaVar1[0]
                    #print(memoriaVar1)
                    var1=local_var_table["values"]["varInt"][memoriaVar1]
                    #print("var1",var1)
                    memoriaVar1=local_var_table["variables"]["tempInt"][var1]
                    #print("MEMORIA DE temp",memoriaVar1)
                elif tipo1=="float":
                    memoriaVar1=local_var_table["variables"]["varFloat"][p[1]]
                    memoriaVar1=memoriaVar1[0]
                    var1=local_var_table["values"]["varFloat"][memoriaVar1]
                    memoriaVar1=local_var_table["variables"]["tempFloat"][var1]

        if (var2==None and arg2==None):
            while (memoriaVar2<20000):
                if tipo2=="int":
                    memoriaVar2=local_var_table["variables"]["varInt"][p[3]]
                    memoriaVar2=memoriaVar2[0]
                    var2=local_var_table["values"]["varInt"][memoriaVar2]
                    memoriaVar2=local_var_table["variables"]["tempInt"][var2]
                elif tipo2=="float":
                    memoriaVar2=local_var_table["variables"]["varFloat"][p[3]]
                    memoriaVar2=memoriaVar2[0]
                    var2=local_var_table["values"]["varFloat"][memoriaVar2]
                    memoriaVar2=local_var_table["variables"]["tempFloat"][var2]

        #busco el valor de su temp
        if arg1==None:
            if tipo1=="int":
                memoria=memoriaVar1
                arg1=local_var_table["values"]["tempInt"][memoria]
                #print("EL ARG 1 ES ",arg1)
                p[0]=arg1
            elif tipo1=="float":
                memoria=memoriaVar1
                arg1=local_var_table["values"]["tempFloat"][memoria]

        if arg2==None:
            if tipo2=="int":
                memoria=memoriaVar2
                arg2=local_var_table["values"]["tempInt"][memoria]
            elif tipo2=="float":
                memoria=memoriaVar2
                arg2=local_var_table["values"]["tempFloat"][memoria]

        memoria=local_var_table["variables"]["tempInt"][temp]

        if comp=="<":
            #primero agarro valor de primer argumento (si es que no es un numero)
            argfinal = 1 if arg1 < arg2 else 0
            local_var_table["values"]["tempInt"][memoria]=argfinal
            quadGen.gen_quad("<", p[1], p[3], temp)
            qCounter+=1
            p[0]=temp
        elif comp==">":
            argfinal = 1 if arg1 > arg2 else 0
            local_var_table["values"]["tempInt"][memoria]=argfinal
            quadGen.gen_quad(">", p[1], p[3], temp)
            qCounter+=1
            p[0]=temp
        elif comp=="==":
            argfinal = 1 if arg1 == arg2 else 0
            print(local_var_table)
            local_var_table["values"]["tempInt"][memoria]=argfinal
            quadGen.gen_quad("==", p[1], p[3], temp)
            qCounter+=1
            p[0]=temp
        elif comp=="!=":
            argfinal = 1 if arg1 != arg2 else 0
            local_var_table["values"]["tempInt"][memoria]=argfinal
            quadGen.gen_quad("!=", p[1], p[3], temp)
            qCounter+=1
            p[0]=temp
        print ("EL RESULTADO DEL IF ES:", argfinal)
        #print("p[0]:",temp)

def p_gexpp(p):
    '''gexpp : LT
             | GT
             | IFEQUAL
             | DIFF'''
    p[0]=p[1]
             
def p_mexp(p):
    '''mexp : t
            | mexp PLUS t
            | mexp MINUS t'''
    if len(p) == 2:
        p[0]=p[1]
    elif len(p)==4:
        global qCounter, tempCounterFloat, tempCounterInt, sTipos, tempIntMemory, tempFloatMemory
        temp = getTemp()
        tipo2=sTipos.pop()
        tipo1=sTipos.pop()
        resambos=None
        res1=None
        res2=None
        #print(local_var_table)

        #print("cuadruplo de ",p[1],p[2],p[3])
        #print("temp actual", temp)
        

        #guardo el valor de su temp
        #print(temp)
        tipo_resultado = semantic_cube[tipo1][p[2]][tipo2]
        sTipos.append(tipo_resultado)
        #print("tipo resultado:",tipo_resultado)
        if (tipo_resultado=="int"):
            local_var_table["variables"]["tempInt"][temp]=tempIntMemory
            tempIntMemory+=1
            tempCounterInt+=1
        elif (tipo_resultado=="float"):
            local_var_table["variables"]["tempFloat"][temp]=tempFloatMemory
            tempFloatMemory+=1
            tempCounterFloat+=1

        
###############Revisan si el parametro que se recibe ya es un numero
        if re.match(regexInt, str(p[1])):
            res1=p[1]

        elif re.match(regexFloat, str(p[1])):
            res1=p[1]

        if re.match(regexInt, str(p[3])):
            res2=p[3]

        elif re.match(regexFloat, str(p[3])):
            res2=p[3]
#########################################
##############Si no es un numero entonces buscan el valor del temp
        #print("res1",res1)
        #print("res2",res2)
        if res1==None:
            if tipo1=="int":
                memoria=local_var_table["variables"]["tempInt"][p[1]]
                res1=local_var_table["values"]["tempInt"][memoria]
            elif tipo1=="float":
                memoria=local_var_table["variables"]["tempFloat"][p[1]]
                res1=local_var_table["values"]["tempFloat"][memoria]

        if res2==None:
            if tipo2=="int":
                memoria=local_var_table["variables"]["tempInt"][p[3]]
                res2=local_var_table["values"]["tempInt"][memoria]
            elif tipo2=="float":
                memoria=local_var_table["variables"]["tempFloat"][p[3]]
                res2=local_var_table["values"]["tempFloat"][memoria]
############################################
        
        #print("VOY A HACER ",res1,p[2],res2)
        #Aqui hago la suma como tal y genero cuadruplos
        if tipo_resultado=="int":
            memoria=local_var_table["variables"]["tempInt"][temp]
            
            if p[2]=="+":
                resambos=res1+res2
                local_var_table["values"]["tempInt"][memoria]=resambos
                quadGen.gen_quad("+", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
            elif p[2]=="-":
                resambos=res1-res2
                local_var_table["values"]["tempInt"][memoria]=resambos
                quadGen.gen_quad("-", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
        elif tipo_resultado=="float":
            memoria=local_var_table["variables"]["tempFloat"][temp]
            
            if p[2]=="+":
                resambos=res1+res2
                local_var_table["values"]["tempFloat"][memoria]=resambos
                quadGen.gen_quad("+", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
            elif p[2]=="-":
                resambos=res1-res2
                local_var_table["values"]["tempFloat"][memoria]=resambos
                quadGen.gen_quad("-", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
        #print("p[0]:",temp)        
        print(local_var_table)




def p_t(p):
    '''t : f 
         | t MULT f
         | t DIV f'''
    if len(p) == 2:
        p[0]=p[1]
    elif len(p)==4:
        global qCounter, tempCounterFloat, tempCounterInt, sTipos, tempIntMemory, tempFloatMemory
        temp = getTemp()
        tipo2=sTipos.pop()
        tipo1=sTipos.pop()
        resambos=None
        res1=None
        res2=None

        #print("cuadruplo de ",p[1],p[2],p[3])
        #print("temp actual", temp)
        

        #guardo el valor de su temp
        #print(temp)
        tipo_resultado = semantic_cube[tipo1][p[2]][tipo2]
        sTipos.append(tipo_resultado)
        if (tipo_resultado=="int"):
            local_var_table["variables"]["tempInt"][temp]=tempIntMemory
            tempIntMemory+=1
            tempCounterInt+=1
        elif (tipo_resultado=="float"):
            local_var_table["variables"]["tempFloat"][temp]=tempFloatMemory
            tempFloatMemory+=1
            tempCounterFloat+=1

        
###############Revisan si el parametro que se recibe ya es un numero
        if re.match(regexInt, str(p[1])):
            res1=p[1]

        elif re.match(regexFloat, str(p[1])):
            res1=p[1]

        if re.match(regexInt, str(p[3])):
            res2=p[3]

        elif re.match(regexFloat, str(p[3])):
            res2=p[3]
#########################################
##############Si no es un numero entonces buscan el valor del temp
        if res1==None:
            if tipo1=="int":
                memoria=local_var_table["variables"]["tempInt"][p[1]]
                res1=local_var_table["values"]["tempInt"][memoria]
            elif tipo1=="float":
                memoria=local_var_table["variables"]["tempFloat"][p[1]]
                res1=local_var_table["values"]["tempFloat"][memoria]

        if res2==None:
            if tipo2=="int":
                memoria=local_var_table["variables"]["tempInt"][p[3]]
                res2=local_var_table["values"]["tempInt"][memoria]
            elif tipo2=="float":
                memoria=local_var_table["variables"]["tempFloat"][p[3]]
                res2=local_var_table["values"]["tempFloat"][memoria]
############################################
        
        #print("VOY A HACER ",res1,p[2],res2)
        #Aqui hago la suma como tal y genero cuadruplos
        if tipo_resultado=="int":
            memoria=local_var_table["variables"]["tempInt"][temp]
            
            if p[2]=="*":
                resambos=res1*res2
                local_var_table["values"]["tempInt"][memoria]=resambos
                quadGen.gen_quad("*", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
            elif p[2]=="/":
                resambos=res1/res2
                local_var_table["values"]["tempInt"][memoria]=resambos
                quadGen.gen_quad("/", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
        elif tipo_resultado=="float":
            memoria=local_var_table["variables"]["tempFloat"][temp]
            
            if p[2]=="*":
                resambos=res1*res2
                local_var_table["values"]["tempFloat"][memoria]=resambos
                quadGen.gen_quad("*", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
            elif p[2]=="/":
                resambos=res1/res2
                local_var_table["values"]["tempFloat"][memoria]=resambos
                quadGen.gen_quad("/", p[1], p[3], temp)
                qCounter+=1
                p[0]=temp
        #print("p[0]:",temp)       
        #print(local_var_table)
   
def p_f(p):
    '''f : LPAREN exp RPAREN
         | CTI
         | CTF
         | var
         | call'''
    global regexInt, regexFloat, sTipos
    if len(p)==2:  
        if re.match(regexFloat, str(p[1])):
            sTipos.append("float")
        elif re.match(regexInt, str(p[1])):
            sTipos.append("int")
        p[0]=p[1]
        

#VOLVER A PONER FUNCESP
def p_statements(p):
    '''statements : assign
                 |  function
                 |  voidfunction
                 |  call
                 |  read
                 |  print
                 |  if
                 |  while
                 |  for
                 |  array
                 |  matrix
                 |  mean'''
    p[0] = p[1]
    
def p_assign(p):
    '''assign : var EQUAL exp SEMICOLON'''
    global qCounter, local_var_table, regexFloat, regexInt, regexTemp
    var_name=p[1]
    var_assign=p[3]
    estaenlocal=0
    var_assign_type="var"
    #Revisa si el que se le asignara es un numero int, float, un temp, o una variable
    if re.match(regexFloat, str(p[3])):
        var_assign_type="float"
    elif re.match(regexInt, str(p[3])):
        var_assign_type="int"
    elif re.match(regexTemp, str(p[3])):
        var_assign_type="temp"
    #Revisa si la variable es un int o un float
    if (var_name in (var_table["global"]["variables"]["int"]) or (var_name in local_var_table["variables"]["varInt"])):
        variable_type="int"
    elif ((var_name in var_table["global"]["variables"]["float"]) or (var_name in local_var_table["variables"]["varFloat"])):
        variable_type="float"

    #Revisa que a lo que se le esta asignando si exista
    if (var_assign_type=="var"):
         varExist(var_assign)
        
    #Ejecucion para scope global
    if scope == "global":
        if (var_name in (var_table["global"]["variables"]["int"]) or (var_name in var_table["global"]["variables"]["float"])):
            print("si existe en global")
            #genera cuadruplo
            quadGen.gen_quad("=",var_assign,None,var_name)
            qCounter+=1
            #añade valor a tabla de constantes

        else:
            print("ERROR NO EXISTE", var_name)
    #Ejecucion para scope local
    elif scope == "local":
        #primero revisa si esta en el local
        if (var_name in (local_var_table["variables"]["varInt"]) or (var_name in local_var_table["variables"]["varFloat"])):
            #para encontrar y almacenar direccion de memoria
            var_assign=p[3]
            if variable_type=="int":
                direccion_memoria = local_var_table.get("variables", {}).get("varInt", {}).get(var_name)
            elif variable_type=="float":
                direccion_memoria = local_var_table.get("variables", {}).get("varFloat", {}).get(var_name)
            direccion_memoria = direccion_memoria[0]
            add_local_var_value(variable_type,direccion_memoria, var_assign)
            #genera cuadruplo
            quadGen.gen_quad("=",var_assign,None,var_name)
            #añade valor a tabla de constantes
            qCounter+=1
            #switch para avisar que esta en local para que no revise en global
            estaenlocal=1
        elif ((var_name in (var_table["global"]["variables"]["int"]) or (var_name in var_table["global"]["variables"]["float"])) and estaenlocal==0):
            print("si existe en global")
            #genera cuadruplo
            quadGen.gen_quad("=",var_assign,None,var_name)
            qCounter+=1
            #añade valor a tabla de constantes
        else:
            print("ERROR NO EXISTE", var_name)

        

#Genera cuadruplos de read
def p_read(p):
    '''read : READ LPAREN var RPAREN SEMICOLON'''
    global qCounter, tempCounterInt, tempIntMemory, tempCounterFloat, tempFloatMemory
    temp=getTemp()
    var_name=p[3]
    if(var_name in (local_var_table["variables"]["varInt"])):
        local_var_table["variables"]["tempInt"][temp]=tempIntMemory
        tempIntMemory+=1
        tempCounterInt+=1
        quadGen.gen_quad('read', None, None, temp)
        quadGen.gen_quad('=', temp, None, p[3])
        qCounter += 2
    elif(var_name in (local_var_table["variables"]["varFloat"])):
        local_var_table["variables"]["tempFloat"][temp]=tempFloatMemory
        tempFloatMemory+=1
        tempCounterFloat+=1
        quadGen.gen_quad('read', None, None, temp)
        quadGen.gen_quad('=', temp, None, p[3])
        qCounter += 2
    else: print("ERROR no existe la var")
    
    

def p_print(p):
    '''print : PRINT LPAREN printp SEMICOLON'''
    global sPrints, qCounter
    while (len(sPrints)!=0):
        quadGen.gen_quad('print',None, None, sPrints.pop())
        qCounter+=1

#Genera cuadruplos de print, separado por comas recibe muchos parametros
def p_printp(p):
    '''printp : exp RPAREN
              | exp COMMA printp'''
    global qCounter, sPrints
    if((p[1] not in local_var_table["variables"]["varInt"]) and (p[1] not in local_var_table["variables"]["varFloat"])):
        print("ERROR VARIABLE NO EXISTE", p[1])
        sys.exit()
    if len(p) == 3:
        sPrints.append(p[1])
        p[0] = p[1]
    elif len(p) == 4:
        sPrints.append(p[1])
        p[0] = p[3]

def p_var(p):
    '''var : ID '''
    p[0]=p[1]
    
def p_call(p):
    '''call : ID LPAREN callp RPAREN'''
    global qCounter, paramCounter, currFunc, sCallParams, sReturns
    funCall=p[1]
    #Revisa si la funcion a llamar existe en la tabla de funciones
    if (funCall in functions_table):
        quadGen.gen_quad('ERA', None, None, funCall)
        qCounter+=1
        #Itera en la pila de parametros hasta que este vacia y genera el cuadruplo de cada param
        while (sCallParams!=[]):
            paramC = "par" + str(paramCounter)
            paramCounter += 1
            quadGen.gen_quad('PARAM', sCallParams.pop(), None, paramC)
        func_address = functions_table[funCall]["start_address"]
        quadGen.gen_quad('GOSUB', None, None, func_address)
        qCounter+=1
        #si la funcion a llamar es de tipo float o int, genera el cuadruplo de almacenarlo
        if((functions_table[funCall]["return_type"]=="int") or (functions_table[funCall]["return_type"]=="float")):
            temp=getTemp()
            quadGen.gen_quad('=', funCall, None, temp)
            qCounter+=1
            p[0]=temp
            #sReturns.append(getFuncReturn(funCall))
            #p[0]=(sReturns.pop())
    #Revisa si la funcion a llamar es la funcion actual
    elif (funCall == currFunc): 
        global currFuncStartAddress
        quadGen.gen_quad('ERA', None, None, funCall)
        qCounter+=1
        #Itera en la pila de parametros hasta que este vacia y genera el cuadruplo de cada param
        while (sCallParams!=[]):
            paramC = "par" + str(paramCounter)
            paramCounter += 1
            quadGen.gen_quad('PARAM', sCallParams.pop(), None, paramC)
        func_address = currFuncStartAddress+1
        quadGen.gen_quad('GOSUB', None, None, func_address)
        qCounter+=1
        #si la funcion a llamar es de tipo float o int, genera el cuadruplo de almacenarlo
        if(currFuncType=="int") or (currFuncType=="float"):
            temp=getTemp()
            quadGen.gen_quad('=', currFunc, None, temp)
            qCounter+=1
            p[0]=temp
            #print("ES UNA LLAMADA A TIPO FLOAT O INT A SI MISMO")
            #sReturns.append(getFuncReturn(funCall))
            #print(sReturns)
            pass
    else:
        print("ERROR NO EXISTE ESA FUNCION")
    sCallParams=[]
    paramCounter=1
        

def p_callp(p):
    '''callp : exp COMMA callp
             | exp
             | '''
    global paramCounter,qCounter
    if len(p)>1:
        sCallParams.append(p[1])
        qCounter+=1

       
##################Quads if######################   
#def p_if(p):
#    '''if : IF LPAREN exp quadsIf RPAREN statements ifp jumpsIf'''    
def p_if(p):
    '''if : IF LPAREN ifexp RPAREN quadsIf LBRACE body RBRACE ifelse jumpsIf SEMICOLON'''

def p_ifexp(p):
    '''ifexp : exp '''
    global sBools
    sBools.append(p[1])

def p_ifelse(p):
    ''' ifelse : 
               | ELSE quadsElse LBRACE body RBRACE'''
    global hayElse
    if (len(p)>2):
        hayElse=1
    else: hayElse=0
            

def p_quadsIf(p):
    '''quadsIf : '''            
    print("AQUI CORRE EL QUADSIF")
    global sBools, qCounter, tempCounter, currBool, sJumps
    currBool=sBools.pop()
    quadGen.gen_quad("gotoF", currBool, None, None)
    sJumps.append(qCounter)
    qCounter += 1

def p_jumpsIf(p):
    '''jumpsIf : '''  
    global qCounter, currBool, sJumps, hayElse    
    jumps = sJumps.pop()
    if(hayElse):
        print("ENTRO ELSE")
        quadGen.quads[jumps] = ("goto",None,None,qCounter)
    else:
        quadGen.quads[jumps] = ("gotoF",currBool ,None,qCounter)

    #al final reseteamos todos nuestras pilas
    sBools=[]
    sJumps=[]


def p_quadsElse(p):
    '''quadsElse : '''   
    print("AQUI CORRE EL QUADSELSE") 
    global sOperators, sOperands, qCounter, currBool, sJumps
    quadGen.gen_quad("goto", None, None, None)
    jumps = sJumps.pop()
    sJumps.append(qCounter)
    qCounter += 1
    quadGen.quads[jumps] = ("gotoF",currBool,None,qCounter)

###############################Quands while#############
def p_while(p):
    ''' while : WHILE saveJumps LPAREN whilexp RPAREN quadsWhile LBRACE body RBRACE jumpsWhile SEMICOLON'''

def p_whilexp(p):
    '''whilexp : exp '''
    global sBools
    sBools.append(p[1])

def p_saveJumps(p):
    ''' saveJumps :'''
    global sJumps, qCounter
    sJumps.append(qCounter)
    
def p_quadsWhile(p):
    ''' quadsWhile :'''
    global sBools, qCounter, tempCounter, currBool, sJumps
    currBool=sBools.pop()
    quadGen.gen_quad("gotoF", currBool, None, None)
    sJumps.append(qCounter)
    qCounter += 1
    
def p_jumpsWhile(p):
    ''' jumpsWhile :'''
    global qCounter, currBool, sJumps, hayElse, sBools    
    jumps = sJumps.pop()
    qCounter += 1
    quadGen.quads[jumps] = ("gotoF", currBool, None, qCounter)
    jumps = sJumps.pop()
    quadGen.gen_quad("goto",None ,None,jumps)
    #al final reseteamos todos nuestras pilas
    sBools=[]
    sJumps=[]
    ##################################################################

def p_for(p):
    '''for : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp'''
    
def p_forp(p):
    ''' forp : RBRACKET
             | statements forp'''
    

 ##########################----------AQUI INICIAN FUNCIONES ESPECIALES--------------------------------------------------------------------------   
def p_funcesp(p):
    ''' funcesp : array
                | mean
                | layers
                | sequential
                | compile
                | fit
                | predict
                | getweights'''  

def p_array(p):
    ''' array : ARRAY ID LBRACKET exp RBRACKET EQUAL LBRACKET arrvalues RBRACKET SEMICOLON'''
    global qCounter, local_var_table, tempFloatMemory, currFunc, tempCounterFloat, sArrayValues, cArrayValues
    array_name=p[2]
    r=1
    rows=p[4]
    temp=getTemp()
    #cuadruplo que genera var para almacenar array
    quadGen.gen_quad("ARRAY", array_name, rows, None)
    qCounter+=1
    #calculo size
    size=r*(rows+1)

    #creo var en tabla local float
    add_var_local(array_name,"float",currFunc)
    memory=local_var_table["variables"]["varFloat"][array_name]
    memory=memory[0]
    
    if (cArrayValues!=size):
        print("ERROR NUMERO INVALIDO DE VALORES PARA ARRAY",array_name,"SE ESPERAN",size,"SE TIENEN", cArrayValues)
        sys.exit()
    i=0
    print(sArrayValues)
    while(len(sArrayValues)!=0):
        value=sArrayValues.pop()
        temp=getTemp()
        if i==0:
            local_var_table["values"]["varFloat"][memory]=temp
            quadGen.gen_quad("ARRAYSTART",temp,memory, array_name)
            qCounter+=1
        local_var_table["variables"]["tempFloat"][temp]=tempFloatMemory
        local_var_table["values"]["tempFloat"][tempFloatMemory]=value
        tempFloatMemory+=1
        tempCounterFloat+=1
        quadGen.gen_quad("=",f"{array_name}[{i}]", None, temp)
        qCounter+=1
        i+=1
    quadGen.gen_quad("ARRAYEND",temp, memory, array_name)
    qCounter+=1

    #reseteo sArrayValues y cArrayValues
    cArrayValues=0
    sArrayValues=[]


def p_arrvalues(p):
    '''arrvalues : exp
                 | exp COMMA arrvalues'''
    global sArrayValues, cArrayValues
    if len(p)==2:
        sArrayValues.append(p[1])
        cArrayValues+=1
    elif len(p)==4:
        sArrayValues.append(p[1])
        cArrayValues+=1
        p[0]=p[1]

def p_matrix(p):
    '''matrix : MATRIX ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUAL LBRACKET matvalues RBRACKET SEMICOLON'''
    global qCounter, local_var_table,tempFloatMemory, currFunc, tempCounterFloat, sMatrixSize, sMatrixStart, matrixCounter, tempCounterFloat, mValues, sMatrixValues
    matrix_name=p[2]
    r=1
    rows=p[4]
    columns=p[7]
    temp=getTemp()
    #cuadruplo que genera var para almacenar matrix
    quadGen.gen_quad("MATRIX", matrix_name, rows, columns)
    qCounter+=1
    #Calculo size          
    lSup1=rows
    lSup2=columns
    r=r*(lSup1+1)
    r=r*(lSup2+1)
    m0=r
    size=m0

    #todas las matrix seran de tipo float
    #creo var en tabla local
    add_var_local(matrix_name,"float",currFunc)
    memory=local_var_table["variables"]["varFloat"][matrix_name]
    memory=memory[0]
    matrixCounter+=1

    if (mValues!=size):
        print("ERROR NUMERO INVALIDO DE VALORES PARA MATRIX",matrix_name,"SE ESPERAN",size,"SE TIENEN", mValues)
        sys.exit()
    #cuadruplo matrixstart que envia cuando inicia la matrix y en que direccion de memoria, y que matrix es
    i=0
    j=0
    #ordena los valores
    ordered_values = []
    for i in range(rows+1):
        row = []
        for j in range(columns+1):
            value = sMatrixValues.pop()
            row.append(value)
        ordered_values.append(row)
    #print ( "ORDERED VALUES" ,ordered_values)

    #genera cuadruplos usando valores ordenados y los almacena en temporales
    for i in range(rows+1):
        for j in range(columns+1):
            value = ordered_values[i][j]
            temp=getTemp()
            if i==0 and j==0:
                local_var_table["values"]["varFloat"][memory]=temp
                quadGen.gen_quad("MATRIXSTART",temp,memory, matrix_name)
                qCounter+=1
            local_var_table["variables"]["tempFloat"][temp]=tempFloatMemory
            local_var_table["values"]["tempFloat"][tempFloatMemory]=value
            tempFloatMemory+=1
            tempCounterFloat+=1
            quadGen.gen_quad("=",f"{matrix_name}[{i}][{j}]", None, temp)
            qCounter+=1

    quadGen.gen_quad("MATRIXEND",temp, memory, matrix_name)
    qCounter+=1

    #reseteo mvalues y smatrixvalues
    mValues=0
    sMatrixValues=[]

                
def p_mat_values(p):
    '''matvalues : exp
                 | exp COMMA matvalues'''
    global sMatrixValues, mValues
    if len(p)==2:
        sMatrixValues.append(p[1])
        mValues+=1
    elif len(p)==4:
        sMatrixValues.append(p[1])
        mValues+=1
        p[0]=p[1]

def p_mean(p):
    '''mean : MEAN LPAREN ID RPAREN SEMICOLON'''
    global qCounter
    id=p[3]
    varExist(id)
    quadGen.gen_quad("MEAN", id, None, None)
    qCounter+=1
    
def p_layers(p):
    '''layers : ID EQUAL LAYERS LPAREN UNITS EQUAL INT RPAREN'''
    
def p_sequential(p):
    ''' sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp'''
    
def p_sequentialp(p):
    ''' sequentialp : RBRACKET RPAREN
                    | COMMA layers sequentialp'''
                    
def p_compile(p):
    ''' compile : sequential DOT COMPILE LPAREN RPAREN'''
    
def p_fit(p):
    ''' fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL INT COMMA VERBOSE EQUAL fitp'''
    
def p_fitp(p):
    ''' fitp : TRUE RPAREN
             | FALSE RPAREN'''

def p_predict(p):
    ''' predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp'''
    
def p_predictp(p):
    ''' predictp : INT RBRACKET RPAREN
                 | FLOAT RBRACKET RPAREN'''

def p_getweights(p):
    ''' getweights : layers DOT GETWEIGHTS LPAREN RPAREN'''

# Empty production
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Error de Sintaxis",p)
    #print("error en la linea "+ str(p.lineno))


#start='program'
parser = yacc.yacc()


# Procesar cada línea con el parser


fileName = "pruebarray.txt"   
inputFile = open(fileName, 'r')
inputCode = inputFile.read()
inputFile.close()

parser.parse(inputCode, lexer=bixoLexer.lexer)