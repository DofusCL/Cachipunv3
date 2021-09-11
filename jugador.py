import cachipun
from computador import *


def jugar():
    player = ''
    while player.capitalize() not in opciones:
        player = (input('¿Piedra, Papel o Tijeras?\n'))
    else:
        cachipun.check(player, npc)
