# VALOR SENO, COSSENO E TANGENTE

import math

print('DESCUBRA O SENO, COSSENO E TANGENTE DO ÂNGULO!')

ang = float(input('Digite o ângulo:'))

sen = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O valor do seno é {:.2f} \n O valor do cosseno é {:.2f} \n O valor da tangente é {:.2f}' .format(sen, coss, tang))