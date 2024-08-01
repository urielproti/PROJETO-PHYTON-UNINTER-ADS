#  Boas-vindas
print("Bem-vindo à Livraria do Uriel Proti")

#  Lista vazia e variável id_global
lista_livro = []
id_global = 0

def print_livro(livro):
    print("id " + str (livro["id"]))
    print("nome " + livro["nome"])
    print("autor " + livro["autor"])
    print("editora " + livro["editora"])

#  Função cadastrar_livro
def cadastrar_livro(id):
    print("------------------------------------------------------")
    print("--------------- MENU CADASTRAR LIVRO -----------------")
  
    global id_global
   
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    id_global += 1

#  Função consultar_livro

def consultar_livro():
    print("------------------------------------------------------")
    print("--------------- CONSULTAR LIVRO ----------------------")
    opcao = input("Escolha uma opção (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu): ")
    if opcao == '1':
        for livro in lista_livro:
            print_livro(livro)
    elif opcao == '2':
        id_consulta = int(input("Digite o ID do livro que deseja consultar: "))
        for livro in lista_livro:
            if livro['id'] == id_consulta:
                print_livro(livro)
                break
        else:
            print("Livro não encontrado.")
    elif opcao == '3':
        autor_consulta = input("Digite o nome do autor que deseja consultar: ")
        for livro in lista_livro:
            if livro['autor'] == autor_consulta:
                print_livro(livro)
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")
        consultar_livro()

#  Função remover_livro


def remover_livro():
    print("-----------------------------------------------------")
    print("---------------REMOVER LIVRO-- ----------------------")
    id_remover = int(input("Digite o ID do livro que deseja remover: "))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            return
    else:
        print("ID inválido.")
        remover_livro()

#  Menu principal
while True:
    
    print("\nMenu:")
    print("-----------------------------------------------------")
    print("--------------- MENU PRINCIPAL ----------------------")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Sair")
    opcao_principal = input("Escolha uma opção: ")

    if opcao_principal == '1':
        cadastrar_livro(id_global)
    elif opcao_principal == '2':
        consultar_livro()
    elif opcao_principal == '3':
        remover_livro()
    elif opcao_principal == '4':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

    

#  Lista de dicionários
# Já implementado ao longo do código com a lista lista_livro

#  Comentários relevantes no código
# Comentários foram adicionados ao longo do código para explicar cada seção

# Saída de Console 1: Mensagem de boas-vindas
# Já implementada no início do código

# Saída de Console 2: Cadastro de 3 livros
cadastrar_livro(id_global)
cadastrar_livro(id_global)
cadastrar_livro(id_global)

# Saída de Console 3: Consulta de todos os livros
consultar_livro()

# Saída de Console 4: Consulta por ID de um livro
consultar_livro()

# Saída de Console 5: Consulta por autor
consultar_livro()

# Saída de Console 6: Remoção de um livro seguida de consulta de todos os livros
remover_livro()
