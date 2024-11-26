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

def generarInforme(listaExperimentos): # funcion que permite generar un informe resumen de los experimentos y sus estadisticas
    if not listaExperimentos:
        print("No existen experimentos registrados")
        return
    #crear un archivo txt para generar el informe
    with open("Informe_experimentos_registrado.txt", "w") as archivoExp : # w (write) para dar permisos de escritura sobre el archivo
        # se procede con la escritura de los atributos del experimento(s)
        for experimento in listaExperimentos:
            archivoExp.write(f"\nNombre experimento          : {experimento.nombreExp}")
            archivoExp.write(f"\nDescripcion del experimento : {experimento.descripcionExp}")
            archivoExp.write(f"\nFecha de realizacion        : {experimento.fechaRealizacion}")
            archivoExp.write(f"\nCategoria del experimento   : {experimento.categoriaExp}")
            archivoExp.write(f"\nresultados Obtenidos        : {experimento.resultadosObtenidos}")
            archivoExp.write(f"\n")

def mostrarMenu(): # funcion que permite mostrar el menu principal del programa que permite elegir una opcion
    listaExperimentos = []
    """listaExperimentos = [
    ["Experimento 01", "recoleccion de muestra de neumocitos", "16/11/2024", "Quimica", [5,3,4,6,8,10]], 
    ["Experimento 02", "recoleccion de muestra de nueumococos", "21/11/2024", "Biología", [4,3,11,1,6,5]],                       
    ["Experimento 01", "recoleccion de muestra de linfocitos", "27/11/2024", "Fisica", [14,3,4,6,8,7]],
    ]"""
    controlop = True
    while controlop == True:
        print()
        print()
        print("==============Menu Principal================")
        print("= 1. Agregar experimentos                  =")               
        print("= 2. Visualizar Experimentos               =")
        print("= 3. Eliminar Experimentos                 =")
        print("= ===========Análisis de Datos==============")
        print("= 4. Calcular estadisticas                 =")
        print("= 5. Comparación de experimentos           =")
        print("= 6. Generar informe                       =")
        print("= 7. Salir                                 =")
        print("============================================")
        print()
        print()
    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregarExperimento(listaExperimentos)
        elif opcion == "2":
            visualizarExperimentos(listaExperimentos)
        elif opcion == "3":
            eliminarExperimento(listaExperimentos)
        elif opcion == "4":
            calcular_estadisticas(listaExperimentos)
        elif opcion == "5":
            compararExperimento(listaExperimentos)
        elif opcion == "6":    
            generarInforme(listaExperimentos)   
        elif opcion == "7":
            print("Saliendo del programa")
            print()
            break     
        else:
            print("opción invalida")
            opcion = input("Seleccione una opción valida (1-7): ")
            print()  
    #pass

mostrarMenu()
