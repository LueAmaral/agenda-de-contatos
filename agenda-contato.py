"""
Desenvolvido por:
Lue Rodrigues do Amaral
Ygor Samuel Nanes de Oliveira
Ultima modificação: 07/12/2023
"""

def menu(): # função para exibir o menu principal
    print("=" * 45)
    print("=         MINHA AGENDA DE CONTATOS          =")
    print("=" * 45)
    print("=    1 - Novo Contato                       =")
    print("=    2 - Alterar Contato                    =")
    print("=    3 - Excluir Contato                    =")
    print("=    4 - Listar Todos os Contatos           =")
    print("=    5 - Listar por Código do Contato       =")
    print("=    6 - Listar por Nome do Contato         =")
    print("=    7 - Sair                               =")
    print("="*45)
    opcao = int(input("Escolha a opção: "))
    print("=" * 45)
    return opcao

def novo_contato(aux_codigo): # função para cadastrar novo contato

    if aux_codigo in codigo: # verifica se o código já existe
        print("*" * 45)
        print(f"Contato com o Código {aux_codigo} já cadastrado.")
        print("*" * 45)
    
    else: # se não existir, conta quantos contatos já existem
        contador = 0
        for i in codigo:
            contador += 1
        
        if contador < 10: # se tiver menos de 11 contatos, cadastra
            aux_nome = input("Informe o NOME do Contato    : ")
            aux_telefone = input("Informe o TELEFONE do Contato: ")

            codigo.append(aux_codigo)
            nome.append(aux_nome)
            telefone.append(aux_telefone)
            print("*" * 45)
            print(f"Contato com o Código {aux_codigo} cadastrado com sucesso.")
            print("*" * 45)
        
        else: # se tiver 10 contatos, não cadastra
            print("*" * 45)
            print("Limite de Contatos cadastrados esgotados.")
            print("*" * 45)

def alterar_contato(aux_codigo): # função para alterar contato

    if aux_codigo in codigo: # verifica se o código existe
        alterar = codigo.index(aux_codigo) # se existir, pega o índice do código
        aux_nome = input("Informe o NOME do Contato    : ")
        aux_telefone = input("Informe o TELEFONE do Contato: ")
        print("*" * 45)

        # alterar o contato
        telefone[alterar] = aux_telefone
        nome[alterar] = aux_nome
        print("*" * 45)
        print(f"Contato com o Código {aux_codigo} alterado com sucesso.")
        print("*" * 45)
        
    else:
        print(f"Contato com o Código {aux_codigo} não cadastrado e não pode ser alterado.")
        print("*" * 45)

def excluir_contato(aux_remove):
    if aux_remove in codigo:
        deletar = codigo.index(aux_remove)
        del(codigo[deletar])
        del(nome[deletar])
        del(telefone[deletar])
        print("*" * 45)
        print(f"Sucesso!")
        print("*" * 45)
    else:
        print("*" * 45)
        print(f"Erro! não foi possivel remover o contato!")
        print("*" * 45)

def listar_todos_contatos(): # função para listar todos os contatos
    print("*" * 45)
    print("Listar Todos os Contatos")
    print("*" * 45)
    contador = 0

    for i in codigo: # conta quantos contatos existem
        contador += 1

    if contador == 0: # se não existir nenhum contato, não lista
        print("Não há contatos cadastrados na Agenda de Contatos.")
        print("*" * 45)

    else: # se existir, lista todos
        for i in range(contador):
            print(f"CÓDIGO do Contato  : {codigo[i]}")
            print(f"NOME do Contato    : {nome[i]}")
            print(f"TELEFONE do Contato: {telefone[i]}")
            print("*" * 45)

def list_por_cod(aux_list_cod):
    if aux_list_cod in codigo:
        list_cod = codigo.index(aux_list_cod)
        print(f"Codigo do Contato: {codigo[list_cod]}")
        print(f"Nome do Contato: {nome[list_cod]}")
        print(f"Telefone do Contato: {telefone[list_cod]}")
    else:
        print(f"Erro! Não foi possivel listar Os contatos!")
        print("*" * 45)

def list_por_nome(aux_list_name):
    if aux_list_name in nome:
        list_name = nome.index(aux_list_name)
        print(f"Codigo do Contato: {codigo[list_name]}")
        print(f"Nome do Contato: {nome[list_name]}")
        print(f"Telefone do Contato: {telefone[list_name]}")
    else:
        print(f"Erro! Não foi possivel listar Os contatos!")
        print("*" * 45)

continuar = True
codigo = []
nome = []
telefone = []
while continuar:
    opcao = menu()

    match opcao:
        case 1: # novo contato
            print("*" * 45)
            print("Novo Contato")
            print("*" * 45)
            aux_codigo = int(input("Informe o CÓDIGO do Contato  : "))
            
            novo_contato(aux_codigo)

        case 2: # alterar contato
            print("*" * 45)
            print("Alterar Contato")
            print("*" * 45)
            aux_codigo = int(input("Informe o CÓDIGO do Contato  : "))
            print("*" * 45)

            alterar_contato(aux_codigo)
            

        case 3: # excluir contato
            print("*" * 45)
            print("Excluir Contato")
            print("*" * 45)
            aux_remove = int(input(f'informe o Codigo do Contato a ser removido: '))

            excluir_contato(aux_remove)

        case 4: # listar todos os contatos
            listar_todos_contatos()

        case 5: # listar por código do contato
            print("*" * 45)
            print(f"Listar por Codigo do contato")
            print("*" * 45)
            aux_list_cod = int(input(f"Informe O Codigo do contato: "))
            print("*" * 45)

            list_por_cod(aux_list_cod)

        case 6: # listar por nome do contato
            print("*" * 45)
            print(f"Listar Por Nome do contato")
            print("*" * 45)
            aux_list_name = input(f"informe o Nome do Contato: ")
            print("*" * 45)

            list_por_nome(aux_list_name)

        case 7:
            continuar = False
            
        case _:
            print("Opção inválida!")