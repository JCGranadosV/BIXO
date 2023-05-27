import copy
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
            result += f"{i+1}: {QuadGenerator.format_quad(quad)}\n"
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

#Funcion que agrega variable local a tabla y asigna memoria
def add_var_local(name, type, currFunc):
     if(type=="int"):
        var_mem = local_var_table["counters"][type] + localInt
     elif(type=="float"):
        var_mem = local_var_table["counters"][type] + localFloat
     #print("memoria:",var_mem)
     local_var_table["function"] = currFunc
     local_var_table["counters"][type] += 1
     local_var_table["variables"][type][name] = [var_mem]      
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
    local_var_table["values"][variable_type][direccion_memoria]=var_assign

#Funcion que crea temporales
def getTemp():
    global tempCounter
    temp = "t" + str(tempCounter)
    tempCounter += 1
    sTemp.append(temp)
    return temp

tokens=bixoLexer.tokens

#almacena los tipos de variables
sTypes = [] 
#pila saltos
sJumps = []
qCounter=0
#counter y stack de temporales
tempCounter=0
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
currFuncStartAddress=0
localArray=[]
localTypes=[]
contLocal=-1
regexInt=r'\d+'
regexFloat=r'\d+\.\d+'
paramCounter=1
sParams=[]
counterInicioFunc=0
#Counters de temporales
tempCounterInt=0
tempCounterFloat=0
#pilatipos cubo semantico
sTipos=[]

functions_table = {}

