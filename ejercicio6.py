def mochila(precio, peso, peso_maximo):
    elementos = (zip(precio,peso))
    precio_total= 0
    peso_total= 0
    for precio, peso in elementos:
        if peso_total + peso  > peso_maximo:
            continue
        precio_total += precio
        peso_total += peso
    return precio_total

precio = [103, 60, 70, 5, 15]
peso = [12, 23, 11, 15, 7]
peso_maximo = 100

print(mochila(precio, peso, peso_maximo))
