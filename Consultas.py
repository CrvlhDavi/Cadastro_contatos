def apresentacao():
    print('-'*10, '|', 'Lista de Contatos' ,'|', '-' * 9 )
    
lista_contatos = [] 
id_global = 1    
def cadastrar_contato(id):
    global id_global
    print('-' * 55)
    print(f'ID para contato: {id}')
    nome = input('Entre com nome do contato: ')
    funcao = input('Entre com a função do contato: ')

    while True:
        ddd = input('Entre com o DDD (2 dígitos): ')
        if not ddd.isdigit() or len(ddd) != 2:
            print('DDD inválido. Deve conter exatamente 2 dígitos numéricos.')
            continue
        break

    while True:
        telefone_num = input('Entre com o telefone (9 dígitos): ')
        if not telefone_num.isdigit() or len(telefone_num) != 9:
            print('Telefone inválido. Deve conter exatamente 9 dígitos numéricos.')
            continue
        break

    telefone = f'({ddd}) {telefone_num[:5]}-{telefone_num[5:]}'

    contato = {
        'id': id,
        'nome': nome,
        'funcao': funcao,
        'telefone': telefone
    }
    
    lista_contatos.append(contato.copy()) 
    id_global += 2    
    
def consultar_contatos():
    while True:
        print('Menu consultar')
        print('1 - Consultar todos ')
        print('2 - Consultar por ID')
        print('3 - Consultar por Função')
        print('4 - voltar ao menu')
        print("-" * 46)

        opcao = input('Escolha uma das opções: ')
        
        if opcao == '1': # 
            for contato in lista_contatos:
                for chave, valor in contato.items():
                    print(f"{chave}: {valor}")
                print("-" * 20)

        elif opcao == '2': 
            try:
                id_busca = int(input('Id do contato: '))
                encontrado = False
                for contato in lista_contatos:
                    if contato['id'] == id_busca:
                        for chave, valor in contato.items():
                            print(f'{chave}: {valor}')
                        encontrado = True
                        print("-" * 20)
                        break
                if not encontrado:
                    print("ID não encontrado.")
            except ValueError:
                print("ID inválido.")
                      
        elif opcao == '3': # 
            funcao_busca = input('Por favor digite a função do contato:  ') 
            for contato in lista_contatos:
                if contato['funcao'].lower() == funcao_busca.lower():
                    for chave, valor in contato.items():
                        print(f'{chave} :{valor}')
                    print("-" * 20)
        
        elif opcao == '4': 
            return
            
        else:
            print('opção invalida')
def remover_contato():
    while True:
        try:
            id_remover = int(input("Digite o ID do contato a ser removido: "))
            for contato in lista_contatos:
                if contato['id'] == id_remover:
                    lista_contatos.remove(contato)
                    print("Contato removido com sucesso!")
                    return
            print("Id inválido") 
        except ValueError:
            print("Por favor, digite um valor numérico para o ID.")
                           
if __name__ == "__main__": 
    apresentacao()
        
    while True:
        print("-" * 42)
        print("-" * 13 + " MENU PRINCIPAL " + "-" * 13)
        print('|', ' ' * 8, "1) Cadastrar Contato", ' '*8, '|')
        print('|', ' ' * 8, "2) Consultar Contato" , ' '*8, '|' )
        print('|', ' ' * 8, "3) Remover Contato", ' '*10, '|')
        print('|', ' ' * 8, "4) Encerrar Programa", ' '*8, '|')
        print("-" * 42)
        
        escolha = input("Escolha a opção desejada: ")
        
        if escolha == '1':
            cadastrar_contato(id_global)
        elif escolha == '2':
            consultar_contatos()
        elif escolha == '3':
            remover_contato()
        elif escolha == '4':
            print("Encerrando programa..")
            break 
        else:
            print("Opção inválida")
      	