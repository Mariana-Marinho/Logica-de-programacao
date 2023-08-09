clima = protetor = ''
dinheiro = 0

while True:
    frase = input()

    if frase == 'choveu':
        clima = 'chuvoso'

    if frase == 'parou de chover':
        clima = 'ensolarado'

    if frase == 'passar protetor':
        protetor = 'sim'

    if frase == 'separar dinheiro':
        dinheiro += float(input())

    if frase == 'ir para a praia':
        if clima == 'chuvoso':
            print('Hoje não vai dar pra ir, chuvinha barrou')
            break

        else:
            print('Hoje tem sol e mar!')

            if protetor == 'sim':
                if dinheiro >= 10:
                    print('Aí sim! Hoje rendeu!')

                else:
                    print('Só faltou uma aguinha de coco...')
                break

            else:
                if dinheiro >= 10:
                    print('O novo camarão do CIn foi criado')

                else:
                    print('Você não chegou muito bem, chame um médico!')
            break