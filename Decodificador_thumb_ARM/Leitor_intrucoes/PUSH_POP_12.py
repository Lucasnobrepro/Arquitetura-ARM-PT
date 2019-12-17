# Base
Base = '1011'

Base1 = '1100'

# Register bin
r0 = '000'
r1 = '001'
r2 = '010'
r3 = '011'
r4 = '100'
r5 = '101'
r6 = '110'
r7 = '111'


# Register bin_one
one_r0 = '00000001'
one_r1 = '00000010'
one_r2 = '00000100'
one_r3 = '00001000'
one_r4 = '00010000'
one_r5 = '00100000'
one_r6 = '01000000'
one_r7 = '10000000'


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

# register list
def find_range(saida,linha):
    
    range_ = []
    for i in range (8):
        range_.append(0)
    
    if len(linha[1]) == 7 and len(linha) == 2:
        menor = int(linha[1][2:3])
        maior = int(linha[1][5:6])
        
        for each in range (menor, maior+1, 1):
            range_[each] = 1
        
        #range_ = np.invert(range_)
        range_.reverse()

        h = ''
        for d in range_:
            if d == 0 or d == 1:
                h += str(d)

        saida += h
        return saida    
        
    elif len(linha[1]) == 4 and len(linha) == 2:
        menor = int(linha[1][2:3])
        
        for each in range (menor, menor+1, 1):
            range_[each] = 1
        
        #range_ = np.invert(range_)
        range_.reverse()

        h = ''
        for d in range_:
            if d == 0 or d == 1:
                h += str(d)

        saida += h
        return saida 
        
        
    elif len(linha[2]) == 7 and len(linha) == 3:
        menor = int(linha[2][2:3])
        maior = int(linha[2][5:6])
        
        for each in range (menor, maior+1, 1):
            range_[each] = 1
        
        #range_ = np.invert(range_)
        range_.reverse()

        h = ''
        for d in range_:
            if d == 0 or d == 1:
                h += str(d)

        saida += h
        return saida
    
    elif len(linha[2]) == 4 and len(linha) == 3:
        menor = int(linha[2][2:3])
        
        for each in range (menor, menor+1, 1):
            range_[each] = 1
        
        #range_ = np.invert(range_)
        range_.reverse()

        h = ''
        for d in range_:
            if d == 0 or d == 1:
                h += str(d)

        saida += h
        return saida 


def find_push_pop_registeList(linha):
    
    if len(linha) != 0 and len(linha) == 2:
        if linha[0] == 'push' or linha[0] == 'pop':
            #1011
            saida = Base
            
            if linha[0] == 'push':
                #1011 + L + 10 + R 
                saida += '0' + '10' + '0'
            elif linha[0] == 'pop':    
                saida += '1' + '10' + '0'
            
            saida = find_range(saida,linha)
            saida = hex(int(saida,2))
            
            return saida
        return -1
    elif len(linha) != 0 and len(linha) == 3:
        if linha[0] == 'stmia' or linha[0] == 'ldmia':
            saida = Base1
            
            if linha[0] == 'stmia':
                #1011 + L + 10 + R 
                saida += '0' 
            elif linha[0] == 'ldmia':    
                saida += '1' 
            
            # pega o Ln 
            saida = regSwitch(saida,linha[1][:-2])
            
            saida = find_range(saida,linha)
            
            saida = hex(int(saida,2))
            
            return saida
        return -1
    return -1

    
