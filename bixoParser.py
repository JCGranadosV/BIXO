import ply.yacc as yacc
from bixoLexer import tokens

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
    
def p_decvar(p):
    '''decvar : VAR type ID decvarp '''

#Revisar declaración de cons-i
def p_decvarp(p):
    '''decvarp : SEMICOLON decvarp
               | LBRACKET CONSI RBRACKET decvarpp'''
                            
def p_decvarpp(p):
    '''decvarpp : SEMICOLON
                | LBRACKET CONSI RBRACKET'''
 
def p_type(p):
    '''type : INT
            |  FLOAT
            |  CHAR
            |  STRING'''
            
def p_function(p):
    '''function : FUNC functionp LPAREN param RPAREN body'''
    
def p_functionp(p):
    '''functionp : type function
                 | VOID function'''
#checar si se puede vacio o epsilon
def p_param(p):
    '''param : 
             | type paramp'''

def p_paramp(p):
    ''' paramp : ID
               | ID RPAREN param'''
               
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
    '''f : LPAREN exp RPAREN
         | CONSI
         | CONSF
         | CONSCH
         | CONSSTR
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
    '''if : IF LPAREN exp RPAREN statement ifp'''
#checar si se puede vacio o epsilon    
def p_ifp(p):
    ''' ifp : 
            | ELSE statement'''

#checar como hacer el loop
def p_while(p):
    ''' while : WHILE LPAREN exp RPAREN statement whilep'''
    
def p_whilep(p):
    ''' whilep : SEMICOLON
               | statement whilep'''
#checar como hacer el loop    
def p_for(p):
    '''for : FOR LPAREN var SEMICOLON exp SEMICOLON exp RPAREN LBRACKET statement forp'''
    
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
    ''' array : ID EQUAL array LPAREN var arrayp'''
    
def p_arrayp(p):
    ''' arrayp : RPAREN
               | COMMA var RPAREN'''

def p_vector(p):
    ''' id : EQUAL array'''
    
def p_matrix(p):
    ''' matrix : ID EQUAL matrix LPAREN array matrixp'''
    
def p_matrixp(p):
    ''' matrixp : RPAREN
                | COMMA array RPAREN'''
                
def p_mean(p):
    '''mean : MEAN LPAREN array RPAREN'''
    
def p_layers(p):
    '''layers : ID EQUAL LAYERS LPAREN UNITS EQUAL CONSI RPAREN'''
    
def p_sequential(p):
    ''' sequential : ID EQUAL SEQUENTIAL LPAREN LBRACKET layers sequentialp'''
    
def p_sequentialp(p):
    ''' sequentialp : RBRACKET RPAREN
                    | COMMA layers sequentialp'''
                    
def p_compile(p):
    ''' compile : sequential DOT COMPILE LPAREN RPAREN'''
    
def p_fit(p):
    ''' fit : ID EQUAL sequential DOT FIT LPAREN array COMMA array COMMA EPOCHS EQUAL CONSI COMMA VERBOSE EQUAL fitp'''
    
def p_fitp(p):
    ''' fitp : TRUE RPAREN
             | FALSE RPAREN'''

def p_predict(p):
    ''' predict : ID EQUAL sequential DOT PREDICT LPAREN LBRACKET predictp'''
#Checar si se puede poner el - "cons-i"    
def p_predictp(p):
    ''' predictp : CONSI RBRACKET RPAREN
                 | CONSF RBRACKET RPAREN'''

def p_getweights(p):
    ''' getweights : layers DOT GETWEIGHTS LPAREN RPAREN'''