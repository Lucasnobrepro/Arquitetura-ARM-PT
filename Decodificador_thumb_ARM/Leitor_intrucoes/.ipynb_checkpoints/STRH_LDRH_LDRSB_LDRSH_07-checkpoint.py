Base = '0101'

r0 = '000'
r1 = '001'
r2 = '010'
r3 = '011'
r4 = '100'
r5 = '101'
r6 = '110'
r7 = '111'


# Switch de reistradores
def regSwitch(saida, linha):
    
    # binario do Primeiro 'RG'
    if linha == 'r0':
        saida += r0
    elif linha == 'r1':
        saida += r1
    elif linha == 'r2':
        saida += r2
    elif linha == 'r3':
        saida += r3
    elif linha == 'r4':
        saida += r4
    elif linha == 'r5':
        saida += r5
    elif linha == 'r6':
        saida += r6
    else:
        saida += r7
        
    return saida

# Indentifica se é imediato #
def findImmed(linha):
    
    if len(linha) == 4:
        num = linha[3]
        if num[0] == '#':
            return True
    # add e sub rd_rs_rn
    elif len(linha) == 6:
        num = linha[5]
        if num[0] == '#':
            return True
    #em caso que nenhuma das condições sejam feitas.
    return False

def find_STRH_LDRH_LDRSB_LDRSH(linha):
     #identificador find_Mov_Cmp_Add_Suv_immed
    if len(linha) != 0 and len(linha) == 4:#--------------------------Se linha não for vazia
        if linha[0] == 'ldrh' or linha[0] == 'strh' or linha[0] == 'ldsb' or linha[0] == 'ldsh':
            
            status = findImmed(linha)
            
            if status == False:
                # saida = 0101
                saida = Base
                
                if linha[0] == 'ldrh':
                    # saida = base + h + s + 1 
                    saida += '1'+ '0'+ '1'
                    
                    # Reistrador Ro
                    saida = regSwitch(saida,linha[3][:-1])

                    # Registrador Rb
                    saida = regSwitch(saida,linha=linha[2][1:-1])

                    # Registrador Rd
                    saida = regSwitch(saida,linha=linha[1][:-1])

                    saida = hex(int(saida,2))

                    print('ldrh Rd,[Rb, Ro]: ', linha)

                    return saida
            
                elif linha[0] == 'strh':
             # saida = base + h + s + 1 
                    saida += '0'+ '0'+ '1'
                    
                    # Reistrador Ro
                    saida = regSwitch(saida,linha[3][:-1])

                    # Registrador Rb
                    saida = regSwitch(saida,linha=linha[2][1:-1])

                    # Registrador Rd
                    saida = regSwitch(saida,linha=linha[1][:-1])

                    saida = hex(int(saida,2))

                    print('strh Rd,[Rb, Ro]: ', linha)

                    return saida

                elif linha[0] == 'ldsh':
             # saida = base + h + s + 1 
                    saida += '1'+ '1'+ '1'       
                    
                    # Reistrador Ro
                    saida = regSwitch(saida,linha[3][:-1])

                    # Registrador Rb
                    saida = regSwitch(saida,linha=linha[2][1:-1])

                    # Registrador Rd
                    saida = regSwitch(saida,linha=linha[1][:-1])

                    saida = hex(int(saida,2))

                    print('LDSH Rd,[Rb, Ro]: ', linha)

                    return saida
                
                elif linha[0] == 'ldsb':
             # saida = base + h + s + 1 
                    saida += '0'+ '1'+ '1'
                    
                    
                    # Reistrador Ro
                    saida = regSwitch(saida,linha[3][:-1])

                    # Registrador Rb
                    saida = regSwitch(saida,linha=linha[2][1:-1])

                    # Registrador Rd
                    saida = regSwitch(saida,linha=linha[1][:-1])

                    saida = hex(int(saida,2))

                    print('ldsb Rd,[Rb, Ro]: ', linha)

                    return saida
                
            return -1    
        
        return -1    
    
    return -1        
            
            