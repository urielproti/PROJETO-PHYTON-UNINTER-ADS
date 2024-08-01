# Questão 03

# Mensagem de boas-vindas
print("Bem-vindo à Copiadora do Uriel")

# Tipo de  serviço desejado
def escolha_servico():
    while True:
        servico = input("Entre com o tipo de serviço desejado\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n>> ").lower()
        if servico == 'dig':
            return 1.10
        elif servico == 'ico':
            return 1.00
        elif servico == 'ipb':
            return 0.40
        elif servico == 'fot':
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente.")

# Obter o número de páginas e aplicar  o desconto caso necessário
def num_pagina():
    while True:
        try:
            num_paginas = int(input("Entre com o número de páginas: "))
            if num_paginas > 20000:
                print("Não aceitamos tantas páginas de uma vez. Ultrapassou o limite de páginas.")
                print("Por favor, entre com o número de páginas novamente.")
            else:
                if num_paginas < 20:
                    return num_paginas
                elif num_paginas < 200:
                    return num_paginas * 0.85
                elif num_paginas < 2000:
                    return num_paginas * 0.80
                elif num_paginas < 20000:
                    return num_paginas * 0.75
        except ValueError:
            print("Valor não numérico. Por favor, insira um número válido.")

# Função para escolher o serviço adicional
def servico_extra():
    while True:
        try:
            extra = input("Deseja adicionar algum serviço?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura - R$ 40.00\nO - Não desejo mais nada\n>> ").lower()
            if extra == '1':
                return 15.00
            elif extra == '2':
                return 40.00
            elif extra == 'o':
                return 0
            else:
                print("Escolha inválida, entre com o tipo do serviço novamente.")
        except ValueError:
            print("Valor não numérico. Por favor, insira um número válido.")

# Código principal
if __name__ == "__main__":
    # Escolher o serviço
    valor_servico = escolha_servico()

    # Obter o número de páginas com desconto aplicado caso necessário
    num_paginas = num_pagina()

    # Escolher o serviço adicional
    valor_extra = servico_extra()

    # Calcular o total a pagar
    total = (valor_servico * num_paginas) + valor_extra

    # Exibir o valor total a pagar
    print(f"Total: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {num_paginas} + extra: {valor_extra:.2f})")


