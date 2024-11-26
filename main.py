# Reto Nro. 1 Proyecto de investigacion cientifica
# Grupo Nro.6
from datetime import datetime # la libreria datetime permite trabajar con el formato DD/MM/AAAA
import statistics # esta libreria permite realizar calculos estadisticos
import re

class Experimento:
    def __init__(self, nombreExp, descripcionExp, fechaRealizacion, categoriaExp, resultadosObtenidos): # funcion de inicialización (metodo constructor) 
        self.nombreExp = nombreExp   #self me permite diferenciar el parametro de la variable, el parametro me permite recibir un literal de información, en el parametro se recibe un argumento
        self.descripcionExp = descripcionExp # asignacionde un argumento descripcionExp a la variable descripcionExp
        self.fechaRealizacion = fechaRealizacion # asignacion de un argumento fecha de realización del experimento a la variable fechaRealización
        self.categoriaExp = categoriaExp # asignacion de un argumento categoria experimento a la variable categoriaExp
        self.resultadosObtenidos = resultadosObtenidos # asignacion de un argumento resultadosObtenidos a la variable resultadosObtenidos

#atributos de un experimento nombre, fecha (DD/MM/AAAA), tipo, resultados
"""listaExperimentos = [
    ["Experimento 01", "recoleccion de muestra de neumocitos", "16/11/2024", "Quimica", [5,3,4,6,8,10]], 
    ["Experimento 02", "recoleccion de muestra de nueumococos", "21/11/2024", "Biología", [4,3,11,1,6,5]],                       
    ["Experimento 01", "recoleccion de muestra de linfocitos", "27/11/2024", "Fisica", [14,3,4,6,8,7]],
]"""
def validarEntradaTexto(texto):
    patron ="[a-zA-Z0-9_]+$"
    if re.match(patron, texto):
        return True
    else:
        print("La entrada no es valida, solo se permiten letras, numeros sin espacios")
        return False
    
def agregarExperimento(listaExperimentos): #permite agregar un experimento con sus atributos
    nombreExp_str = input("Ingrese el nombre del Experimento sin espacios use _ o numeros: ").lower()
    #validarEntradaTexto(nombreExp)

    controlname = True
    while controlname == True:
        if nombreExp_str == "":
            print()
            print("El nombre del experimento no puede estar vacio")
            nombreExp_str = input("Ingrese nuevamente el nombre del Experimento : ").lower()
            print()
            #nombreExp = nombreExp_str
        else:
            nombreExp = nombreExp_str
            controlname = False

    descripcionExp_str = input("Ingrese una descripcion del experimento : ").lower()
    controldes = True
    while controldes == True:
        if descripcionExp_str == "":
            print()
            print("la descripcion del experimento no puede estar vacia")
            descripcionExp_str = input("Ingrese una descripcion del experimento : ").lower()
            print()
            descripcionExp = descripcionExp_str
        else:
            descripcionExp = descripcionExp_str
            controldes = False

    fechaRealizacion_str = input("Ingrese la fecha de realización del experimento (DD/MM/YYYY) : ")
    controlfer = True
    while controlfer == True:
        try:  
            fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y") #tambien se puede implementar %H:%M:%S
            controlfer = False
        except ValueError:
            print()
            print("fecha no valida.")  #si encuentra que la fecha no fue ingresada en formato DD/MM/AAAA le envia un mensaje
            fechaRealizacion_str = input("Ingrese la fecha de realización del experimento (DD/MM/YYYY) : ")
            #return                     #y lo retorna al mismo punto

    #categoriaExp_str = (input("Seleccione la categoria del Experimento(A=Química, B=Biología, C=Fisica) : ")).lower()
    controlcat = True
    while controlcat == True:
        categoriaExp_str = (input("Seleccione la categoria del Experimento(A=Química, B=Biología, C=Fisica) : ")).lower()
        if categoriaExp_str == "a":
            categoriaExp = "Química"
            controlcat = False
        elif categoriaExp_str == "b": 
            categoriaExp = "Biología"
            controlcat = False
        elif  categoriaExp_str == "c":
            categoriaExp = "Fisica"
            controlcat = False
        else:
            print()
            categoriaExp_str = (input("Opcion invalida, seleccione la categoria del Experimento(A=Química, B=Biología, C=Fisica) : "))   
            print()

    controlres = True
    while controlres == True:
        resultadosObtenidos_str = input("Ingrese los resultados obtenidos, separados por comas : ")
        try:
            tamano = len(list(map(float,resultadosObtenidos_str.split(","))))
            if tamano >= 3:
                try:  
                    resultadosObtenidos = list(map(float,resultadosObtenidos_str.split(","))) #map separa en forma individual los valores ingresados
                    controlres = False
                except ValueError:
                    print() 
                    resultadosObtenidos_str = input("Resultados no validos, ingrese los resultados separados por comas : ")
                    print()
                    #return  
            else:
                print("Ingrese una cantidad de datos como minima a 3")
        except:
            print()
            print("Resultados no validos, deben estar separados por comas")
                          

    #crear un objeto y lo agrega a la lista de tareas
    experimento = Experimento (nombreExp, descripcionExp, fechaRealizacion, categoriaExp, resultadosObtenidos)
    listaExperimentos.append(experimento)
    print("Experimento agregado con exito....")
    
    def eliminarExperimento(listaExperimentos): # funcion que permite eliminar experimenteos
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    nombreExpDel = input("Ingrese el nombre del experimento a eliminar : ").lower()
    for exp in listaExperimentos:
        if exp.nombreExp == nombreExpDel:
            listaExperimentos.remove(exp)
            print(f"\nEl experimento {exp} fue elimindo con exito")
            return
    #pass

def visualizarExperimentos(listaExperimentos): #permite visualizar todos los experimentos
    if not listaExperimentos:
        print("No hay experimentos registrados. ")
        print()
        return
    for i, experiment in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"\nNombre del experimento      : {experiment.nombreExp}")
        print(f"\nDescripcion del experimento : {experiment.descripcionExp}")
        print(f"\nFecha de realización        : {experiment.fechaRealizacion.strftime("%d/%m/%Y")}")
        print(f"\nCategoria del Experimento   : {experiment.categoriaExp}")
        print(f"\nResultados del experimento  : {experiment.resultadosObtenidos}")
        print()
    

