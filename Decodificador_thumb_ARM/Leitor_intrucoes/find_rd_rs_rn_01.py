# comandos com registradores e com immediato
add_immed_rs_rd = '0001110'
sub_immed_rs_rd = '0001111'

add_Rg_rs_rd = '0001100'
sub_Rg_rs_rd = '0001101'


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

# ADD Rd, Rs, Rn , Sub Rd, Rs, Rn, ADD Rd, Rs, #immedi e Sub Rd, Rs, #immed
def find_Add_sub_rd_rs_rn(linha):
    
    #identificador find_Mov_Cmp_Add_Suv_immed
    if len(linha) != 0 and len(linha) == 4:#--------------------------Se linha não for vazia
        if linha[0] == 'add' or linha[0] == 'sub': #-------------------Verifica se a instrução é 'mov'
            
            # procura uma '#'  
            status = findImmed(linha)           
            
            # 01 - mov com imediato
            if status == True: 
                # binario do ADD
                if linha[0] == 'add':
                    saida = add_immed_rs_rd
                elif linha[0] == 'sub':
                    saida = sub_immed_rs_rd
                
                num = linha[3][1:]
                
                # binario do imediato
                num = str(bin(int(num)))[2:]
                
                # coloca os 0 faltantes do imediato
                while( len(num) < 3):
                    num = '0'+num
                
                saida += num
                
                # Reistrador Rs
                saida = regSwitch(saida,linha[2][:-1])
                
                # Registrador Rd
                saida = regSwitch(saida,linha=linha[1][:-1])
                
                saida = hex(int(saida,2))
                
                c = saida
                #
                
                if linha[0] == 'add':
                    print('É add imed: ')
                elif linha[0] == 'sub':
                    print('É sub imed: ')
                
                return saida
            
            else:# ADD rd, rs, rm e SUB rd, rs, rm
                
                # binario das operações
                if linha[0] == 'add':
                    saida = add_Rg_rs_rd
                elif linha[0] == 'sub':
                    saida = sub_Rg_rs_rd
                
                num = linha[3]
                # Rn
                saida = regSwitch(saida,linha=linha[3])
                
                # Reistrador Rs
                saida = regSwitch(saida,linha=linha[2][:-1])
                
                # Registrador Rd
                saida = regSwitch(saida,linha=linha[1][:-1])
                
                saida = hex(int(saida,2))
                
                c = saida
                #
                
                if linha[0] == 'add':
                    print('É add Reg: ')
                elif linha[0] == 'sub':
                    print('É sub reg: ')
                
                return saida
        
            #print('É mov: ')
            
    return -1   