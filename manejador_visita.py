from clase_visita import Visita
import csv

class Gestor_Visitas:
    __listado_visita:list
    __contador:int

    def __init__(self):
        self.__contador = 0
        self.__listado_visita = []
    
    def cargar_visita(self,Una_visita):
        if Una_visita is not None:
            self.__contador += 1
            self.__listado_visita.append(Una_visita)
    def get_contador(self):
        return self.__contador
    def abrir_visitas(self):
        bandera = False
        with open('visitas.csv',encoding='UTF-8') as archivo_visitas:
            lector= csv.reader(archivo_visitas,delimiter=';')
            for file in lector:
                if not bandera:
                    bandera = True
                else:
                    Una_visita = Visita(file[0],int(file[1]),file[2],int(file[3]),file[4])
                    self.cargar_visita(Una_visita)
        archivo_visitas.close()
    '''inciso a'''
    def listar_datos_visitas(self,elemento,M_medico):
        for file in self.__listado_visita:
            dni_medico = int(M_medico.buscar_medico(elemento))
            if dni_medico is not None and dni_medico == int(elemento):
                print(f"DNI->{file.get_fecha():<5}|Zona->{file.get_zona():<5}|Diagnostico->{file.get_diagnostico():<5}|Total de visitas realizadas->{file.get_contador():<5}")
    
    '''inciso c'''
    def mostrar_listado_visitas(self,elemento,M_medico):
        nombre_medico = M_medico.buscar_nombre(elemento)
        for file in self.__listado_visita:
            if nombre_medico is not None and file.get_zona() == elemento:
                print(f"Fecha->{file.get_fecha():<5}|DNI del paciente->{file.get_paciente():<5}|Nombre medico->{nombre_medico:<5}|Diagnosticos->{file.get_diagnostico():<5}")