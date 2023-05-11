import ply.lex as lex

tokens = [
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'VAR',
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
    'SEQUENTIAL',
    'COMPILE',
    'FIT',
    'PREDICT',
    'GETWEIGHTS',
    #NUMPY
    'NUMPY',
    'ARRAY',
    'MATRIX',
    'MEAN'
]

reserved = {
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
    'listen' : 'READ_INPUT',
    'print' : 'PRINT',
    'void' : 'VOID'
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
t_DIFF = r'\<>'
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
t_VAR = r'var'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_PRINT = r'print'
t_READ = r'read'
t_ASSIGN = r'assign'
t_FUNCTION = r'function'
t_FUNCESP = r'funcesp'
t_VOID = r'void'
#LIBRERIAS DE ML:
#t_TENSORFLOW = r'tensorflow'
t_LAYERS = r'layers'
t_SEQUENTIAL = r'sequential'
t_COMPILE = r'compile'
t_FIT = r'fit'
t_PREDICT = r'predict'
t_GETWEIGHTS = r'getweights'
#NUMPY
t_NUMPY = r'numpy'
t_ARRAY = r'array'
t_MATRIX = r'matrix'
t_MEAN = r'mean'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
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