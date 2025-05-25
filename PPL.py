from manejador_medico import Gestor_Medico
from manejador_visita import Gestor_Visitas

def menu():
    manejar_medicos = Gestor_Medico(5)
    manejar_visitas = Gestor_Visitas()
    manejar_medicos.abrir_archivo()
    manejar_visitas.abrir_visitas()
    if manejar_medicos.abrir_archivo() is not None and manejar_visitas.abrir_visitas() is not None:
        print("datos cargados con exito :)")
    else:
        print("error :/")
    print("a)->Ver listado de datos de las visitas para un DNI")
    print("b)->Ver datos de cada medico y total a facturar")
    print("c)->Ver listado de visitas realizadas para una zona")
    opcion=input("Seleccione una de las opciones->")
    if opcion == 'a':
        dni = int(input("DNI del medico->"))
        manejar_visitas.listar_datos_visitas(dni,manejar_medicos)
    elif opcion == 'b':
        manejar_medicos.mostrar_medico(manejar_visitas)
    elif opcion == 'c':
        zona = input("Zona->")
        manejar_visitas.mostrar_listado_visitas(zona,manejar_medicos)

if __name__ == '__main__':
    print("1->Iniciar   |   0->Terminar")
    inicio = input("Elija una oopcion->")
    while inicio != '0':
        menu()
        print("1->Iniciar   |   0->Terminar")
        inicio = input("Bienvenido/a de nuevo\n Elija una opcion->")