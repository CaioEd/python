# CORES NO TERMINAL

# \033[estilo,texto,cor-fundo m
# EX: \033[0;33;44m

# Estilo: 0-none, 1-negrito, 4-underline, 7-inverter
# Texto: Cores - 30 a 37
# Fundo: Cores - 40 a 47

print('\033[1;35;40mTeste\033[m')
print('\033[4;36;42mTestando as cores!\033[m')

a = 7
b = 5

print('Os valores são \033[32m{}\033[m e \033[34m{}\033[m'.format(a, b))