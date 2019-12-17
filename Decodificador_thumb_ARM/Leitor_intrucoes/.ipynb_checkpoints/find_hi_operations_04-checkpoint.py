# BINARIO  BASE DA INTRUÇÃO
Base = '010001'

# BINARIO DA OPERAÇÃO
BIN_ADD = '00'
BIN_CMP = '01'
BIN_MOV = '10'

# BINARIO DIFERECIADOR DA INTRUÇÃO
BIN_Ld_Hm = '01'
BIN_Hd_Lm = '10'
BIN_Hd_Hm = '11'

# Register bin
r0 = '000'
r1 = '001'
r2 = '010'
r3 = '011'
r4 = '100'
r5 = '101'
r6 = '110'
r7 = '111'

# São iguais aos de cima por que fazem uma AND com 7
r8 = '000'
r9 = '001'
r10 = '010'
r11 = '011'
r12 = '100'
r13 = '101'
r14 = '110'
r15 = '111'


def indentifica_ALTO(linha):
    if linha == 'r8' or linha == 'r9' or linha == 'r10' or linha == 'r11' or linha == 'r12' or linha == 'r13' or linha == 'r14' or linha == 'r15':
        return True
    
    return False
    

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

# Switch de reistradores
def regSwitch_Maiores(saida, linha):
    
    # binario do Primeiro 'RG'
    if linha == 'r8':
        saida += r8
    elif linha == 'r9':
        saida += r9
    elif linha == 'r10':
        saida += r10
    elif linha == 'r11':
        saida += r11
    elif linha == 'r12':
        saida += r12
    elif linha == 'r13':
        saida += r13
    elif linha == 'r14':
        saida += r14
    elif linha == 'r15':
        saida += r15
        
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

