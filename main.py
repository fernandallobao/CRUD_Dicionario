# Crie, em Python, um CRUD de usuários completo (Cadastrar, Pesquisar/Listar, Alterar e Excluir).
# O programa deverá:

# - Cadastrar usuário
# - Listar todos os usuários
# - Alterar os dados do usuário
# - Excluir usuário
# - Sair do programa

# O usuário deverá cadastrar:

# - Nome completo
# - Data de Nascimento
# - CPF
# - Profissão
# - E-mail
# - Endereço
# - Telefone

pessoas = []

while True:
    pessoa = {}

    print('\n')
    print('Escolha uma opção:')
    print('1 - Cadastrar um novo usuário')
    print('2 - Mostrar todos os usuários')
    print('3 - Alterar um usuário')
    print('4 - Deletar um usuário')
    print('5 - Sair')

    #usuario digita o numero da opçao, le como strig
    op = input(f'Digite o índice da ação que deseja fazer: ')

    match op:
        case '1': #cadastra
            pessoa['nome'] = input('Informe o nome: ')
            pessoa['data_nascimento'] = int(input('Informe a data de nascimento: '))
            pessoa['cpf'] = int(input('Informe o CPF: '))
            pessoa['profissao'] = input('Informe a profissão: ')
            pessoa['email'] = input('Informe o e-mail: ')
            pessoa['endereco'] = input('Informe o endereço: ')
            pessoa['telefone'] = input('Informe o telefone: ')
            pessoas.append(pessoa)
            print('Novo usuário cadastrado com sucesso!')
            
        case '2': #lista todo mundo
            for i in range(len(pessoas)):
                print('\n')
                print(f'Índice: {i + 1}:')
                print(f'Nome: {pessoas[i]['nome']}')
                print(f'Data de nascimento: {pessoas[i]['data_nascimento']}')
                print(f'CPF: {pessoas[i]['data_nascimento']}')
                print(f'Profissão: {pessoas[i]['profissao']}')
                print(f'E-mail: {pessoas[i]['email']}')
                print(f'Endereço: {pessoas[i]['endereco']}')
                print(f'Telefone: {pessoas[i]['telefone']}')

        case '3': #altera
            for i in range(len(pessoas)):
                print('\n')
                print(f'Índice: {i + 1}:')
                print(f'Nome: {pessoas[i]['nome']}')
                print(f'Data de nascimento: {pessoas[i]['data_nascimento']}')
                print(f'CPF: {pessoas[i]['data_nascimento']}')
                print(f'Profissão: {pessoas[i]['profissao']}')
                print(f'E-mail: {pessoas[i]['email']}')
                print(f'Endereço: {pessoas[i]['endereco']}')
                print(f'Telefone: {pessoas[i]['telefone']}')

            indice = int(input('Informe o índice do usuário a ser alterado: '))
            campo = input('Informe o nome do campo a ser alterado: ')

            # usuário altera o dado do campo desejado
            try:
                pessoas[indice][campo] = input(f'Informe o novo valor do campo {campo}: ')
                # mostra os dados que foram alterados do usuario escolhido
                print('\n')
                print(f'Novos dados do índice {indice}:\n')
                print(f'Nome: {pessoas[i]['nome']}')
                print(f'Data de nascimento: {pessoas[i]['data_nascimento']}')
                print(f'CPF: {pessoas[i]['data_nascimento']}')
                print(f'Profissão: {pessoas[i]['profissao']}')
                print(f'E-mail: {pessoas[i]['email']}')
                print(f'Endereço: {pessoas[i]['endereco']}')
                print(f'Telefone: {pessoas[i]['telefone']}')
            except:
                print('Não foi possível alterar usuário.')

        case '4': #deleta
            for i in range(len(pessoas)):
                print('\n')
                print(f'Índice: {i + 1}:')
                print(f'Nome: {pessoas[i]['nome']}')
                print(f'Data de nascimento: {pessoas[i]['data_nascimento']}')
                print(f'CPF: {pessoas[i]['data_nascimento']}')
                print(f'Profissão: {pessoas[i]['profissao']}')
                print(f'E-mail: {pessoas[i]['email']}')
                print(f'Endereço: {pessoas[i]['endereco']}')
                print(f'Telefone: {pessoas[i]['telefone']}')

            # usuário informa o índice a ser excluído
            indice = int(input('Informe o índice do usuário que deseja deletar da lista de dicionários:'))
           
            indice -= 1
            # índice é deletado
            try:
                del[pessoas[indice]]
                print('Usuário deletado com sucesso!')
            except:
                print('Não foi possível deletar o índice.')


        case '5':
            break

print('Progama encerrado!')