
preco = float(input('Digite o preço do produto: '))

if preco < 20.00:

    desconto1 = preco * 0.05

    valor1 = preco + desconto1

    print('Valor do produto  com acréscimo {} '.format(valor1))

    if valor1 < 40.00:

        print('barato')

    elif valor1 > 40.00 and valor1 <= 80.00:

        print('normal')

    elif valor1 > 40.00 and valor1 <= 120.00:

        print('caro')

    elif valor1 > 120.00:

        print('muito caro')

if 20.00 < preco < 80.00:

    desconto2 = preco * 0.10

    valor2 = preco + desconto2

    print('Valor do produto  com acréscimo {}'.format(valor2))

    if valor2 < 40.00:

        print('barato')

    elif valor2 > 40.00 and valor2 <= 80.00:

        print('normal')

    elif valor2 > 40.00 and valor2 <= 120.00:

        print('caro')

    elif valor2 > 120.00:

        print('muito caro')

if preco > 80.00:

    desconto3 = preco * 0.15

    valor3 = preco + desconto3

    print('Valor do produto  sem acréscimo {} '.format(preco))

    print('Valor do produto  com acréscimo {} '.format(valor3))

    if valor3 < 40.00:

        print('barato')

    elif valor3 > 40.00 and valor3 <= 80.00:

        print('normal')

    elif valor3 > 40.00 and valor3 <= 120.00:

        print('caro')

    elif valor3 > 120.00:

        print('muito caro')
