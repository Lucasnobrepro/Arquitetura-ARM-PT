# Base das operações
Base = '010000'

# BIN's DA LINHA DE OPERAÇÃO.

AND_EOR_LSL_LSR = '00'# --linha 1
ASR_ADC_SBC_ROR = '01'# --linha 2
TST_NEG_CMP_CMN = '10'# --linha 3
ORR_MUL_BIC_MVN = '11'# --linha 4

#BIN's DE OPERAÇÃO DE TODAS AS LINHAS:
#--Bin's de operação da linha 1
BIN_AND = '00'
BIN_EOR = '01'
BIN_LSL = '10'
BIN_LSR = '11'
#--Bin's de operação da linha 2
BIN_ASR = '00'
BIN_ADC = '01'
BIN_SBC = '10'
BIN_ROR = '11'
#--Bin's de operação da linha 3
BIN_TST = '00'
BIN_NEG = '01'
BIN_CMP = '10'
BIN_CMN = '11'
#--Bin's de operação da linha 3
BIN_ORR = '00'
BIN_MUL = '01'
BIN_BIC = '10'
BIN_MVN = '11'


# Register bin
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


# INTRUÇÕES DA ULA
# --AND, EOR, LSL, LSR => status = OK
# --ASR, ADC, SBC, ROR => status = fazer
# --TST, NEG, CMP, CMN => status = fazer
# --ORR, MUL, BIC, MVN => status = fazer

# Encontra operaões da ULA
def find_ULA_operations(linha):
    
    
    # Se linha não for vazia e o tamanho for 3
    if len(linha) != 0 and len(linha) == 3:
        #print(linha)
        # verifica se a instrução faz parte do conjunto analizado pela função
        
        # LINHA1 = AND, EOR, LSL e LSR
        if linha[0] == 'and' or linha[0] == 'eor' or linha[0] == 'lsl' or linha[0] == 'lsr':
          # saida = 010000 + 00
            saida = Base + AND_EOR_LSL_LSR
            
            # saida = 010000 + 00 + opcode(2bits)
            if linha[0] == 'and': # and Rd, Rs
                # saida = 010000 + 00 + 00
                saida += BIN_AND
                print('É ULA-and:')
            elif linha[0] == 'eor':
                # saida = 010000 + 00 + 01
                saida += BIN_EOR
                print('É ULA-eor:')
            elif linha[0] == 'lsl':
                # saida = 010000 + 00 + 10
                saida += BIN_LSL
                print('É ULA-lsl:')
            elif linha[0] == 'lsr':
                # saida = 010000 + 00 + 11
                saida += BIN_LSR
                print('É ULA-lsr:')
                
            # saida = 010000 + 00 + opcode(2bits) + Rs(3bits)
            saida = regSwitch(saida,linha=linha[2])
            
            # saida = 010000 + 00 + opcode(2bits) + Rs(3bits) + Rd(3bits)
            saida = regSwitch(saida,linha=linha[1][:-1])
            
            # Transformando a saida de string para binario para hexadecimal
            saida = hex(int(saida,2))            
            
            # retorna o Hexadecimal    
            return saida
        
        # LINHA2 = ASR, ADC, SBC, ROR
        elif linha[0] == 'asr' or linha[0] == 'adc' or linha[0] == 'sbc' or linha[0] == 'ror':
                        
            saida = Base + ASR_ADC_SBC_ROR
            
            # saida = 010000 + 01 + opcode(2bits)
            if linha[0] == 'asr': # and Rd, Rs
                # saida = 010000 + 01 + 00
                saida += BIN_AND
                print('É ULA-asr:')
                
            elif linha[0] == 'adc':
                # saida = 010000 + 01 + 01
                saida += BIN_EOR
                print('É ULA-adc:')
                
            elif linha[0] == 'sbc':
                # saida = 010000 + 01 + 10
                saida += BIN_LSL
                print('É ULA-sbc:')
                
            elif linha[0] == 'ror':
                # saida = 010000 + 01 + 11
                saida += BIN_LSR
                print('É ULA-ror:')
                
            # saida = 010000 + 01 + opcode(2bits) + Rs(3bits)
            saida = regSwitch(saida,linha=linha[2])
            
            # saida = 010000 + 01 + opcode(2bits) + Rs(3bits) + Rd(3bits)
            saida = regSwitch(saida,linha=linha[1][:-1])
            
            # Transformando a saida de string para binario para hexadecimal
            saida = hex(int(saida,2))            
            
            # retorna o Hexadecimal    
            return saida
        
        # LINHA3 = TST_NEG_CMP_CMN
        elif linha[0] == 'tst' or linha[0] == 'neg' or (linha[0] == 'cmp' and linha[2][0] != '#') or linha[0] == 'cmn':
                        
            saida = Base + TST_NEG_CMP_CMN
            
            # saida = 010000 + 01 + opcode(2bits)
            if linha[0] == 'tst': # and Rd, Rs
                # saida = 010000 + 10 + 00
                saida += BIN_TST
                print('É ULA-tst:')
                
            elif linha[0] == 'neg':
                # saida = 010000 + 10 + 01
                saida += BIN_NEG
                print('É ULA-neg:')
                
            elif linha[0] == 'cmp':
                # saida = 010000 + 10 + 10
                saida += BIN_CMP
                print('É ULA-cmp:')
                
            elif linha[0] == 'cmn':
                # saida = 010000 + 10 + 11
                saida += BIN_CMN
                print('É ULA-cmn:')
                
            # saida = 010000 + 10 + opcode(2bits) + Rs(3bits)
            saida = regSwitch(saida,linha=linha[2])
            
            # saida = 010000 + 10 + opcode(2bits) + Rs(3bits) + Rd(3bits)
            saida = regSwitch(saida,linha=linha[1][:-1])
            
            # Transformando a saida de string para binario para hexadecimal
            saida = hex(int(saida,2))            
            
            # retorna o Hexadecimal    
            return saida
        
        # LINHA4 = ORR_MUL_BIC_MVN
        elif linha[0] == 'orr' or linha[0] == 'mul' or linha[0] == 'bic' or linha[0] == 'mvn':
                        
            saida = Base + ORR_MUL_BIC_MVN
            
            # saida = 010000 + 11 + opcode(2bits)
            if linha[0] == 'orr': # and Rd, Rs
                # saida = 010000 + 11 + 00
                saida += BIN_TST
                print('É ULA-orr:')
                
            elif linha[0] == 'mul':
                # saida = 010000 + 11 + 01
                saida += BIN_NEG
                print('É ULA-mul:')
                
            elif linha[0] == 'bic':
                # saida = 010000 + 11 + 10
                saida += BIN_CMP
                print('É ULA-bic:')
                
            elif linha[0] == 'mvn':
                # saida = 010000 + 11 + 11
                saida += BIN_CMN
                print('É ULA-mvn:')
                
            # saida = 010000 + 11 + opcode(2bits) + Rs(3bits)
            saida = regSwitch(saida,linha=linha[2])
            
            # saida = 010000 + 11 + opcode(2bits) + Rs(3bits) + Rd(3bits)
            saida = regSwitch(saida,linha=linha[1][:-1])
            
            # Transformando a saida de string para binario para hexadecimal
            saida = hex(int(saida,2))            
            
            # retorna o Hexadecimal    
            return saida
        
        else:
            return -1
            
        
    return -1        
            
            
            
            





































