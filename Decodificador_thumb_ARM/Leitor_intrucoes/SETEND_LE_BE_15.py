# Base
Base = '101101100101'

# Register bin
r0 = '000'
r1 = '001'
r2 = '010'
r3 = '011'
r4 = '100'
r5 = '101'
r6 = '110'
r7 = '111'


# Switch de reistradores menores
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
    elif linha == 'r7':
        saida += r7
        
    return saida


def find_SETEND_LE_BE(linha):
    if len(linha) != 0 and len(linha) == 2:
        if (linha[0] == 'setend' and linha[1] == 'le') or (linha[0] == 'setend' and linha[1] == 'be'):
            
            saida = Base
            
            if linha[1] == 'le':
                saida += '0'
                print('intruão setend le: ',linha)
                
            elif linha[1] == 'be':
                saida += '1'
                print('intruão setend be: ',linha)
            
            #Lm
            saida += '000'
            
            #converte para hexa
            saida = hex(int(saida,2))
            
            return saida
        return -1
    return -1