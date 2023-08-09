def primo(num):
    # checa se o número é primo e não retorna valor
    if num <= 1:
        return False
    else:
        for c in range(2, num):
            if num % c == 0:
                return False
        return True


def tem_primo(intervalo):
    # adiciona os primos no intervalo numa lista e retorna a lista
    lista = []
    for c in range(2, intervalo):
        if primo(c):
            lista.append(c)
    lista.sort()
    return lista


def printar_numeros(lista):
    # printa os números do intervalo, não retorna nada
    for n in lista:
        if lista.index(n) == 0:
            print(n, end='')
        else:
            print(f', {n}', end='')
    print()


entrada = int(input())

if primo(entrada):
    print(f'O número {entrada} é primo.')

else:
    print(f'O número {entrada} não é primo')
    primos_intervalo = tem_primo(entrada)

    if len(primos_intervalo) > 0:
        print(f'Entretanto, temos primos no intervalo de 1 à {entrada}. Estes são:')
        printar_numeros(primos_intervalo)

    else:
        print(f'Além disso, não temos primos no intervalo de 1 à {entrada}')

print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')
