import ply.lex as lex

tokens = (
    'PROGRAM',
    'END',
    'MAIN',
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'CTI',
    'CTF',
    'VAR',
    'TRUE',
    'FALSE',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'GT',
    'GTE',
    'LT',
    'LTE',
    'EQUAL',
    'DIFF',
    'IFEQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'DOT',
    'SEMICOLON',
    'COLON',
    'QUOTE',
    'STRING',
    'IF',
    'ELSE',
    'AND',
    'OR',
    'WHILE',
    'FOR',
    'PRINT',
    'READ',
    'ASSIGN',
    'FUNCTION',
    'VOID',
    #LIBRERIAS DE ML:
    'FUNCESP',
    #'TENSORFLOW',
    'LAYERS',
    'UNITS',
    'SEQUENTIAL',
    'COMPILE',
    'FIT',
    'EPOCHS',
    'VERBOSE',
    'PREDICT',
    'GETWEIGHTS',
    #NUMPY
    'NUMPY',
    'ARRAY',
    'MATRIX',
    'MEAN'
)

reserved = {
    'program' : 'PROGRAM',
    'end' : 'END',
    'main' : 'MAIN',
    'var' : 'VAR',
    'type' : 'TYPE',
    'function' : 'FUNCTION',
    'read' : 'READ',
    'call' : 'CALL',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'string': 'STRING',
    'true': 'TRUE',
    'false': 'FALSE',
    'print' : 'PRINT',
    'void' : 'VOID',
    'epochs' : 'EPOCHS',
    'verbose' : 'VERBOSE'
}

#REGEX TOKENS

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_GT = r'\>'
t_GTE = r'>='
t_LT = r'\<'
t_LTE = r'<='
t_EQUAL = r'\='
t_AND = r'\&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_DOT = r'\.'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_QUOTE = r'\"'
t_STRING = r'\".*?\"'
#t_VAR = r'var'
t_TRUE = r'true'
t_FALSE = r'false'
t_FOR = r'for'
t_PRINT = r'print'
t_READ = r'read'
t_ASSIGN = r'assign'
t_FUNCESP = r'funcesp'
#LIBRERIAS DE ML:
#t_TENSORFLOW = r'tensorflow'
t_LAYERS = r'layers'
t_UNITS = r'units'
t_SEQUENTIAL = r'sequential'
t_COMPILE = r'compile'
t_FIT = r'fit'
t_EPOCHS = r'epochs'
t_VERBOSE = r'verbose'
t_PREDICT = r'predict'
t_GETWEIGHTS = r'getweights'
#NUMPY
t_NUMPY = r'numpy'
t_ARRAY = r'array'
t_MATRIX = r'matrix'
t_MEAN = r'mean'


def t_PROGRAM(t):
    r'program'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_END(t):
    r'end'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_VAR(t):
    r'var'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IFEQUAL(t):
    r'=='
    return t

def t_DIFF(t):
    r'!='
    return t

def t_WHILE(t):
    r'while'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_VOID(t):
    r'void'
    return t

def t_CTF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)


# Ignorar los espacios en blanco y los comentarios
t_ignore = ' \t\n'
t_ignore_COMMENT = r'\#.*'

lexer = lex.lex()