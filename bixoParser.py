import sys
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
            "float": {},
            #"char": {},
            #"bool": {},
        },
        "counters": {
            "int": 0,
            "float": 0,
            #"char": 0,
            #"bool": 0,
        }
    },
    "local": {
        "function":"",
        "variables": {
            "int": {},
            "float": {},
            #"char": {},
            #"bool": {},
        },
        "counters": {
            "int": 0,
            "float": 0,
            #"char": 0,
            #"bool": 0,
        }
    }
}

def add_var_local(name, type, currFunc):
     if(type=="int"):
        var_mem = var_table["local"]["counters"][type] + localInt
     elif(type=="float"):
        var_mem = var_table["local"]["counters"][type] + localFloat
     print("memoria:",var_mem)
     var_table["local"]["function"] = currFunc
     var_table["local"]["counters"][type] += 1
     var_table["local"]["variables"][type][name] = [var_mem]      
     sTypes.append(type)

def add_var_global(name, type):
     if(type=="int"):
        var_mem = var_table["global"]["counters"][type] + globalInt
     elif(type=="float"):
        var_mem = var_table["global"]["counters"][type] + globalFloat
     print("memoria:",var_mem)
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
SOperators = []
#almacena el scope actual
scope="global"
#pilavars
sVars=[]
quadGen=QuadGenerator()
#pila de cuadruplos = quadGen.quads
#para imprimir cuadruplos : print(str(quadGen))
#current function
currFunc="ejemplo1"


functions_table = {}

def add_function(name, return_type, start_address, varInt, varFloat, tempInt, tempFloat, vars_table):
    functions_table[name] = {
        "return_type": return_type,
        "start_address": start_address,
        "resources": {
            "varInt": varInt,
            "varFloat": varFloat,
            "tempInt": tempInt,
            "tempFloat": tempFloat
        },
        "vars_table": vars_table
    }

#para acceder a tabla de funciones de alguna funcion
# vars_table = functions_table[function_name]["vars_table"]


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
    '''program : PROGRAM ID SEMICOLON if'''
    print("Nombre del programa:", p[2])
    #p[0]=p[4]


def p_decvar(p):
    '''decvar : VAR decvarp
              | VAR decvarp decvar'''
    #p[0]=p[2]

def p_decvarp(p):
    '''decvarp : type decvarpp SEMICOLON'''

    var_type = p[1]
    var_name = p[2]

    if scope == "local":
        print("pilavars: ", sVars)
        #Revisa que la variable no exista ya en la tabla 
        if var_name in var_table["local"]["variables"][var_type]:
            print("ya existeeeeeeeeeeeee")
        else:
            if var_type == "int":
                for vars in sVars:
                    add_var_local(vars,var_type,currFunc)
            elif var_type =="float":
                for vars in sVars:
                    add_var_local(vars,var_type,currFunc) 
        print("pilatypes: ", sTypes)
        print ("var_table (local): ",var_table["local"])

    if scope == "global":
        print("pilavars: ", sVars)
        #Revisa que la variable no exista ya en la tabla 
        if var_name in var_table["global"]["variables"][var_type]:
            print("ya existeeeeeeeeeeeee")
        else:
            for vars in sVars:
                if var_type == "int":
                    print("ES INT Y :", vars, var_type)
                    add_var_global(vars,var_type)
                elif var_type == "float":
                    add_var_global(vars,var_type)
        print("pilatypes: ", sTypes)
        print ("var_table (global): ",var_table["global"])

    sVars.clear()


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
    '''function : FUNCTION type ID LPAREN param RPAREN body'''
    
def p_voidfunction(p):
    '''voidfunction : FUNCTION VOID ID LPAREN param RPAREN body'''
    
def p_body(p):
    '''body : LBRACE bodyp RBRACE'''
    
def p_bodyp(p):
    '''bodyp : decvar statements bodyp
             | statements bodyp
             | decvar
             | '''
#checar si se puede vacio o epsilon
def p_param(p):
    '''param : 
             | type paramp'''

def p_paramp(p):
    ''' paramp : ID
               | ID COMMA param'''
               
def p_exp(p):
    '''exp : texp 
           | texp OR exp'''

def p_texp(p):
    '''texp : gexp 
            | gexp AND texp'''

def p_gexp(p):
    '''gexp : mexp 
            | mexp gexpp mexp'''

def p_gexpp(p):
    '''gexpp : LT
             | GT
             | EQUAL
             | DIFF'''
             
def p_mexp(p):
    '''mexp : t
            | t PLUS mexp
            | t MINUS mexp'''
    
    if p[2]=="+":
        p[0] = p[1] + p[3]
    elif p[2]=="-":
        p[0] = p[1] - p[3]

def p_t(p):
    '''t : f 
         | f MULT t
         | f DIV t'''
    if p.len()==2:
        p[0]=p[1]
         
def p_f(p):
    '''f : LPAREN exp RPAREN
         | INT
         | FLOAT
         | var
         | call'''
    if p.len()==2:
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
    '''assign : var EQUAL exp'''

def p_read(p):
    '''read : READ var'''
#checar si tenemos que agregar sting o no xq la eliminamos
def p_print(p):
    '''print : PRINT LPAREN printp'''

def p_printp(p):
    '''printp : exp RPAREN
              | exp COMMA printp'''

def p_var(p):
    '''var : ID 
           | ID LBRACKET exp RBRACKET
           | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET'''
    
    if len(p)==2:
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
    '''if : IF LPAREN INT EQUAL EQUAL CTI RPAREN quadsIf ifp jumpsIf'''
                
def p_ifp(p):
    ''' ifp : 
            | ELSE quadsElse statements'''

def p_quadsIf(p):
    '''quadsIf : '''            
    global SOperators, sOperands, sTypes, qCounter
    print("quadsif")
    sTypes = 1
    if  sTypes == 0 | 1:
        print("si es bool")
        print("entro1")
        quadGen.gen_quad("gotoF", None, None, None)
        quadGen.gen_quad("*", "1", "5", "t2")
        quadGen.gen_quad("*", "1", "5", "t2")
        sJumps.append(qCounter)
        qCounter += 1
        print("QG ES: ",str(quadGen))
        
        print("QG POS 0 ES>>> ",quadGen.quads)
    else: print("no es bool")

def p_jumpsIf(p):
    '''jumpsIf : '''  
    print("jumpsif")          
    jumps = sJumps.pop()
    print("jumpsif", quadGen.quads[0]) 

def p_quadsElse(p):
    '''quadsElse : '''    
    global qCounter
    quadGen.gen_quad("goto", None, None, None)
    jumps = sJumps.pop()
    sJumps.append(qCounter)
    qCounter += 1
    #quadGen[jumps].temp=qCounter

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


fileName = "prueba2.txt"   
inputFile = open(fileName, 'r')
inputCode = inputFile.read()
inputFile.close()

parser.parse(inputCode, lexer=bixoLexer.lexer)