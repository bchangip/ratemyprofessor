# -*- coding: utf-8 -*-
# universidad del Valle de Guatemala


def detection(x):
    
    cont_malas=0
    cont_buenas=0

    clasificacion_prueba = 0.43

    x = x.strip()

    cantidad_palabras = len ( x.split(" "))

    #print "el tamaño del texto es "+ cantidad_palabras

    print "esto es"
    print x.split(" ")

    for i in range (len (x.split(" "))):
        #censuramos el comentario
        if i in malisimas:
            x.replace(i,"#@#@!")
        if i in malas:
            cont_malas = cont_malas + 1
        if i in buenas:
            cont_buenas = cont_buenas + 1
    #si clasificacion_prueba es negativo el comentario es negativo y se denotará que tan negativo
    if cont_malas>cont_buenas:
        clasificaion_prueba = (cont_malas / cantidad_palabras)*-1
    #si clasificacion_prueba es positiva el comentario es positiva y se denotará que tan positiva
    if cont_malas<cont_buenas:
        clasificaion_prueba = cont_buenas / cantidad_palabras
            
    ##-----------------calificacion = malas o buenas / cantidad_palabras-----------------------

    calificacion = clasificacion_prueba * 10
    print calificacion
    return calificacion

texto = raw_input("Ingrese el texto a revisar: ")
detection(texto)
