
 #corregir strings y bool

semantic_cube = {
    'int': {
        '+': {
            'int': 'int',
            'float': 'float',
        },
        '-': {
            'int': 'int',
            'float': 'float',
        },
        '*': {
            'int': 'int',
            'float': 'float',
        },
        '/': {
            'int': 'float',
            'float': 'float',
        },
        '>': {
            'int': 'bool',
            'float': 'bool',
        },
        '<': {
            'int': 'bool',
            'float': 'bool',
        },
        '>=': {
            'int': 'bool',
            'float': 'bool',
        },
        '<=': {
            'int': 'bool',
            'float': 'bool',
        },
        '==': {
            'int': 'bool',
            'float': 'bool',
        },
        '!=': {
            'int': 'bool',
            'float': 'bool',
        },
        'and': {
            'bool': 'bool',
        },
        'or': {
            'bool': 'bool',
        }
    },
    'float': {
        '+': {
            'int': 'float',
            'float': 'float',
        },
        '-': {
            'int': 'float',
            'float': 'float',
        },
        '*': {
            'int': 'float',
            'float': 'float',
        },
        '/': {
            'int': 'float',
            'float': 'float',
        },
        '>': {
            'int': 'bool',
            'float': 'bool',
        },
        '<': {
            'int': 'bool',
            'float': 'bool',
        },
        '>=': {
            'int': 'bool',
            'float': 'bool',
        },
        '<=': {
            'int': 'bool',
            'float': 'bool',
        },
        '==': {
            'int': 'bool',
            'float': 'bool',
        },
        '!=': {
            'int': 'bool',
            'float': 'bool',
        },
        'and': {
            'bool': 'error',
        },
        'or': {
            'bool': 'error',
        }
    },
    'bool': {
        'and': {
            'bool': 'bool',
        },
        'or': {
            'bool': 'bool',
        },
        '==': {
            'bool': 'bool',
        },
        '!=': {
            'bool': 'bool',
        }
    },
    'char': {
        '==': {
            'char': 'bool',
        },
        '!=': {
            'char': 'bool',
        }
    },
    'string': {
        '+': {
            'string': 'string',
        },
        '==': {
            'string': 'bool',
        },
        '!=': {
            'string': 'bool',
        }
    }
}


# TESTING cubo semántico
#tipo1 = 'int'
#tipo2 = 'float'
#operacion = '/'
#if operacion in semantic_cube[tipo1]:
#    if tipo2 in semantic_cube[tipo1][operacion]:
#        tipo_resultado = semantic_cube[tipo1][operacion][tipo2]
#        print(f"El resultado de {tipo1} {operacion} {tipo2} es de tipo: {tipo_resultado}")
#    else:
#        print(f"Error: No se puede realizar la operación")


        