# *-* encoding: utf-8 *-*
DEBUG = True
# Discriminacion de la entrada, para achicar las columnas de la tabla
tipo_entrada = {
    '0' : 'cero',
    '1' : 'digito',
    '2' : 'digito',
    '3' : 'digito',
    '4' : 'digito',
    '5' : 'digito',
    '6' : 'digito',
    '7' : 'digito',
    '8' : 'digito',
    '9' : 'digito',
    '+' : 'operacion',
    '-' : 'operacion',
    '*' : 'operacion',
    '/' : 'operacion',
    '=' : 'igual',
    'c' : 'clear'
}

# Algunas definicones para indexar en las tuplas
FUNCIONES = 1
PROXIMO_ESTADO = 0
# Automata de la calculadora
# [estado][estimulo] ('nuevo_estado', ['accion1', <'accion2>'])
automata = {
    'en_cero'   : {
        'cero':      ('cero', [] ),
        'digito':    ('primer_dig', ['establecer']),
        'operacion': ('operando', ['almacenar']),
        'igual':     ('cero',[]),
        'clear':     ('en_cero',['limpiar']),
    },
    'primer_dig': {
        'cero':      ('primer_dig',['actualizar']),
        'digito':    ('primer_dig',['actualizar']),
        'operacion': ('operando',  ['guardar_op', 'almacenar']),
        'igual':     ('resultado', ['almacenar']),
        'clear':     ('en_cero',['limpiar']),
    },
    'operando': {
        'cero':      ('cero_dos', ['establecer']),
        'digito':    ('segundo_dig', ['establecer']),
        'operacion': ('resultado', ['operar']),
        'igual':     ('resultado',['operar']),
        'clear':     ('en_cero',['limpiar']),
    },
    'cero_dos': {
        'cero':      ('cero_dos', []),
        'digito':    ('segundo_dig',['establecer']),
        'operacion': ('cero_dos', []),
        'iugal':     ('cero_dos', []),
        'clear':     ('en_cero',['limpiar']),
    },
    'segundo_dig' : {
        'cero':      ('segundo_dig', ['actualizar']),
        'digito':    ('segundo_dig', ['actualizar']),
        'operacion': ('resultado', ['guardar_op','operar']),
        'igual':     ('resultado', ['operar']),
        'clear':     ('en_cero',['limpiar']),
    },
    'resultado': {
        'cero':      ('en_cero', ['establecer']),
        'digito':    ('primer_dig', ['establecer']),
        'operacion': ('operando',['almacenar', 'guardar_op']),
        'igual':     ('resultado',[]),
        'clear':     ('en_cero',['limpiar']),
    },
}

def ejecutar_automata( caracter, vista ):
    '''Ejecuta la logia de la caluladora.'''
    entrada = tipo_entrada[str(caracter)]
    transicion = automata[ getattr(vista, "estado") ][entrada]
    # Realizar la lista de acciones relacionadas con el cambio de estado
    # si es que existen...
    if transicion[FUNCIONES]:
        for i in transicion[FUNCIONES]:
            if DEBUG:
                print "estado %s -> %s(%s)" % (getattr(vista, "estado") ,i, caracter)
            accion = getattr(vista, i)
            accion(caracter)

    if DEBUG:
        print "Cambiando a %s" % (transicion[PROXIMO_ESTADO])
    setattr(vista, "estado", transicion[PROXIMO_ESTADO])
