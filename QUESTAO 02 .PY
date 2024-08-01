#Questão02

print('Bem-vindo à loja do Uriel')
print('---------------------Cardápio----------------------')
print('------| Tamanho | Cupucaçu (CP) | Açaí (AC) |------')
print('------|    P    |    R$ 9,00    |  R$ 11,00 |------')
print('------|    M    |    R$ 14,00   |  R$ 16,00 |------')
print('------|    G    |    R$ 18,00   |  R$ 20,00 |------')
print('---------------------------------------------------')

acumulador = 0
while True:
    sabor=input('Entre com o sabor desejado (CP/AC): ')
    sabor = sabor.upper()

    if sabor != 'AC' and sabor != 'CP':
        print('Sabor Inválido. Tente novamente')
        continue
    print('') #adicionado para que o resultado fique compativel com o exemplo do professor

    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    tamanho = tamanho.upper()

    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente')
        continue

    preco = 0

    if tamanho == 'P' and sabor == 'CP':
        preco = 9

    elif tamanho == 'P' and sabor == 'AC':
        preco = 11

    elif tamanho == 'M' and sabor == 'CP':
        preco = 14

    elif tamanho == 'M' and sabor == 'AC':
        preco = 16

    elif tamanho == 'G' and sabor == 'CP':
        preco = 18

    elif tamanho == 'G' and sabor == 'AC':
        preco = 20

    acumulador = acumulador + preco

    sabor_extenso = ''
    if sabor == 'AC':
        sabor_extenso = 'AÇAÍ'
    elif sabor == 'CP':
        sabor_extenso = 'CUPUAÇU'

    print('Você pediu ' + sabor_extenso + ' no tamanho ' + tamanho +': R$' + str(preco) + ',00')

    satisfeito = input('Deseja mais alguma coisa (s/ditige outra tecla)?: ') 
    satisfeito = satisfeito.upper()

    if satisfeito != 'S':
        break

print('O valor total a ser pago: R$' + str(acumulador) + ',00')
