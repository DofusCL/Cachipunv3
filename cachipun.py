def check(player, npc):
    print(f'\nEl computador eligió {npc}...\n')
    if player == npc:
        print('Empatados....\n')
        print('Fin del juego')
    else:
        if (player == 'Piedra' and npc == 'Tijeras') or (player == 'Papel' and npc == 'Piedra') or (player == 'Tijeras' and npc == 'Papel'):
            print('Has Ganado! Felicitaciones :D \n')
            print('Fin del juego')
        else:
            print('Ding....ding....ding.... El computador Ganó')
            print('Fin del juego')