def add_function(name, return_type, start_address, varInt, varFloat, tempInt, tempFloat,local_table):
    functions_table[name] = {
        "return_type": return_type,
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
    local_var_table["variables"]["int"]={}
    local_var_table["variables"]["float"]={}
    local_var_table["counters"]["int"]=0
    local_var_table["counters"]["float"]=0
    local_var_table["values"]["int"]={}
    local_var_table["values"]["float"]={}
    print("LOCAL VAR TABLE DESPUES DE EMPTY: ",local_var_table)

def checkTable():
    return(local_var_table)
    

########################--Rangos de memoria--############################

globalInt = 4000
globalFloat = 8000 
localInt = 12000
localFloat = 16000
tempInt = 20000
tempFloat = 24000
tempPointer = 28000
consInt = 32000
consFloat = 36000
consString = 40000



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
    '''program : PROGRAM gotomain ID SEMICOLON decvar modules'''
    print("Nombre del programa:", p[2])
    print("TABLA DE FUNCIONES", functions_table)
    print("Cuadruplos: ",str(quadGen))
    print("Counter de cuadruplos: ", qCounter)

def p_gotomain(p):
    '''gotomain : '''
    global qCounter
    #genera cuadruplo goto main
    quadGen.gen_quad("GOTO","main",None,None)
    #añade valor a tabla de constantes
    qCounter+=1

def p_decvar(p):
    '''decvar : VAR decvarp
              | VAR decvarp decvar
              |'''
    global scope
    scope="local"
    #p[0]=p[2]

def p_decvarp(p):
    '''decvarp : type decvarpp SEMICOLON'''

    print("EL SCOPE ES", scope)

    var_type = p[1]
    var_name = p[2]

    if scope == "local":
        #print("pilavars: ", sVars)
        for vars in sVars:
        #Revisa que la variable no exista ya en la tabla 
            if (vars in local_var_table["variables"]["int"]) or (vars in local_var_table["variables"]["float"]):
                #antes de implementar este error checar la logica 
                print(vars,"ERROR YA EXISTE")
            else:
                add_var_local(vars,var_type,currFunc) 
        #copy_var_local()

    if scope == "global":
        #print("pilavars: ", sVars)
        #Revisa que la variable no exista ya en la tabla 
        for vars in sVars:
            if (vars in var_table["global"]["variables"]["int"]) or (vars in var_table["global"]["variables"]["float"]):
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
    '''function : FUNCTION type decfunc LPAREN param RPAREN LBRACE body RBRACE'''
    global localArray, currFunc, functions_table, counterInicioFunc, tempCounterFloat, tempCounterInt
    func_type=p[2]
    copy_var_local()
    #Revisa si existe la función
    if currFunc in functions_table: 
        print("YA EXISTE ESA FUNCION")
    else:
        #Revisa que si haya algo en su tabla de variables locales
        if(len(localArray)!=0):
            func_var_table=localArray.pop()
        else: func_var_table=local_var_table
        func_var_table_copy = copy.deepcopy(func_var_table)
        print("FUNC VAR TABLE ES: ",func_var_table_copy)
        varCounterFloat=func_var_table_copy['counters']['float']
        varCounterInt=func_var_table_copy['counters']['int']
        add_function(currFunc, func_type, (counterInicioFunc+1), varCounterInt,varCounterFloat, tempCounterInt, tempCounterFloat, func_var_table_copy)
        #Reseteo counters despues de guardar para usarlos en la prox funcion
        tempCounterFloat=0
        tempCounterInt=0
        #print("TABLA DE FUNCIONES", functions_table)

def p_decfunc(p):
    '''decfunc : ID'''
    limpiaDatos()
    global currFunc,currFuncStartAddress,counterInicioFunc
    print(tempCounter)
    currFunc=p[1]
    currFuncStartAddress=qCounter
    counterInicioFunc=qCounter
    print("CURRENT FUNCCC", currFunc)

    
def p_voidfunction(p):
    '''voidfunction : FUNCTION VOID decfunc LPAREN param RPAREN LBRACE body RBRACE'''
    global localArray, currFunc, functions_table,counterInicioFunc, tempCounterInt, tempCounterFloat
    func_type=p[2]
    #Revisa si existe la función
    if currFunc in functions_table: 
        print("YA EXISTE ESA FUNCION")
    else:
        #Revisa que si haya algo en su tabla de variables locales
        if(len(localArray)!=0):
            func_var_table=localArray.pop()
        else: func_var_table=local_var_table
        func_var_table_copy = copy.deepcopy(func_var_table)
        varCounterFloat=func_var_table_copy['counters']['float']
        varCounterInt=func_var_table_copy['counters']['int']
        add_function(currFunc, func_type, (counterInicioFunc+1), varCounterInt, varCounterFloat, tempCounterInt, tempCounterFloat, func_var_table_copy)
        #Reseteo counters despues de guardar para usarlos en la prox funcion
        tempCounterFloat=0
        tempCounterInt=0
        #print("TABLA DE FUNCIONES", functions_table)

def p_mainfunction(p):
    '''mainfunction : MAIN LPAREN RPAREN LBRACE body RBRACE'''


def p_modules(p):
    '''modules : function modules
               | voidfunction modules
               | function
               | voidfunction'''
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
    global sVars, sTypes
    if len(p)==3:
        sTypes.append(p[1])
        sVars.append(p[2])
        add_var_local(p[2],p[1],currFunc) 


#AQUI FALTA EL DEL SEGUNDO     
def p_exp(p):
    '''exp : texp 
           | texp OR exp'''
    if len(p) == 2:
        p[0]=p[1]

#AQUI FALTA EL DEL SEGUNDO 
def p_texp(p):
    '''texp : gexp 
            | gexp AND texp'''
    if len(p) == 2:
        p[0]=p[1]

def p_gexp(p):
    '''gexp : mexp 
            | mexp gexpp mexp'''
    if len(p) == 2:
        p[0]=p[1]
    elif len(p) == 4:
        sOperands.append(p[1])
        sOperands.append(p[3])
        sOperators.append(p[2])
        #print("Pila operandos:", sOperands)
        #print("pila operadores:", sOperators)

def p_gexpp(p):
    '''gexpp : LT
             | GT
             | EQUAL
             | DIFF'''
    p[0]=p[1]
             
def p_mexp(p):
    '''mexp : t
            | mexp PLUS t
            | mexp MINUS t'''
    if len(p) == 2:
        p[0]=p[1]
    elif len(p)==4:
        global qCounter, tempCounterFloat, tempCounterInt
        temp = getTemp()
        tipo2=sTipos.pop()
        tipo1=sTipos.pop()
        tipo_resultado = semantic_cube[tipo1][p[2]][tipo2]
        sTipos.append(tipo_resultado)
        if (tipo_resultado=="int"):
                tempCounterInt+=1
        elif (tipo_resultado=="float"):
                tempCounterFloat+=1
        qCounter+=1
        if p[2]=="+":
            quadGen.gen_quad("+", p[1], p[3], temp)
            p[0]=temp
        elif p[2]=="-":
            quadGen.gen_quad("-", p[1], p[3], temp)
            p[0]=temp
    

def p_t(p):
    '''t : f 
         | t MULT f
         | t DIV f'''
    
    if len(p) == 2:
        p[0]=p[1]
    elif len(p)==4:
        global qCounter, tempCounterFloat, tempCounterInt
        temp = getTemp()
        tipo2=sTipos.pop()
        tipo1=sTipos.pop()
        tipo_resultado = semantic_cube[tipo1][p[2]][tipo2]
        sTipos.append(tipo_resultado)
        if (tipo_resultado=="int"):
                tempCounterInt+=1
        elif (tipo_resultado=="float"):
                tempCounterFloat+=1
        qCounter+=1
        if p[2]=="*":
            quadGen.gen_quad("*", p[1], p[3], temp)
            p[0]=temp
        elif p[2]=="/":
            temp = getTemp()
            quadGen.gen_quad("/", p[1],p[3], temp)
            p[0]=temp
   
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
                 |  for'''
    p[0] = p[1]
    
def p_assign(p):
    '''assign : var EQUAL exp SEMICOLON'''
    global qCounter, local_var_table
    var_name=p[1]
    var_assign=p[3]
    estaenlocal=0
    if (var_name in (var_table["global"]["variables"]["int"]) or (var_name in local_var_table["variables"]["int"])):
        variable_type="int"
    elif ((var_name in var_table["global"]["variables"]["float"]) or (var_name in local_var_table["variables"]["float"])):
        variable_type="float"
    if scope == "global":
        if (var_name in (var_table["global"]["variables"]["int"]) or (var_name in var_table["global"]["variables"]["float"])):
            print("si existe en global")
            #genera cuadruplo
            quadGen.gen_quad("=",var_assign,None,var_name)
            qCounter+=1
            #añade valor a tabla de constantes

        else:
            print("ERROR NO EXISTE")
    elif scope == "local":
        #primero revisa si esta en el local
        if (var_name in (local_var_table["variables"]["int"]) or (var_name in local_var_table["variables"]["float"])):
            print("si existe en local")
            #para encontrar y almacenar direccion de memoria
            var_assign=p[3]
            direccion_memoria = local_var_table.get("variables", {}).get(variable_type, {}).get(var_name)
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
            print("ERROR NO EXISTE")

    print(quadGen.quads)
        

#Genera cuadruplos de read
def p_read(p):
    '''read : READ LPAREN var RPAREN SEMICOLON'''
    global qCounter
    temp=getTemp()
    quadGen.gen_quad('read', None, None, temp)
    quadGen.gen_quad('=', temp, None, p[3])
    qCounter += 2


def p_print(p):
    '''print : PRINT LPAREN printp SEMICOLON'''

#Genera cuadruplos de print, separado por comas recibe muchos parametros
def p_printp(p):
    '''printp : exp RPAREN
              | exp COMMA printp'''
    global qCounter
    if len(p) == 3:
        quadGen.gen_quad('print', None, None, p[1])
        qCounter += 1
        p[0] = p[1]
    elif len(p) == 4:
        quadGen.gen_quad('print', None, None, p[1])
        qCounter += 1
        p[0] = p[3]

def p_var(p):
    '''var : ID '''
    p[0]=p[1]
    
def p_call(p):
    '''call : ID LPAREN callp RPAREN SEMICOLON'''
    global qCounter, paramCounter, currFunc, sParams
    funCall=p[1]
    #Revisa si la funcion a llamar existe en la tabla de funciones
    if (funCall in functions_table):
        quadGen.gen_quad('ERA', None, None, funCall)
        qCounter+=1
        #Itera en la pila de parametros hasta que este vacia y genera el cuadruplo de cada param
        while (sParams!=[]):
            paramC = "par" + str(paramCounter)
            paramCounter += 1
            quadGen.gen_quad('PARAM', sParams.pop(), None, paramC)
        func_address = functions_table[funCall]["start_address"]
        quadGen.gen_quad('GOSUB', None, None, func_address)
        qCounter+=1
    #Revisa si la funcion a llamar es la funcion actual
    elif (funCall == currFunc): 
        global currFuncStartAddress
        quadGen.gen_quad('ERA', None, None, funCall)
        qCounter+=1
        #Itera en la pila de parametros hasta que este vacia y genera el cuadruplo de cada param
        while (sParams!=[]):
            paramC = "par" + str(paramCounter)
            paramCounter += 1
            quadGen.gen_quad('PARAM', sParams.pop(), None, paramC)
        func_address = currFuncStartAddress+1
        quadGen.gen_quad('GOSUB', None, None, func_address)
        qCounter+=1
    else:
        print("ERROR NO EXISTE ESA FUNCION")
    sParams=[]
    paramCounter=1
        

def p_callp(p):
    '''callp : exp COMMA callp
             | exp
             | '''
    global paramCounter,qCounter
    if len(p)>1:
        sParams.append(p[1])
        qCounter+=1

       
##################Quads if######################   
#def p_if(p):
#    '''if : IF LPAREN exp quadsIf RPAREN statements ifp jumpsIf'''    
def p_if(p):
    '''if : IF LPAREN exp RPAREN quadsIf statements ifelse jumpsIf'''
    print("AQUI CORRE EL IF")
    print("QG ES: ",str(quadGen))    
    print("OPERANDS",sOperands)    
def p_ifelse(p):
    ''' ifelse : 
               | ELSE quadsElse statements'''
    global hayElse
    if (len(p)>2):
        hayElse=1
    else: hayElse=0
            

def p_quadsIf(p):
    '''quadsIf : '''            
    print("AQUI CORRE EL QUADSIF")
    global sOperators, sOperands, sTypes, qCounter, tempCounter
    arg2=sOperands.pop()
    arg1=sOperands.pop()
    operator=sOperators.pop()
    if operator not in ['ERA', 'GOSUB']:
        temp = "t" + str(tempCounter)
        quadGen.gen_quad(operator, arg1, arg2, temp)
        tempCounter += 1
    else:
        print("no entro el temp")
        quadGen.gen_quad(operator, arg1, arg2, None)
    print(arg1,arg2,operator)
    if(operator == ">"):
        if(arg1>arg2):
            sOperands.append(1)
        else: sOperands.append(0)
    elif(operator == "=="):
        if(arg1==arg2):
            sOperands.append(1)
        else: sOperands.append(0)    
    elif(operator == "<"):
        if(arg1<arg2):
            sOperands.append(1)
        else: sOperands.append(0)    
    elif(operator == "!="):
        if(arg1!=arg2):
            sOperands.append(1)
        else: sOperands.append(0) 
    toF = sOperands[len(sOperands)-1]
    if (len(sOperands) != 0):
        print("TOF ES: ",sOperands[len(sOperands)-1])
        if (toF == 0 or toF ==1):
            print("ENTRO AL IF")
            quadGen.gen_quad("gotoF", sOperands[len(sOperands)-1], None, None)
            qCounter += 1
            sJumps.append(qCounter)
            print("QG ES: ",str(quadGen))
            print(sJumps)
    else: print("no es bool")
    

def p_jumpsIf(p):
    '''jumpsIf : '''  
    print("AQUI CORRE EL JUMPIF")
    print("jumpsif")          
    jumps = sJumps.pop()
    print("JUMPS ES: ",jumps)
    if(hayElse):
        print("ENTRO ELSE")
        quadGen.quads[jumps] = ("goto",None,None,qCounter)
    else: quadGen.quads[jumps] = ("gotoF",sOperands[len(sOperands)-1],None,qCounter)

def p_quadsElse(p):
    '''quadsElse : '''   
    print("AQUI CORRE EL QUADSELSE") 
    global sOperators, sOperands, sTypes, qCounter
    quadGen.gen_quad("goto", None, None, None)
    qCounter += 1
    jumps = sJumps.pop()
    sJumps.append(qCounter)
    quadGen.quads[jumps] = ("gotoF",sOperands[len(sOperands)-1],None,qCounter)
    print("QG ES: ",str(quadGen))

###############################Quands while#############
def p_while(p):
    ''' while : WHILE LPAREN saveJumps exp RPAREN quadsWhile statements jumpsWhile whilep'''

def p_whilep(p):
    ''' whilep : SEMICOLON
               | statements whilep'''
               
def p_saveJumps(p):
    ''' saveJumps :'''
    sJumps.append(qCounter)
    
def p_quadsWhile(p):
    ''' quadsWhile :'''
    print("AQUI CORRE EL QUADSWHILE")
    global sOperators, sOperands, sTypes, qCounter, tempCounter
    arg2=sOperands.pop()
    arg1=sOperands.pop()
    operator=sOperators.pop()
    if operator not in ['ERA', 'GOSUB']:
        temp = "t" + str(tempCounter)
        quadGen.gen_quad(operator, arg1, arg2, temp)
        tempCounter += 1
    else:
        print("no entro el temp")
        quadGen.gen_quad(operator, arg1, arg2, None)
    print(arg1,arg2,operator)
    if(operator == ">"):
        if(arg1>arg2):
            sOperands.append(1)
        else: sOperands.append(0)
    elif(operator == "=="):
        if(arg1==arg2):
            sOperands.append(1)
        else: sOperands.append(0)    
    elif(operator == "<"):
        if(arg1<arg2):
            sOperands.append(1)
        else: sOperands.append(0)    
    elif(operator == "!="):
        if(arg1!=arg2):
            sOperands.append(1)
        else: sOperands.append(0) 
    toF = sOperands[len(sOperands)-1]
    if (len(sOperands) != 0):
        print("TOF ES: ",sOperands[len(sOperands)-1])
        if (toF == 0 or toF ==1):
            print("ENTRO AL WHILE")
            quadGen.gen_quad("gotoF", sOperands[len(sOperands)-1], None, None)
            qCounter += 1
            sJumps.append(qCounter)
            print("QG ES: ",str(quadGen))
            print(sJumps)
    else: print("no es bool")
    
def p_jumpsWhile(p):
    ''' jumpsWhile :'''
    global sOperators, sOperands, sTypes, qCounter, sJumps
    jumps = sJumps.pop()
    endret = sJumps.pop()
    quadGen.gen_quad("goto", len(sOperands)-1, None, endret)
    qCounter += 1
    quadGen.quads[jumps] = ("goto",None,None,qCounter)
    ##################################################################

def p_for(p):
    '''for : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statements forp'''
    
def p_forp(p):
    ''' forp : RBRACKET
             | statements forp'''
    

 ##########################----------AQUI INICIAN FUNCIONES ESPECIALES--------------------------------------------------------------------------   
def p_funcesp(p):
    ''' funcesp : array
                | matrix
                | mean
                | layers
                | sequential
                | compile
                | fit
                | predict
                | getweights'''  

def p_array(p):
    ''' array : ID EQUAL ARRAY LPAREN var arrayp'''
    
def p_arrayp(p):
    ''' arrayp : RPAREN
               | COMMA var RPAREN'''
    
def p_matrix(p):
    ''' matrix : ID EQUAL MATRIX LPAREN array matrixp'''
    
def p_matrixp(p):
    ''' matrixp : RPAREN
                | COMMA array RPAREN'''
                
def p_mean(p):
    '''mean : MEAN LPAREN array RPAREN'''
    
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


fileName = "prueba4.txt"   
inputFile = open(fileName, 'r')
inputCode = inputFile.read()
inputFile.close()

parser.parse(inputCode, lexer=bixoLexer.lexer)