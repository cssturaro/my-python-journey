import os

# Classe de usuário
class User:
    def __init__(self, id, nome, email, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade
        
# Lista com todos os usuários
users = []

# FUNÇÃO PRINCIPAL DO PPROGRAMA
def main():
    while True:
        # Limpar tela
        os.system("cls" if os.name == "nt" else "clear")

        # Opções principais
        print("===============================\n")
        print("      Sistema de Usuários      \n")
        print("         O que deseja?      \n")
        print("      1 - adicionar usuário      ")
        print("      2 - listar usuários      ")
        print("      3 - buscar usuário      ")
        print("      4 - Fechar Programa      \n")
        print("===============================\n")

        # Pedido de input para escolha de opção
        option = input("> ")

        # Validação da opção
        match option:
            case "1":
                criarUser()
            case "2":
                listarUsers()
            case "3":
                buscarUser()
            case "4":
                print("Finalizando programa")
                break
            case _:
                input("Opção invalida, pressione [ENTER] para tentar novamente")


# --- FUNÇÃO CRIAR USUÁRIOS
def criarUser():
    os.system("cls" if os.name == "nt" else "clear")

    print("===== Criar novo usuário =====")
    # Definição de atributos do usuário
    id = str(len(users))
        
    nome = input("Nome do usuário: ")
    email = input("Email do usuário: ")
    idade = input("Idade do usuário: ")

    # Adiciona usuário à lista de usuários
    novo_user = User(id, nome, email, idade)
    users.append(novo_user)
        
    # Pergunta se deseja criar novo usuário
    while True:
        option = input("\n[S] para criar novo usuário [N] Para parar de criar usuários\n\n> ")

        if option in {"N", "n"}:
            return # Retorna esta função para voltar ao loop da função main (que já está ativo)
        elif option not in {"S", "s"}:
            input("Opção inválida. Pressione [ENTER] para tentar novamente")
            continue # Volta ao início do loop de seleção de [S] ou [N]
        
        criarUser() # Volta pra função de criar usuário
        return
                

# --- FUNÇÃO LISTAGEM DE USUÁRIOS
def listarUsers():
    # Seleção de tipo de listagem (Simples ou Completa)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        option = input("[1] Para listagem simples [2] Para listagem completa\n\n> ")
        if option in {"1", "2"} : break
        input("Opção inválida. Pressione [ENTER] para tentar novamente")


    os.system("cls" if os.name == "nt" else "clear")

    # Listagem
    print("===============================\n")
    print("      Listagem de usuários\n")
    
    if option == "1":
        for user in users: # Listagem simples de usuários registrados
            print(f"{user.id} - {user.nome}")
    if option == "2":
        for user in users: # Listagem completa de usuários registrados
            print(f"{user.id} - {user.nome} | {user.email} | {user.idade} anos")

    if not users : print("  Não há usuários registrados") # Caso não haja usuários registrados
    print("===============================\n")
    input("Pressione [ENTER] para voltar à tela principal")
    return

# --- FUNÇÃO DE BUSCA
def buscarUser():
    # Seleção de opção de busca: por ID ou nome
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        option = input("[1] Para buscar por id [2] Para buscar por nome\n\n> ")
        if option in {"1", "2"} : break
        input("Opção inválida. Pressione [ENTER] para tentar novamente")
           
    encontrado = False

    print("===================================")

    # Busca por ID
    if option == "1":
        id_buscado = input("Digite o ID do seu usuário\n\n> ")
        for user in users: # Loop na lista de usuários em busca de um ID corresppondente 
            if  id_buscado == user.id:
                print(f"{user.id} - {user.nome} | {user.email} | {user.idade} anos")
                encontrado = True # Para avisar ao sistema que um ID correspondente foi encontrado
                break

    # Busca por nome
    if option == "2":
        nome_buscado = input("Digite o nome do seu usuário\n\n> ")
        for user in users: # Loop na lista de usuários em busca de um nome correspondente 
            if  nome_buscado.lower() in user.nome.lower():
                print(f"{user.id} - {user.nome} | {user.email} | {user.idade} anos")
                encontrado = True # Para avisar ao sistema que ao menos um nome foi encontrado

    if not encontrado: input("Nenhum usuário encontrado. Pressione [ENTER] para continuar")

    print("===================================")

    while True:
        option = input("\n[S] para buscar novamente [N] Para para retornar ao menu inicial\n\n> ")

        if option in {"N", "n"}:
            return # Retorna esta função para voltar ao loop da função main (que já está ativo)
        elif option not in {"S", "s"}:
            input("Opção inválida. Pressione [ENTER] para tentar novamente")
            continue # Volta ao início do loop de seleção de [S] ou [N]
        
        buscarUser() # Volta pra função de buscar usuáriro
        return
            
# --- INICIA PROGRAMA   
main()
