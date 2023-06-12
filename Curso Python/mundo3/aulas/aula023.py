try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a/b
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except KeyboardInterrupt:
    print('O usuário não informou os dados.')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('FIM')