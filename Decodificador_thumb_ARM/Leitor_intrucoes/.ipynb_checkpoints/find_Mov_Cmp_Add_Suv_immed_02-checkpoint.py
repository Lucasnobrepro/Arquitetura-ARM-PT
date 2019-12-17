
## DEFINES
# Registradores
r0 = '000'
r1 = '001'
r2 = '010'
r3 = '011'
r4 = '100'
r5 = '101'
r6 = '110'
r7 = '111'

# comandos com valor imediato
cmp_op_im = '00101'
mov_op_im = '00100'
add_op_im = '00110'
sub_op_im = '00111'

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

# Encontra a intrução: [ MOV Rn, #immediate ]
def find_Mov_Cmp_Add_Suv_immed(linha):
    
    #identificador find_Mov_Cmp_Add_Suv_immed
    if len(linha) != 0 and len(linha) == 3:#--------------------------Se linha não for vazia
        if linha[0] == 'mov' or linha[0] == 'cmp' or linha[0] == 'add' or linha[0] == 'sub': #-------------------Verifica se a instrução é 'mov'
            
            # procura uma '#'  
            status = findImmed(linha)           
            
            # 01 - mov com imediato
            if status == True: 
                # binario do ADD
                if linha[0] == 'mov':
                    saida = mov_op_im
                elif linha[0] == 'cmp':
                    saida = cmp_op_im
                elif linha[0] == 'add':
                    saida = add_op_im
                elif linha[0] == 'sub':
                    saida = sub_op_im
                
                # numero imediato a ser usado sem o '#'.
                num = linha[2][1:]
                
                saida = regSwitch(saida,linha=linha[1][:-1])
                
                # binario do imediato
                
                num = str(bin(int(num)))[2:]
                
                # coloca os 0 faltantes do imediato
                
                while( len(num) < 8):
                    num = '0'+num
                
                saida += num
                saida = hex(int(saida,2))

                
                if linha[0] == 'mov':
                    print('É mov imed: ',linha)
                elif linha[0] == 'cmp':
                    print('É cmp imed: ',linha)
                elif linha[0] == 'add':
                    print('É add imed: ',linha)
                elif linha[0] == 'sub':
                    print('É sub imed: ',linha)
                
                return saida
            
    return -1    