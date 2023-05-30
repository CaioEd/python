def maior(*num):
    maiorNum = 0

    print(num, end=' ')

    print(f'Foram informados {len(num)} números.')

    for n in num:
        if n > maiorNum:
            maiorNum = n
    print(f'O maior número é {maiorNum}')


maior(5, 7, 3)
maior(10, 55, 67, 345, 900, 2)