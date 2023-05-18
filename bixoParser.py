import sys
import copy
import ply.yacc as yacc
import bixoLexer
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
        }
    },
    "local": {
        "function":"",
        "variables": {
            "int": {},
            "float": {}
        },
        "counters": {
            "int": 0,
            "float": 0
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
    }
}

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

def add_var_global(name, type):
     if(type=="int"):
        var_mem = var_table["global"]["counters"][type] + globalInt
     elif(type=="float"):
        var_mem = var_table["global"]["counters"][type] + globalFloat
     #print("memoria:",var_mem)
     var_table["global"]["counters"][type] += 1
     var_table["global"]["variables"][type][name] = [var_mem]      
     sTypes.append(type)

tokens=bixoLexer.tokens

#almacena los tipos de variables
sTypes = [] 
#pila saltos
sJumps = []
qCounter=0
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
localArray=[]
localTypes=[]
contLocal=-1

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
        "vars_table": {local_table}
    }

#para acceder a tabla de funciones de alguna funcion
# vars_table = functions_table[function_name]["vars_table"]

def limpiaDatos():
    local_var_table["function"]=""
    local_var_table["variables"]["int"]={}
    local_var_table["variables"]["float"]={}
    local_var_table["counters"]["int"]=0
    local_var_table["counters"]["float"]=0

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
    '''program : PROGRAM ID SEMICOLON decvar modules mainfunction'''
    print("Nombre del programa:", p[2])
    #p[0]=p[4]


def p_decvar(p):
    '''decvar : VAR decvarp
              | VAR decvarp decvar'''
    global scope
    scope="local"
    #p[0]=p[2]

def p_decvarp(p):
    '''decvarp : type decvarpp SEMICOLON'''
    
    print("EL SCOPE ES", scope)

    var_type = p[1]
    var_name = p[2]

    if scope == "local":
        print("pilavars: ", sVars)
        for vars in sVars:
        #Revisa que la variable no exista ya en la tabla 
            if (vars in local_var_table["variables"]["int"]) or (vars in local_var_table["variables"]["float"]):
                #antes de implementar este error checar la logica 
                print(vars,"ERROR YA EXISTE")
            else:
                add_var_local(vars,var_type,currFunc) 

        print("pilatypes: ", sTypes)
        local_var_table_copy = copy.deepcopy(local_var_table)
        print ("var_table (local): ",local_var_table_copy)
        global localArray
        localArray.append(local_var_table_copy)
        print("LOCAL ARRAY (LOCAL)",localArray)

    if scope == "global":
        print("pilavars: ", sVars)
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
        print("pilatypes: ", sTypes)
        print ("var_table (global): ",var_table["global"])

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
    global localArray
    lA=localArray
    global currFunc
    func_type=p[2]
    func_id=p[3]
    print("CURRENT FUNC",currFunc)
    print("LOCAL ARRAY ES EN FUNC: ",lA)
    #add_function(func_id, func_type, qCounter, varInt, varFloat, tempInt, tempFloat, tabla_local)

def p_decfunc(p):
    '''decfunc : ID'''
    limpiaDatos()
    global currFunc
    currFunc=p[1]

    
def p_voidfunction(p):
    '''voidfunction : FUNCTION VOID ID LPAREN param RPAREN LBRACE body RBRACE'''

def p_mainfunction(p):
    '''mainfunction : MAIN'''
    


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
             | type ID COMMA param'''
    #sTypes.append(p[1])
    #sVars.append(p[2])
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
    if len(p) == 4:
        sOperands.append(p[1])
        sOperands.append(p[3])
        sOperators.append(p[2])

def p_gexpp(p):
    '''gexpp : LT
             | GT
             | EQUAL
             | DIFF'''
    p[0]=p[1]
             
def p_mexp(p):
    '''mexp : t
            | t PLUS mexp
            | t MINUS mexp'''
    if len(p) == 2:
        p[0]=p[1]
    elif len(p)==4:
        if p[2]=="+":
            p[0] = p[1] + p[3]
        elif p[2]=="-":
            p[0] = p[1] - p[3]
    

def p_t(p):
    '''t : f 
         | f MULT t
         | f DIV t'''
    if len(p) == 2:
        p[0]=p[1]
    elif len(p)==4:
        if p[2]=="*":
            p[0] = p[1] * p[3]
        elif p[2]=="/":
            p[0] = p[1] / p[3]
   
def p_f(p):
    '''f : LPAREN exp RPAREN
         | CTI
         | CTF
         | var
         | call'''
    if len(p)==2:
        p[0]=p[1]

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
                 |  funcesp'''
    p[0] = p[1]
    
