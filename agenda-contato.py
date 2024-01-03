continuar = True
codigo = []
nome = []
telefone = []

while continuar:
    print("=============================================")
    print("=         MINHA AGENDA DE CONTATOS          =")
    print("=============================================")
    print("=    1 - Novo Contato                       =")
    print("=    2 - Alterar Contato                    =")
    print("=    3 - Excluir Contato                    =")
    print("=    4 - Listar Todos os Contatos           =")
    print("=    5 - Listar por Código do Contato       =")
    print("=    6 - Listar por Nome do Contato         =")
    print("=    7 - Sair                               =")
    print("=============================================")
    opcao = int(input("Escolha a opção: "))
    print("=============================================")

    match opcao:
        case 1: # novo contato
            print("*********************************************")
            print("Novo Contato")
            print("*********************************************")
            aux_codigo = int(input("Informe o CÓDIGO do Contato  : "))
            aux_nome = input("Informe o NOME do Contato    : ")
            aux_telefone = input("Informe o TELEFONE do Contato: ")

            if aux_codigo in codigo:
                print("*********************************************")
                print(f"Contato com o Código {aux_codigo} já cadastrado.")
                print("*********************************************")
            else:
                contador = 0
                for i in codigo:
                    contador += 1
                
                if contador < 10:
                    codigo.append(aux_codigo)
                    nome.append(aux_nome)
                    telefone.append(aux_telefone)
                    print("*********************************************")
                    print(f"Contato com o Código {aux_codigo} cadastrado com sucesso.")
                    print("*********************************************")
                else:
                    print("*********************************************")
                    print("Limite de Contatos cadastrados esgotados.")
                    print("*********************************************")

        case 2: # alterar contato
            print("*********************************************")
            print("Alterar Contato")
            print("*********************************************")
            aux_codigo = int(input("Informe o CÓDIGO do Contato  : "))
            print("*********************************************")
            aux_nome = input("Informe o NOME do Contato    : ")
            aux_telefone = input("Informe o TELEFONE do Contato: ")
            print("*********************************************")

            if aux_codigo in codigo:
                for indice in codigo:
                    if aux_codigo == indice:
                        indice = aux_codigo
                        nome[indice] = aux_nome
                        telefone[indice] = aux_telefone
                        print("*********************************************")
                        print(f"Contato com o Código {aux_codigo} alterado com sucesso.")
                        print("*********************************************")
            else:
                print("*********************************************")
                print(f"Contato com o CÓDIGO: {aux_codigo} não cadastrado e não pode ser alterado.")
                print("*********************************************")

        case 3: # excluir contato
            print('*********************************************')
            print("Excluir Contato")
            print('*********************************************')
            aux_remove = int(input(f'informe o Codigo do Contato a ser removido: '))
            if aux_remove in codigo:
                deletar = codigo.index(aux_remove)
                del(codigo[deletar])
                del(nome[deletar])
                del(telefone[deletar])
                print('*********************************************')
                print(f"Sucesso!")
                print('*********************************************')
            else:
                print('*********************************************')
                print(f"Erro! não foi possivel remover o contato!")
                print('*********************************************')

        case 4: # listar todos os contatos
            print("*********************************************")
            print("Listar Todos os Contatos")
            print("*********************************************")
            contador = 0
            for i in codigo:
                contador += 1
            if contador == 0:
                print("Não há contatos cadastrados na Agenda de Contatos.")
                print("*********************************************")
            else:
                for i in range(contador):
                    print(f"CÓDIGO do Contato  : {codigo[i]}")
                    print(f"NOME do Contato    : {nome[i]}")
                    print(f"TELEFONE do Contato: {telefone[i]}")
                    print("*********************************************")

        case 5: # listar por código do contato
            print("*********************************************")
            print(f"Listar por Codigo do contato")
            print("*********************************************")
            aux_list_cod = int(input(f"Informe O Codigo do contato: "))
            print("*********************************************")
            if aux_list_cod in codigo:
                list_cod = codigo.index(aux_list_cod)
                print(f"Codigo do Contato: {codigo[list_cod]}")
                print(f"Nome do Contato: {nome[list_cod]}")
                print(f"Telefone do Contato: {telefone[list_cod]}")
            else:
                print(f"Erro! Não foi possivel listar Os contatos!")
                print("*********************************************")
        case 6: # listar por nome do contato
            print("*********************************************")
            print(f"Listar Por Nome do contato")
            print("*********************************************")
            aux_list_name = input(f"informe o Nome do Contato: ")
            print("*********************************************")
            if aux_list_name in nome:
                list_name = nome.index(aux_list_name)
                print(f"Codigo do Contato: {codigo[list_name]}")
                print(f"Nome do Contato: {nome[list_name]}")
                print(f"Telefone do Contato: {telefone[list_name]}")
            else:
                print(f"Erro! Não foi possivel listar Os contatos!")
            print("*********************************************")

        case 7:
            continuar = False
            
        case _:
            print("Opção inválida!")