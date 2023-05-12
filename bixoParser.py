import ply.yacc as yacc
import bixoLexer
from bixoLexer import tokens


class QuadGenerator:
    def __init__(self, op, arg1, arg2, res):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.res = res

    def __str__(self):
        return f'[{self.op}][{self.arg1}][{self.arg2}][{self.res}]'


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

#almacena los tipos de variables
sTypes = [] 
#pila saltos
sJumps = []
#Pila cuadruplos
SQuads = []
qCounter=0
#pila operandos
sOperands = []
#pila operadores
SOperators = []
#almacena el scope actual
scope="global"


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
def p_decvar(p):
    '''decvar : VAR type ID decvarp '''

    var_type = p[2]
    var_name = p[3]

    var_mem = None

#Para declarar variables locales
    if scope == "local":
     if var_type == "int":
        var_mem = var_table["local"]["counters"]["int"] + localInt
        var_table["local"]["counters"]["int"] += 1
     elif var_type == "float":
        var_mem = var_table["local"]["counters"]["float"] + localFloat
        var_table["local"]["counters"]["float"] += 1
    var_table["local"]["variables"][var_type][var_name] = var_mem
    


#Para declarar variables globales
    if scope == "global":
     if var_type == "int":
        var_mem = var_table["local"]["counters"]["int"] + localInt
        var_table["local"]["counters"]["int"] += 1
     elif var_type == "float":
        var_mem = var_table["local"]["counters"]["float"] + localFloat
        var_table["local"]["counters"]["float"] += 1
    var_table["local"]["variables"][var_type][var_name] = var_mem

def p_decvarp(p):
    '''decvarp : SEMICOLON decvarp
               | LBRACKET INT RBRACKET decvarpp'''
                            
def p_decvarpp(p):
    '''decvarpp : SEMICOLON
                | LBRACKET INT RBRACKET'''
 
def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR
            | STRING'''
    p[0] = p[1]
            
def p_function(p):
    '''function : FUNCTION type ID LPAREN param RPAREN body'''
    
def p_voidfunction(p):
    '''voidfunction : FUNCTION VOID ID LPAREN param RPAREN body'''
    
def p_body(p):
    '''body : LBRACE pbody RBRACE'''
    
def p_pbody(p):
    '''pbody : decvar statement pbody
             | statement pbody
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
    
    if p[2]=="PLUS":
        p[0] = p[1] + p[3]
    elif p[2]=="MINUS":
        p[0] = p[1] - p[3]

def p_t(p):
    '''t : f 
         | f MULT t
         | f DIV t'''
         
def p_f(p):
    '''f : LPAREN exp RPAREN
         | INT
         | FLOAT
         | var
         | call'''

def p_statement(p):
    '''statement : assign
                 |  call
                 |  read
                 |  print
                 |  if
                 |  while
                 |  for
                 |  funcesp'''
    
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
    
def p_call(p):
    '''call : ID LPAREN callp RPAREN'''

def p_callp(p):
    '''callp : exp SEMICOLON callp
             | exp'''
             
def p_if(p):
    '''if : IF LPAREN exp RPAREN statement ifp'''
#checar si se puede vacio o epsilon    
def p_ifp(p):
    ''' ifp : 
            | ELSE statement'''

#checar si la gen de codigo es correcta
def p_while(p):
    ''' while : WHILE LPAREN exp RPAREN statement whilep'''

def p_whilep(p):
    ''' whilep : SEMICOLON
               | statement whilep'''
  
def p_for(p):
    '''for : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statement forp'''
    
def p_forp(p):
    ''' forp : RBRACKET
             | statement forp'''
    
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

parser = yacc.yacc()

with open('prueba.txt', 'r') as archivo:
    lineas = archivo.readlines()


# Procesar cada línea con el parser
for i, linea in enumerate(lineas):
    resultado = parser.parse(linea, lexer=bixoLexer.lexer)
    print(f"Línea {i+1}: {linea.strip()} = {resultado}")