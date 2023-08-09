nome_invencao = input()
custo_total = etapas_realizadas = total_falhas = 0

while True:
    nome_etapa = input()

    if nome_etapa != 'concluir' and nome_etapa != 'desistir':
        custo_etapa = int(input())

        if nome_etapa != 'dar um plus':
            tentativas_etapa = int(input())
            for i in range(tentativas_etapa):
                status_etapa = input()
                custo_total += custo_etapa

                if status_etapa == 'correto':
                    print(f'Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}')
                    etapas_realizadas += 1
                    break

                else:
                    print(f"Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}")
                    total_falhas += 1
            print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {total_falhas}')

        else:
            # se o nome da etapa for 'dar um plus'
            custo_total += custo_etapa
            print(f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}')

    else:
        # se o nome dar etapa for 'concluir' ou 'desistir'
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
        if nome_etapa == 'desistir':
            print(f'Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${custo_total}')

        else:
            print(f'Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${custo_total}')
        break