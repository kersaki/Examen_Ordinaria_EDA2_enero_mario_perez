def usar_la_fuerza(mochila, objetos):
    contador = 0
    for i in mochila:
        if i == objetos:
            return mochila[:objetos]
            

    