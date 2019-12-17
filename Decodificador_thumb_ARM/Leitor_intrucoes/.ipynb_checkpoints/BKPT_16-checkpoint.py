# Base
Base = '10111110'

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


# Indentifica se é imediato #
def findImmed(linha):
    
    if len(linha) == 2:
        num = linha[1]
        if num[0] == '#':
            return True
    # add e sub rd_rs_rn
    elif len(linha) == 6:
        num = linha[5]
        if num[0] == '#':
            return True
    #em caso que nenhuma das condições sejam feitas.
    return False


def find_BKPT(linha):
    
    if len(linha) != 0 and len(linha) == 2:
        if (linha[0] == 'bkpt'):
            print('intrução BKPT #immed')
            saida = Base
            
            num = linha[1][1:]
            
            # tranforma o immediato e binario
            num = str(bin(int(num)))[2:]
                
                # coloca os 0 faltantes do imediato
            while( len(num) < 8):
                 num = '0'+num
                
            saida += num
                
            saida = hex(int(saida,2))
               
            return saida       
        return -1
    return -1
            