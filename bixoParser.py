import ply.yacc as yacc
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


procedures_directory = {}

def add_procedure(name, params, vars):
    procedures_directory[name] = {
        "params": params,
        "vars": vars
    }

def get_procedure(name):
    return procedures_directory.get(name, None)


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
    ('left', 'GREATER', 'SMALLER', 'EQUAL', 'DIFF'),
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
    if var_type == "int":
        var_mem = var_table["local"]["counters"]["int"] + localInt
        var_table["local"]["counters"]["int"] += 1
    elif var_type == "float":
        var_mem = var_table["local"]["counters"]["float"] + localFloat
        var_table["local"]["counters"]["float"] += 1
    
    var_table["local"]["variables"][var_type][var_name] = var_mem

def p_decvarp(p):
    '''decvarp : SEMICOLON decvarp
               | LBRACKET CONS-I RBRACKET decvarpp'''
                            
def p_decvarpp(p):
    '''decvarpp : SEMICOLON
                | LBRACKET CONS-I RBRACKET'''
 
def p_type(p):
    '''type : INT
            |  FLOAT
            |  CHAR
            |  STRING'''
    p[0] = p[1]
            
def p_function(p):
    '''function : FUNC functionp ID LPARENT param RPARENT body'''
    
def p_functionp(p):
    '''functionp : type function
                 | VOID function'''
#checar si se puede vacio o epsilon
def p_param(p):
    '''param : 
             | type paramp'''

def p_paramp(p):
    ''' paramp : ID
               | ID COMMA param'''
               
def p_exp(p):
    '''exp : texp 
           | texp || exp'''

def p_texp(p):
    '''texp : gexp 
            | gexp & texp'''

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

def p_t(p):
    '''t : f 
         | f MULT t
         | f DIV t'''
         
def p_f(p):
    '''f : LPARENT exp RPARENT
         | CONS-I
         | CONS-F
         | CONS-CH
         | CONS-STR
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
                 |  func_esp'''
    
def p_assign(p):
    '''assign : var EQUAL exp'''

def p_read(p):
    '''read : READ var'''

def p_print(p):
    '''print : PRINT LPAREN printp'''

def p_printp(p):
    '''printp : exp COMMA printp
              | sign COMMA printp
              | exp RPAREN
              | sign RPAREN'''

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
    '''if : IF LPARENT exp RPARENT statement ifp'''
#checar si se puede vacio o epsilon    
def p_ifp(p):
    ''' ifp : 
            | ELSE statement'''

#checar como hacer el loop
def p_while(p):
    ''' while : WHILE LPARENT exp RPARENT statement whilep'''
    
def p_whilep(p):
    ''' whilep : SEMICOLON
               | statement whilep'''
#checar como hacer el loop    
def p_for(p):
    '''for : FOR LPARENT var SEMICOLON exp SEMICOLON exp RPARENT LBRACKET statement forp'''
    
def p_forp(p):
    ''' forp : RBRACKET
             | statement forp'''
    
def p_funcesp(p):
    ''' funcesp : array
                | vector
                | matrix
                | mean
                | layers
                | secuential
                | compile
                | fit
                | predict
                | getweights'''  

def p_array(p):
    ''' array : ID EQUAL array LPARENT var arrayp'''
    
def p_arrayp(p):
    ''' arrayp : RPARENT
               | COMMA var RPARENT'''

def p_vector(p):
    ''' id : EQUAL array'''
    
def p_matrix(p):
    ''' matrix : ID EQUAL matrix LPARENT array matrixp'''
    
def p_matrixp(p):
    ''' matrixp : RPARENT
                | COMMA array RPARENT'''
                
def p_mean(p):
    '''mean : MEAN LPARENT array RPARENT'''
    
def p_layers(p):
    '''layers : ID EQUAL LAYERS LPARENT UNITS EQUAL CONS-I RPARENT'''
    
def p_sequential(p):
    ''' sequential : ID EQUAL SEQUENTIAL LPARENT LBRACKET layers sequentialp'''
    
def p_sequentialp(p):
    ''' sequentialp : RBRACKET RPARENT
                    | COMMA layers sequentialp'''
                    
def p_compile(p):
    ''' compile : sequential DOT COMPILE LPARENT RPARENT'''
    
def p_fit(p):
    ''' fit : ID EQUAL sequential DOT FIT LPARENT array COMMA array COMMA EPOCHS EQUAL CONS-I COMMA VERBOSE EQUAL fitp'''
    
def p_fitp(p):
    ''' fitp : TRUE RPARENT
             | FALSE RPARENT'''

def p_predict(p):
    ''' predict : ID EQUAL sequential DOT PREDICT LPARENT LBRACKET predictp'''
#Checar si se puede poner el - "cons-i"    
def p_predictp(p):
    ''' predictp : CONS-I RBRACKET RPARENT
                 | CONS-F RBRACKET RPARENT'''

def p_getweights(p):
    ''' getweights : layers DOT GETWEIGHTS LPARENT RPARENT'''





