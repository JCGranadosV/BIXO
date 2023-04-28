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


