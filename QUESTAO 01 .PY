#Questao01

# mensagem de boas vindas
print("bem-vindo à loja do Uriel")
# capturar o input do usuario
valor = input("entre com o valor do produto ")
# transformar o input de string para float
valor = float(valor)
# capturar o imput do usuario
quantidade = input("entre com a quantidade do produto ")
# transformar o input de string para int
quantidade = int(quantidade)
# multiplicar os inputs do usuario
resultado = valor * quantidade
# imprimir o resultado do calculo
print("valor sem desconto:" + str(resultado))
# criar as condições impostas no enunciado
if resultado < 2500:
    resultadoFinal = resultado * 1
elif resultado < 6000:
    resultadoFinal = resultado * 0.96
elif resultado < 10000:
    resultadoFinal = resultado * 0.93
else:
    resultadoFinal = resultado * 0.89
#imprimir o resultado final
print("valor com desconto:" + str(resultadoFinal))
