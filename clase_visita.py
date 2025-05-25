class Visita:
    __fecha:str
    __dni_paciente:int
    __zona:str
    __dni_medico:int
    __diagnostico:str

    def __init__(self,fe,dni_pa,zon,dni_med,diag):
        self.__fecha = fe
        self.__dni_paciente = dni_pa
        self.__zona = zon
        self.__dni_medico = dni_med
        self.__diagnostico = diag

    def get_fecha(self):
        return self.__fecha
    def get_paciente(self):
        return self.__dni_paciente
    def get_zona(self):
        return self.__zona
    def get_medico(self):
        return self.__dni_medico
    def get_diagnostico(self):
        return self.__diagnostico
    def __eq__(self,otra_zona):
        return self.__zona == otra_zona.get_zona()