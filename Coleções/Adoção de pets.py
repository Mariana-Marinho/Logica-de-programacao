def cadastrado(dicionario, lista):
    """ retorna falso se algum animal informado nao estiver na lista """
    for nome in lista:
        if nome not in dicionario:
            return False
    return True


def adotados(dicionario, lista):
    """ printa as necessidades dos animais que serão adotados """
    print(f'Segue aqui as necessidades dos animais:')

    for nome in lista:
        print(f'As necessidades do(a) {nome} são:')

        for frase in dicionario.get(nome).get('necessidades'):
            print(f'- {frase};')

    print('Dito isso, vamos adotá-los!!!')


def ler_inimigos(lista):
    """ printa os inimigos de acordo com a ordem do input """

    inimigos = {
        'cachorro': ['gato'],
        'gato': ['cachorro', 'hamster', 'peixe'],
        'hamster': ['cachorro', 'gato'],
        'peixe': ['gato']
    }

    for animal in lista:
        # criar uma lista com os outros para comparar se é inimigo
        comparativo = lista.copy()
        comparativo.remove(animal)

        for inimigo in comparativo:
            if inimigo in inimigos[animal]:
                print(
                    f'Sérgio, o(a) {animal} tem o(a) {inimigo} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos')


animais = {
    'cachorro': {'necessidades': ('coleira', 'ração', 'ursinho de pelúcia')},
    'gato': {'necessidades': ('bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo')},
    'hamster': {'necessidades': ('ração', 'roda para hamster', 'serragem')},
    'peixe': {'necessidades': ('aquário', 'filtro', 'ração')}
}

entrada = input().split()
for x in entrada:
    if x == 'e':
        entrada.remove('e')
n = input()

if cadastrado(animais, entrada):
    if n == 'sim':
        print(f'Como os animais são recém nascidos, eles podem ser adotados juntos!')
        adotados(animais, entrada)

    else:
        if entrada.count(entrada[0]) != len(entrada):
            # se os animais informados forem de especies diferentes
            if 'gato' in entrada or ('cachorro' in entrada and 'hamster' in entrada):
                ler_inimigos(entrada)
            else:
                adotados(animais, entrada)

        else:
            # se os animais informados forem da mesma espécie
            adotados(animais, entrada)

else:
    # algum animal não está na lista
    for animal in entrada:
        if animal not in animais:
            print(
                f'Sérgio, o animal {animal} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.')
