# -*- coding: utf-8 -*-
# universidad del Valle de Guatemala


def detection(x):

    calificacion = 0
    malas=0

    clasificacion_prueba = 0.43

    x = x.strip()

    cantidad_palabras = str(len ( x.split(" ")) )

    print "el tamaño del texto es", cantidad_palabras

    print "esto es"
    print x.split(" ")

    for i in range (len (x.split(" "))):
        print "entre"

        #aqui tienes que hacer lo de la revision


    ##-----------------calificacion = malas / cantidad_palabras-----------------------

    calificacion = clasificacion_prueba * 10

    return calificacion


texto = raw_input("Ingrese el texto a revisar: ")
detection(texto)
