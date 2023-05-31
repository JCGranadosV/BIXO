#def p_matrix(p):
#    ''' matrix : MATRIX DOT ID EQUAL MATRIX LPAREN matrixp RPAREN SEMICOLON'''
#    global qCounter, local_var_table, regexFloat, regexInt, regexTemp, dimCounter, sDim, tempIntMemory, tempFloatMemory, tempCounterInt, tempCounterFloat
#    var_name=p[3]
#    k=[]
#    r=1
#    offset=0
#    size=0
#    temp=getTemp()
#    print("ENTRO AQUI")
#    print("DIMCOUNTER", dimCounter, sDim)
#    #si son mas de 3 dimensiones marca error
#    if dimCounter>3:
#        print("ERROR DEMASIADAS DIMENSIONES")
#    if dimCounter==0:
#        print("ERROR NO HAY DIMENSIONES")
#    #Revisa que exista la variable a la que la vamos a asignar
#    varExist(var_name)
#
#    if dimCounter==1:
#        currDim=sDim.pop()
#        lInf=0
#        lSup=currDim
#        r=r*(lSup-lInf+1)
#        m0=r
#        size=m0
#        m1=m0/(lSup-lInf+1)
#    elif dimCounter==2:
#        lSup1=sDim.pop()
#        lSup2=sDim.pop()
#        r=r*(lSup1+1)
#        r=r*(lSup2+1)
#        m0=r
#        size=m0
#        m1=m0/(lSup1+1)
#        m2=m1/(lSup2+1)
#    elif dimCounter==3:
#        lSup1=sDim.pop()
#        lSup2=sDim.pop()
#        lSup3=sDim.pop()
#        r=r*(lSup1+1)
#        r=r*(lSup2+1)
#        r=r*(lSup3+1)
#        size=r
#
#
#    #Revisa si la variable es un int o un float
#    if(var_name in (local_var_table["variables"]["varInt"])):
#        variable_type="varInt"
#        local_var_table["variables"]["tempInt"][temp]=tempIntMemory
#        tempIntMemory+=size
#        tempCounterInt+=1
#        quadGen.gen_quad('ARRAY', None, None, temp)
#        quadGen.gen_quad('=', temp, None, p[3])
#        qCounter += 2
#    elif(var_name in (local_var_table["variables"]["varFloat"])):
#        variable_type="varFloat"
#        local_var_table["variables"]["tempFloat"][temp]=tempFloatMemory
#        tempFloatMemory+=size
#        tempCounterFloat+=1
#        quadGen.gen_quad('ARRAY', None, None, temp)
#        quadGen.gen_quad('=', temp, None, p[3])
#        qCounter += 2
#    #print("size",size)
#    #ya que tengo el size se lo agrego a counter de espacios de memoria
#
#    #reset valores
#    dimCounter=1
#    sDim=[]
#    
#def p_matrixp(p):
#    ''' matrixp : exp
#                | exp COMMA matrixp'''
#    global dimCounter, sDim
#    if len(p)==2:
#        sDim.append(p[1])
#        dimCounter+=1
#    if len(p)==4:
#        sDim.append(p[1])
#        dimCounter+=1
#        p[0]=p[1]
#
#def p_fill_matrix(p):
#    '''fill_matrix : MATRIX FILL ID LBRACKET INT ']' '[' INT ']' '=' '[' matrix_values ']''''
#    matrix_name = p[1]
#    rows = p[3]
#    columns = p[6]
#    values = p[9]
#
#    # Verificar que la matriz exista en la tabla de símbolos
#    if matrix_name not in local_var_table['vars_table']['que']['variables']['varMatrix']:
#        raise ValueError(f"Matrix '{matrix_name}' is not declared.")
#
#    # Verificar que las dimensiones de la matriz coincidan con los valores proporcionados
#    if rows * columns != len(values):
#        raise ValueError(f"Invalid number of values for matrix '{matrix_name}'. Expected {rows * columns}, got {len(values)}.")
#
#    # Generar cuádruplos para llenar la matriz con los valores proporcionados
#    for i in range(rows):
#        for j in range(columns):
#            value = values[i * columns + j]
#            quad = ('=', value, None, f"{matrix_name}[{i}][{j}]")
#            quadruples.append(quad)

def p_matrixvalues(p):
    '''matrixvalues: exp
                   | exp COMMA matrixvalues'''
    print("ENTRA ACA")
    global sMatrixValues, mValues
    if len(p)==2:
        sMatrixValues.append(p[1])
        mValues+=1
    if len(p)==4:
        sMatrixValues.append(p[1])
        mValues+=1
        p[0]=p[1]