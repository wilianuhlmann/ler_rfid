cartoes_liberados = {
    '0005593112': 'Wilian Cesar Uhlmann',
    '9999999': 'Miguel Machado',
    '999988': 'Sandra',
}

print(cartoes_liberados)

print('Aproxime seu cartão RFID')

while True:
    ler_rfid = str(input('Aproxime seu cartão: '))

    if ler_rfid is not None:
        print('Cartão detectado!')

        id_rfid = ler_rfid
        print(id_rfid)
        if id_rfid in cartoes_liberados:
            print('Acesso Liberado!')
        else:
            print('Acesso Negado!')

        print('Aproxime seu cartão RFID')
