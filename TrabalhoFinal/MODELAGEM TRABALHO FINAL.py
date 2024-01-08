# FUNÇÃO OBJETIVA
min x12*2 + x21*2 + x13*10 + x31*10 + x23*5 + x32*5

# RESTRIÇÃO PARA CORES
#PRETO
y1 + y2 >= 1 

#AZUL
y3 >= 1

# RESTRIÇÃO DE ARESTAS
#NÓ 0
x01 + x02 + x03 = 1

# NÓ 1
x14 + x12 + x13 = x21 + x31 + x01 -> x14 + x12 + x13 - (x21 + x31 + x01) = 0

# NÓ 2
x21 + x23 + x24 = x12 + x32 + x02

# NÓ 3
x31 + x32 + x34 = x13 + x23 + x03

# NÓ 4
x14 + x24 + x34 = 1

# RESTRIÇÃO ENTRE ARESTAS E VÉRTICES
# NÓ 1: PRETO
x01 + x21 + x31 >= y1

#NÓ 2: PRETO
x02 + x12 + x32 >= y2

#NÓ 3: AZUL
x03 + x13 + x23 >= y3



# TODAS AS ARESTAS QUE CHEGAM EM DETERMINADO NÓ TEM Q SER MAIOR IGUALA A 1






