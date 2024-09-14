import os

# Lista de dicionários representando restaurantes com nome, categoria e status (ativo ou inativo).
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


def exibir_nome_do_programa():
    """
    Função para exibir o título artístico do programa na tela.
    Mostra uma arte com o nome do programa.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    # Exibe as opções disponíveis para o usuário no menu principal.

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    # Função chamada para encerrar o aplicativo.

    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    # Espera o usuário pressionar uma tecla e retorna ao menu principal.

    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    # Exibe uma mensagem quando uma opção inválida é escolhida.

    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Exibe um título com linhas decorativas acima e abaixo do texto.
    Usado para organizar as seções do programa.

    :param texto: Título ou subtítulo a ser exibido.
    """
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Permite ao usuário cadastrar um novo restaurante, coletando nome e categoria,
    e adiciona o restaurante à lista de 'restaurantes'.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {
                      nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    #  Exibe a lista de restaurantes cadastrados, mostrando nome, categoria e status (ativado/desativado).

    exibir_subtitulo('Listando restaurantes')
    print(f'{"Nome do restaurante".ljust(22)} | {
          "Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)
                   } | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alterna o status 'ativo' de um restaurante (entre ativado e desativado),
    com base no nome fornecido pelo usuário.
    """

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {
                nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Função para capturar a escolha do usuário e redirecioná-lo para a função apropriada
    com base na opção escolhida.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """
    Função principal que limpa a tela, exibe o nome do programa,
    exibe as opções disponíveis e aguarda a escolha do usuário.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
