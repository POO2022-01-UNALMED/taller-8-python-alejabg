from persona import Persona
from deportista import Deportista

class Futbolista(persona, deportista):

    listaFutbolistas=[]

    def __init__(self, nom, edad, estatura,sexo,an,gol,tar,pier):
        Persona.__init__(self, nom, edad, estatura, sexo)
        Deportista.__init__(self,"Futbol",an)
        self._golesMarcados = gol
        self._tarjetasRojas = tar
        self._piernaHabil = pier
        Futbolista.listaFutbolistas += [self]
        
    def __str__(self):
        return "Mi nombre es "+str(self._nombre)+" soy profesional en el deporte "+str(self._deporte)+" Tengo "+str(self._edad )+" años de edad y llevo "+str(self._añosPracticando) +" años en el deporte"   

    @staticmethod
    def  getListaFutbolistas():
        return Futbolista.listaFutbolistas

    @staticmethod
    def setListaFutbolistas( listaFutbolistas):
        Futbolista.listaFutbolistas = listaFutbolistas

    def  getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, _golesMarcados):
        self._golesMarcados = _golesMarcados

    def  getTarjetasRojas(self):
        return self._tarjetasRojas

    def set_tarjetasRojas(self, _tarjetasRojas):
        self._tarjetasRojas = _tarjetasRojas

    def  getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, _piernaHabil):
        self._piernaHabil = _piernaHabil

futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
print(isinstance(futbolista, Deportista) and isinstance(futbolista, Persona))