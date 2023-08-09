fibonacci = list()

for i in range(100):
    if i == 0:
        fibonacci.append(1)
        valor = 0
        x = 1
        y = 0
    valor = x + y
    y = x
    x = valor
    fibonacci.append(valor)

n = int(input())

for i in range(n):
    entrada = input()

    espaco = entrada.find(' ')
    indice_fibonacci = entrada[:espaco]

    indice_digitos = entrada.replace(indice_fibonacci, '').replace(' ', '')

    hifen = indice_digitos.find('-')
    primeiro_digito = int(indice_digitos[:hifen])
    segundo_digito = int(indice_digitos[hifen + 1:])

    numero_fibonacci = str(fibonacci[int(indice_fibonacci) - 1])
    codigo_digito = str(numero_fibonacci[primeiro_digito]) + str(numero_fibonacci[segundo_digito])
    codigo_digito = int(codigo_digito)

    print(chr(codigo_digito), end='')
