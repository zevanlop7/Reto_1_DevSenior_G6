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