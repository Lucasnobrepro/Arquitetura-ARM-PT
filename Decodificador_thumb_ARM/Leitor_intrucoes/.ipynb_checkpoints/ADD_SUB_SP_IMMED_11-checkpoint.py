# Base
Base = '10110000'

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
    
    if len(linha) == 3:
        num = linha[2]
        if num[0] == '#':
            return True
    # add e sub rd_rs_rn
    elif len(linha) == 6:
        num = linha[5]
        if num[0] == '#':
            return True
    #em caso que nenhuma das condições sejam feitas.
    return False

def find_ADD_sub_sp_IMMED(linha):
    
    if len(linha) != 0 and len(linha) == 3:
        if (linha[0] == 'add' and (linha[1][:-1] == 'sp' or linha[1][:-1] == 'r13') ) or (linha[0] == 'add' and (linha[1][:-1] == 'pc' or linha[1][:-1] == 'r15') ):
            
            status = findImmed(linha)
            
            if status == True:
                
                saida = Base
                
                if linha[0] == 'add':
                    saida += '0'
                    print(' Add sp, #immed: ', linha)
                
                elif linha[0] == 'sub':
                    saida += '1'
                    print(' Sub sp, #immed: ', linha)
                    
                
                num = linha[2][1:]
                
                # tranforma o immediato e binario
                num = str(bin(int(num)))[2:]
                
                # coloca os 0 faltantes do imediato
                while( len(num) < 7):
                    num = '0'+num
                
                saida += num
                
                saida = hex(int(saida,2))
                
                return saida
            return -1
        return -1
    return -1
            
            