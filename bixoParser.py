import ply.yacc as yacc
from bixoLexer import tokens

precedence = (
    #Checar que precences faltan (left o right)
    ('left','LT','LTE','GT','GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'GREATER', 'SMALLER', 'EQUAL', 'DIFF')
    ('left','LPAREN','RPAREN'),
    ('left','LBRACE','RBRACE'),
    ('left','LBRACKET','RBRACKET'),
)

#REGLAS ANALIZADOR SINTÁCTICO

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
    
def decvar(p):
    '''decvar : VAR decvarp '''

#Revisar declaración de cons-i
def decvarp(p):
    '''decvarp : type ID SEMICOLON decvarp
               | type ID LBRACKET '''
    

