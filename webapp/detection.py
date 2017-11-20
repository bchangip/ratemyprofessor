# -*- coding: utf-8 -*-
# universidad del Valle de Guatemala
from __future__ import division


def detection(x):
    malisimas = ['estupida', 'estupido', 'estúpido', 'idiota', 'pendejo', 'tarado', 'imbecil', 'puta', 'mierda',
                 'cerote', 'cerota', 'puto']
    malas = ['poco', 'impuntual', 'impaciente', 'desatento', 'injusto', 'perdida', 'poco', 'inflexible', 'inutil',
             'desconsiderado', 'inútil', 'incompetente', 'tonto', 'tonta', 'flojo', 'ineficiente', 'inepto', 'incapaz',
             'pesado', 'abusivo', 'racista', 'machista', 'incomodo', 'mal', 'malo', 'mala']
    buenas = ['mucho', 'paciente', 'justo', 'util', 'útil', 'bueno', 'atento', 'puntual', 'considerado', 'buena',
              'bien', 'excelente', 'interesante', 'esfuerzo', 'esfuerza', 'gusta', 'gusto', 'cómodo', 'comodo',
              'recomendado', 'recomendada', ]
    calificacion = 0
    cont_malas = 0
    cont_buenas = 0

    clasificacion_prueba = 0.0

    x = x.split(" ")

    cantidad_palabras = len(x)

    for i in range(len(x)):
        # censuramos el comentario
        for j in range(len(malisimas)):
            if x[i]==malisimas[j]:
                #x[i] = '####'
                cont_malas = cont_malas + 1
        for j in range(len(malas)):
            if x[i]==malas[j]:
                cont_malas = cont_malas + 1
        for j in range(len(buenas)):
            if x[i]==buenas[j]:
                cont_buenas = cont_buenas + 1
    # si clasificacion_prueba es negativo el comentario es negativo y se denotará que tan negativo


    if cont_malas > cont_buenas:
        clasificaion_prueba = float(cont_malas / cantidad_palabras) * (-1)
        return float(cont_malas / cantidad_palabras) * (-1) * 10
    # si clasificacion_prueba es positiva el comentario es positiva y se denotará que tan positiva
    if cont_malas < cont_buenas:
        clasificaion_prueba = float(cont_buenas / cantidad_palabras)
        #x = "".join(str(x) for x in texto)
    a =""
    for i in range(len(x)):
        a = a + x[i] + " "
        
    
        x = censura(a)
        return float(cont_buenas / cantidad_palabras) * 10
    return 0

        ##-----------------calificacion = malas o buenas / cantidad_palabras-----------------------


def censura(x):
    malisimas = ['estupida', 'estupido', 'estúpido', 'idiota', 'pendejo', 'tarado', 'imbecil', 'puta', 'mierda',
                 'cerote', 'cerota', 'puto']
    x = x.split(" ")
    nuevo = ""
    cantidad_palabras = len(x)

    for i in range(len(x)):
        # censuramos el comentario
        for j in range(len(malisimas)):
            if x[i]==malisimas[j]:
                x[i] = '####'
            # print x[i]
    for i in range (len (x)):
        nuevo = nuevo + x[i]+ " "

    return nuevo

def processComment(comment):
    print("Running detection")
    commentCategory = detection(comment)
    cleanedComment = censura(comment)
    print("Category:"+str(commentCategory))
    return commentCategory, cleanedComment
