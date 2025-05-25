from clase_medico import Medico
import csv
import numpy as np

class Gestor_Medico:
    __cantidad:int
    __dimension:int
    __incremento = 5
    __listado_medicos:np.ndarray

    def __init__(self,dimension):
        self.__dimension = dimension
        self.__cantidad = 0
        self.__listado_medicos = np.empty(self.__dimension,Medico)
    
    def cargar_medico(self,Un_medico):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listado_medicos.resize(self.__dimension)
        self.__listado_medicos[self.__cantidad] = Un_medico
        self.__cantidad += 1
    
    def abrir_archivo(self):
        bandera = False
        with open('medicos.csv',encoding='UTF-8') as archivo_medicos:
            lector = csv.reader(archivo_medicos,delimiter=';')
            for file in lector:
                if not bandera:
                    bandera = True
                else:
                    Un_medico = Medico(int(file[0]),file[1],file[2],file[3],file[4])
                    self.cargar_medico(Un_medico)
        archivo_medicos.close()
    '''inciso a'''
    def buscar_medico(self,elemento:int):
        bandera = False
        encontrado = None
        indice = 0
        while not bandera and indice < len(self.__listado_medicos):
            if elemento == self.__listado_medicos[indice].get_dni():
                bandera =  True
                encontrado =  int(self.__listado_medicos[indice].get_dni())
            else:
                indice += 1
        return encontrado
    '''inciso b'''
    def mostrar_medico(self,M_visitas):
        visitas_realizadas = int(M_visitas.get_contador())
        for file in self.__listado_medicos:
            if visitas_realizadas is not None:
                print(f"Nombre->{file.get_nombre():<5}|Especialidad->{file.get_especialidad():<5}|Zona->{file.get_zona_cubierta():<5}|Total de visitas->{visitas_realizadas:<5}|Importe total->{visitas_realizadas * file.get_valor_visita()}")
    '''inciso c'''
    def buscar_nombre(self,elemento):
        bandera = False
        encontrado = None
        indice = 0
        while not bandera and indice < len(self.__listado_medicos):
            if elemento == self.__listado_medicos[indice].get_zona_cubierta():
                bandera =  True
                encontrado =  self.__listado_medicos[indice].get_nombre().lower()
            else:
                indice += 1
        return encontrado