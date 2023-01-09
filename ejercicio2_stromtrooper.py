class StormTrooper():
    def __init__(self, nombre, rango):
        self.nombre=nombre
        self.rango=rango

class Calificacion(StormTrooper):
    def __init__(self, nombre, rango, codigo_legion, id_cohorente, id_siglo, id_escuadra, numero):
        StormTrooper.__init__(self, nombre, rango)
        self.codigo_legion=input(codigo_legion)
        self.id_cohorente=input(id_cohorente)
        self.id_siglo=input(id_siglo)
        self.id_escuadra=input(id_escuadra)
        self.numero=input(numero)

    def __str__(self):
        return 'El StoormTrooper se llama {}, tiene rango {} y su calificacion es {}-{}{}{}{}'.format(self.nombre, self.rango, self.codigo_legion,self.id_cohorente,self.id_siglo,self.id_escuadra,self.numero)

StormTrooper1 = StormTrooper(Calificacion('Mario', 'Jefe', 'LM', 8, 3, 7, 5))
print(StormTrooper1)