def p_assign(p):
    '''assign : var EQUAL exp SEMICOLON'''
    var_name=p[1]
    var_assign=p[3]
    estaenlocal=0
    if scope == "global":
        if var_name in (var_table["global"]["variables"]["int"] or var_table["global"]["variables"]["float"]):
            print("si existe en global")
            quadGen.gen_quad("=",var_assign,None,var_name)
        else:
            print("ERROR NO EXISTE")
    elif scope == "local":
        #primero revisa si esta en el local
        if var_name in (local_var_table["variables"]["int"] or local_var_table["variables"]["float"]):
            print("si existe en local")
            quadGen.gen_quad("=",var_assign,None,var_name)
            #switch para avisar que esta en local para que no revise en global
            estaenlocal=1
        elif (var_name in (var_table["global"]["variables"]["int"] or var_table["global"]["variables"]["float"])) and estaenlocal==0:
            print("si existe en global")
            quadGen.gen_quad("=",var_assign,None,var_name)
        else:
            print("ERROR NO EXISTE")

            
    print(quadGen.quads)
        


def p_read(p):
    '''read : READ var'''
#checar si tenemos que agregar sting o no xq la eliminamos
def p_print(p):
    '''print : PRINT LPAREN printp'''

def p_printp(p):
    '''printp : exp RPAREN
              | exp COMMA printp'''

def p_var(p):
    '''var : ID '''
    p[0]=p[1]
    
def p_call(p):
    '''call : ID LPAREN callp RPAREN'''

def p_callp(p):
    '''callp : exp SEMICOLON callp
             | exp'''
       
##################Quads if######################   
#def p_if(p):
#    '''if : IF LPAREN exp quadsIf RPAREN statements ifp jumpsIf'''    
def p_if(p):
    '''if : IF LPAREN CTI GT CTI RPAREN quadsIf ifp jumpsIf'''
 
def p_ifp(p):
    ''' ifp : 
            | ELSE quadsElse statements'''

def p_quadsIf(p):
    '''quadsIf : '''            
    global SOperators, sOperands, sTypes, qCounter
    print("quadsif")
    if len(SOperators) != 1:
        print("entro1")
        #if sTypes [0] == 'int':
        print("entro")
        #sTypes.pop()
        quadGen.gen_quad("+", "2", "3", "t1")
        quadGen.gen_quad("*", "1", "5", "t2")

        sJumps.append(qCounter)
        qCounter += 1
        print("QG ES: ",str(quadGen))
        print(quadGen.quads)

def p_jumpsIf(p):
    '''jumpsIf : '''  
    print("jumpsif")          
    jumps = sJumps.pop()
    #SQuads[jumps].temp = qCounter

def p_quadsElse(p):
    '''quadsElse : '''    
    global qCounter
    #SQuads.append(QuadGenerator("goto", None, None, None))
    jumps = sJumps.pop()
    sJumps.append(qCounter)
    qCounter += 1
    #SQuads[jumps].temp=qCounter

###############################Quands while#############
def p_while(p):
    ''' while : WHILE LPAREN exp RPAREN statements whilep'''

def p_whilep(p):
    ''' whilep : SEMICOLON
               | statements whilep'''

#global SOperators, sOperands, sTypes, SQuads, qCounter
 #   if len(SOperators) != 0:
  #      if sTypes [-1] == 'int':
   #         sTypes.pop()
    #        SQuads.append(QuadGenerator("gotoF", sOperands.pop(), None, None))
     #       sJumps.append(qCounter)
      #      qCounter += 1
            
    #global qCounter
    #qJumpsF = sJumps.pop()
    #qJumpsT = sJumps.pop()
    #SQuads.append(QuadGenerator("goto", None, None, qJumpsT))
    #qCounter += 1
    #SQuads[qJumpsF].temp = qCounter 
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


fileName = "prueba3.txt"   
inputFile = open(fileName, 'r')
inputCode = inputFile.read()
inputFile.close()

parser.parse(inputCode, lexer=bixoLexer.lexer)