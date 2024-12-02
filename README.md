# Reto_1_DevSenior_G6
Importacion de librerias datetime para trabajar con fechas en especial el formato DD/MM/AAAA
Importacion de libreria statistics para trabajar con promedios, minimos y maximos
Importacion de libreria re para trabajar con validacion de entradas y crear patrones
creacion de una clase Experimento con sus respectivos argumentos
se crea una lista de experimentos y cada uno de4 estos con sus respectivos atributos para facilitar la verificacion
Se creo la funcion agregarExperimento(listaExperimentos) en la cual se realizaron validaciones para evitar vacios en su nombre, descripcion, fecha de realizacion, categoria y resultados, por ultimo se agrego un experimento a la clase Experimento
Se creo la funcion eliminarExperimento(listaExperimentos) en la cual se le pide al usuario que ingrese el nombre del experimento se realiza la busqueda y al encontrarlo se elimina
Se creo la funcion visualizarExperimentos(listaExperimentos) en la cual se recorre la lista de experimentos y se imprime usando la funcion enumerate para presentar los experimentos
Se creo la funcion compararExperimento(listaExperimentos) en el cual se visualizan todos los experimentos, se crean las listas generales de promedio, maximo y minimo y se solicita al usuario que ingrese los ids de los experimentos que desea comparar, a los cuales se les realiza el calculo de promedio, maximo y minimo, luego se llama otra funcio de comparacion.
se creo la funcion comparacionExperimento(listaIndicesComparacion,listaPromedios,listaMaximos,listaMinimos, resultadosComparacion, listaPromediosGral) en esta funcion se toman la informacion ya extraida y se inicia a validar en caso que el usuario ingreso un solo valor se le solicita que ingrese minimo dos valores, luego se valida si el valor es igual a dos se procede con la comparacion directa mediante un if, else, si el valor es mayor a dos se procede la validacion con un ciclo for y se evalua la posibilidad que los promedios sean iguales
Se creo la funcion calcular_estadisticas(listaExperimentos) en la cual se valida si la lista tiene valores y de tenerlos mediante un ciclo for se procede a calcularlo y exponerlo al usuario
Se creo la funcion generarInforme(listaExperimentos) en la cual se valida la lista de experimentos se realiza el calculo general del promedio, maximo y minimo por ultimo se crea un archivo y se le da privilegios de escrituara en la cual se ingresan los atributos de los experimentos y los calculos generales de promedio, maximo y minimo
Por ultimo se crea una funcion de mostrarMenu() en la cual se le presenta al usuario un menu con sus respectivas opciones y mediante un ciclo while se hace una validacion para el ingreso a las opciones