def find_hi_operations(linha):
    
    
    # Se linha não for vazia e o tamanho for 3
    # R0-R7 é low.
    # R8-R15 é high
    if len(linha) != 0 and len(linha) == 3:
        if linha[0] == 'add' or linha[0] == 'cmp' or linha[0] == 'mov':
            
            # procura uma '#'  
            status = findImmed(linha) 
            
            if status == False:
                # saida = 010001
                saida = Base
                
                if linha[0] == 'add':
                    
                    #saida = 010001 + 00 
                    saida += BIN_ADD
                    if indentifica_ALTO(linha[1][:-1]) == False and indentifica_ALTO(linha[2]) == True:
                        # saida = 010001 + 00 + 01
                        saida += BIN_Ld_Hm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 00 + 01 + Rs 
                        saida = regSwitch_Maiores(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 00 + 01 + Rs + Rd
                        saida = regSwitch(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É add LD, Hm: ', linha)
                        
                        # Devolve a saida
                        return saida
                    
                    # ADD Hd, Lm
                    elif indentifica_ALTO(linha[1][:-1]) == True and indentifica_ALTO(linha[2]) == False:
                        # saida = 010001 + 00 + 10
                        saida += BIN_Hd_Lm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 00 + 01 + Rs 
                        saida = regSwitch(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 00 + 01 + Rs + Rd
                        saida = regSwitch_Maiores(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É add Hd, Lm: ', linha)
                        
                        # Devolve a saida
                        return saida
                                                                                      
                    # ADD Hd, Hm    
                    elif indentifica_ALTO(linha[1][:-1]) == True and indentifica_ALTO(linha[2]) == True:
                        # saida = 010001 + 00 + 11
                        saida += BIN_Hd_Hm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 00 + 11 + Rs 
                        saida = regSwitch_Maiores(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 00 + 01 + Rs + Rd
                        saida = regSwitch_Maiores(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É add Hd, Hm: ', linha)
                        
                        # Devolve a saida
                        return saida
                ##########################################################################
                # MOV
                elif linha[0] == 'mov':
                    
                    #saida = 010001 + 10 
                    saida += BIN_MOV

                    # MOV Ld,Hm
                    if indentifica_ALTO(linha[1][:-1]) == False and indentifica_ALTO(linha[2]) == True:
                        # saida = 010001 + 10 + 01
                        saida += BIN_Ld_Hm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 10 + 01 + Rs 
                        saida = regSwitch_Maiores(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 00 + 01 + Rs + Rd
                        saida = regSwitch(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É mov LD, Hm: ', linha)
                        
                        # Devolve a saida
                        return saida
                    
                    # MOV Hd, Lm
                    elif indentifica_ALTO(linha[1][:-1]) == True and indentifica_ALTO(linha[2]) == False:
                        # saida = 010001 + 10 + 10
                        saida += BIN_Hd_Lm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 10 + 10 + Rs 
                        saida = regSwitch(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 00 + 01 + Rs + Rd
                        saida = regSwitch_Maiores(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É mov Hd, Lm: ', linha)
                        
                        # Devolve a saida
                        return saida
                                                                                      
                    # MOV Hd, Hm    
                    elif indentifica_ALTO(linha[1][:-1]) == True and indentifica_ALTO(linha[2]) == True:
                        # saida = 010001 + 10 + 11
                        saida += BIN_Hd_Hm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 10 + 11 + Rs 
                        saida = regSwitch_Maiores(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 10 + 11 + Rs + Rd
                        saida = regSwitch_Maiores(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É mov Hd, Hm: ', linha)
                        
                        # Devolve a saida
                        return saida
#####################################################################################################                           # CMP
                elif linha[0] == 'cmp':
                                                                                      
                    # saida = 010001 + 01                                                                 
                    saida += BIN_CMP                                                                  
                    if indentifica_ALTO(linha[1][:-1]) == False and indentifica_ALTO(linha[2]) == True:
                        # saida = 010001 + 01 + 01
                        saida += BIN_Ld_Hm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 01 + 01 + Rs 
                        saida = regSwitch_Maiores(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 01 + 01 + Rs + Rd
                        saida = regSwitch(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É cmp LD, Hm: ', linha)
                        
                        # Devolve a saida
                        return saida
                    
                    # CMP Hd, Lm
                    elif indentifica_ALTO(linha[1][:-1]) == True and indentifica_ALTO(linha[2]) == False:
                        # saida = 010001 + 01 + 10
                        saida += BIN_Hd_Lm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 01 + 10 + Rs 
                        saida = regSwitch(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 01 + 10 + Rs + Rd
                        saida = regSwitch_Maiores(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É cmp Hd, Lm: ', linha)
                        
                        # Devolve a saida
                        return saida
                                                                                      
                    # MOV Hd, Hm    
                    elif indentifica_ALTO(linha[1][:-1]) == True and indentifica_ALTO(linha[2]) == True:
                        # saida = 010001 + 01 + 11
                        saida += BIN_Hd_Hm
                        
                        # Pego registrador Rs esse faz parte => R8-R15
                        # saida = 010001 + 01 + 11 + Rs 
                        saida = regSwitch_Maiores(saida,linha=linha[2])
                        
                        # Pego registrador Rd esse faz parte => R0-R7
                        # saida = 010001 + 01 + 11 + Rs + Rd
                        saida = regSwitch_Maiores(saida,linha=linha[1][:-1])
                        
                        # Tranforma em hexadecimal
                        saida = hex(int(saida,2))
                        
                        # Print a intrução
                        print('É cmp Hd, Hm: ', linha)
                        
                        # Devolve a saida
                        return saida                                                                 
                                                                                        
            # Quando status == True            
            return -1            
        # Quando não encontra a instrução
        return -1                
    # Quando o tamanho não fo correto                    
    elif len(linha) != 0 and len(linha) == 2:
        saida = Base + '11'
        
        if indentifica_ALTO(linha[1]) == False and linha[0] == 'bx':
            saida += '00'
            
            saida = regSwitch(saida,linha=linha[1])
            
            saida += '000'
            
            saida = hex(int(saida,2))
                        
            # Print a intrução
            print('É Bx Rs: ', linha)
            
            return saida
            
        elif indentifica_ALTO(linha[1]) == True and linha[0] == 'blx':
            saida +='01'
            
            saida = regSwitch_Maiores(saida,linha=linha[1])
            
            saida += '000'
            
            saida = hex(int(saida,2))
                        
            # Print a intrução
            print('É Blx Hs: ', linha)
            
            return saida
    
    return -1