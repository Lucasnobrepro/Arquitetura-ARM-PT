# str, ldr immed
Base1 = '0110'
# strb, ldrb immed
Base2 = '0111'
# strh, ldrh immed
Base3 = '1000'

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

def find_ldr_str_immed(linha):
    if len(linha) != 0 and len(linha) == 4:#--------------------------Se linha não for vazia
        if (linha[0] == 'ldr' or linha[0] == 'str' or linha[0] == 'ldrb' or linha[0] == 'strb' or linha[0] == 'strh' or linha[0] == 'ldrh') and linha[2][1:-1] != 'pc':
            
            status = findImmed(linha)
            
            if status == True:
                if linha[0] == 'ldr': 
                    saida = Base1 + '1'
                    
                elif linha[0] == 'str':
                    saida = Base1 + '0'
                    
                elif linha[0] == 'ldrb': 
                    saida = Base2 + '1'
                    
                elif linha[0] == 'strb':
                    saida = Base2 + '0'
                    
                elif linha[0] == 'ldrh': 
                    saida = Base3 + '1'
                    
                elif linha[0] == 'strh':
                    saida = Base3 + '0'
                # numero imediato a ser usado sem o '#'.
                num = linha[3][1:-1]
                
                #convetendo numero
                num = str(bin(int(num)))[2:]
                
                # completando o numero com zeros
                while( len(num) < 5):
                    num = '0'+num               
                    
                saida += num
                
                # pega Ln
                saida = regSwitch(saida,linha=linha[2][1:-1])
                
                # pea Ld
                saida = regSwitch(saida,linha=linha[1][:-1])
                
                #converte para hexa
                saida = hex(int(saida,2))
                
                
                if linha[0] == 'ldr': 
                    print('É ldr Ld, [Ln, #immed]: ', linha)
                elif linha[0] == 'str':
                    print('É str Ld, [Ln, #immed]: ', linha)
                elif linha[0] == 'ldrb': 
                    print('É ldrb Ld, [Ln, #immed]: ', linha)
                elif linha[0] == 'strb':
                    print('É strb Ld, [Ln, #immed]: ', linha)
                elif linha[0] == 'ldrh': 
                    print('É ldrh Ld, [Ln, #immed]: ', linha)
                elif linha[0] == 'strh':
                    print('É strh Ld, [Ln, #immed]: ', linha)
                
                return saida
            return -1
        return-1
    return -1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
