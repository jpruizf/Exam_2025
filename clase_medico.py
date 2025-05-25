class Medico:
    __dni:int
    __nombre:str
    __especialidad:str
    __matricula:str
    __valor_visita = 14500
    __zona:str

    def __init__(self,dni,nombre,especialidad,matricula,zona):
        self.__dni = dni
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__matricula = matricula
        self.__zona = zona

    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_especialidad(self):
        return self.__especialidad
    def get_matricula(self):
        return self.__matricula
    def get_valor_visita(self):
        return self.__valor_visita
    def get_zona_cubierta(self):
        return self.__zona
    def __mul__(self,otro_valor):
        return otro_valor.get_valor_visita() * self.__valor_visita
    