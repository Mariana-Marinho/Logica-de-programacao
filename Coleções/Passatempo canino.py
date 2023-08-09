def vaquinha(energia, gasto):
    """ retorna energia - gasto informado """
    return energia - int(gasto)


def chupeta(energia, gasto):
    """ retorna energia - 5 se for maior que o proprio gasto """
    gasto = int(gasto)
    energia = max(energia - 5, gasto)
    return energia


def ze_gotinha(energia, gasto):
    """ retorna divisao inteira da energia pelo gasto, e se este for 0 retorna a energia inalterada """
    # se o gasto for 0, a energia voltará intacta
    gasto = max(1, int(gasto))
    return energia // gasto


def bolinha(energia, gasto):
    """ retorna energia - gasto//4 """
    return energia - (int(gasto) // 4)


def osso(energia, gasto):
    """ retorna energia + 2*gasto """
    return energia + (int(gasto) * 2)


def comida(energia, palavra):
    """ retorna o valor da energia conforme a comida for par ou impar """
    # dicionario para mapear o que fazer dada a quantidade de caracteres da palavra
    resultado = {
        '0': +len(palavra),
        '1': -len(palavra)
    }
    mod = str(len(palavra) % 2)
    energia += resultado[mod]
    return energia


# dicionario como ponteiro para as funcoes
funcoes = {
    'Vaquinha': vaquinha,
    'Chupeta': chupeta,
    'Zé Gotinha': ze_gotinha,
    'Bolinha': bolinha,
    'Osso': osso,
    'Comida': comida
}

#  um dicionario sem o nome 'Comida', para poder usar a função .get() como uma condicional
frases = {
    'Vaquinha': 'Brinquedo da vaquinha! Vou chacoalhar',
    'Chupeta': 'Minha pipeta! Vou morder',
    'Zé Gotinha': 'Meu preferido! Faz barulho e mordo',
    'Bolinha': 'ZOOOOOOOOOOOOOOOOOM',
    'Osso': 'Pausa para roer',
}

inicial = int(input())
# energia que ela tem atualmente
atual = inicial
# energia que ela gastou no total
total_gasto = 0

while atual > 0 and total_gasto < 100:

    nome, valor = input().split(': ')

    # energia da rodada anterior
    velha = atual

    # energia que ela tem agora
    atual = funcoes[nome](atual, valor)
    # não pode exceder a energia inicial nem ser menor que 0
    atual = max(min(atual, inicial), 0)

    # energia gasta ao total, desconsiderando a energia que Charlote ganhou
    total_gasto += max((velha - atual), 0)

    print(frases.get(nome, f'Uhh, {valor} deve ser comestível'))

# tem que estar entre 0 e 100
final = min(max(total_gasto, 0), 100)

# tem que estar entre 1 e 10
letras = max(min(final // 10, 10), 1) * "a"

print(f'Mamãe chegou! Gastei {final} pontos da minha energia e estou c{letras}nsada, mas vou correr para seus braços!')
