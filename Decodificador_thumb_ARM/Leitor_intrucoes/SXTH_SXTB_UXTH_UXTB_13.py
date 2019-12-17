# Base
Base = '10110010'

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





def find_SXTH_SXTB_UXTH_UXTB(linha):
    if len(linha) != 0 and len(linha) == 3:
        if linha[0] == 'sxth' or linha[0] == 'sxtb' or linha[0] == 'uxth' or linha[0] == 'uxtb':
            saida = Base
            
            if linha[0] == 'sxth':
                saida += '00'
                print('intruão sxth: ',linha)
                
            elif linha[0] == 'sxtb':
                saida += '01'
                print('intruão sxtb: ',linha)
                
            elif linha[0] == 'uxth':
                saida += '10'
                print('intruão uxth: ',linha)
                
            elif linha[0] == 'uxtb':
                saida += '11'
                print('intruão uxtb: ',linha)
            
            #Lm
            saida = regSwitch(saida,linha=linha[2])
            
            #Ld
            saida = regSwitch(saida,linha=linha[1][:-1])
            
            #converte para hexa
            saida = hex(int(saida,2))
            
            return saida
        return -1
    return -1
            