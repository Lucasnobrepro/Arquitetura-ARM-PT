Base = '0100011000'

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

def find_CPY(linha):
    
    #identificador find_Mov_Cmp_Add_Suv_immed
    if len(linha) != 0 and len(linha) == 3:#--------------------------Se linha não for vazia
        if linha[0] == 'cpy':
            saida = Base
            print('intrução cpy Ld, Lm: ', linha)
            
            #Lm
            saida = regSwitch(saida, linha[2])
            
            #Ld
            saida = regSwitch(saida, linha[1][:-1])
            
            saida = hex(int(saida,2))
            
            return saida
        return -1
    return -1