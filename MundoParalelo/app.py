"""
    @author: Adrian Verdugo
    @since 28/11/2018
    @verson 0.1
    TODO Mundo pararelo
"""

from datetime import time, datetime, timedelta
from dateutil.relativedelta import relativedelta 

def calculo_mundo_paralelo(tiempo):
    #tiempo_paralelo = datetime.strptime('03:55', '%H:%M')
    #diff = relativedelta(tiempo, tiempo_paralelo)
    t = tiempo - timedelta(hours=4, minutes=10)
    return '{}:{}'.format(t.hour, t.minute)


def manifiesto_navegacion():
    NOMBRE_DOC_MANIFIESTO = './manifiesto.txt'
    NOMBRE_DOC_PARELELO = './paralelo.txt'
    with open(NOMBRE_DOC_MANIFIESTO, 'r+') as doc_man:
        mensaje = doc_man.read()
        linea  = mensaje.split('\n')
        print('------------------------------------------')
        print('[INFO]:> Lectura Finalizada: {}'.format(NOMBRE_DOC_MANIFIESTO))
    doc_man.closed
    with open(NOMBRE_DOC_PARELELO, 'w') as doc_paralelo:
        sum = 0
        for l in linea:
            if sum == 0:
                doc_paralelo.write(linea[sum])
            else:
                print('horas disponibles :> {}'.format(linea[sum]))
                tiempo = datetime.strptime(linea[sum], '%H:%M')
                calculo_mundo_paralelo(tiempo)
                doc_paralelo.write('\n' + calculo_mundo_paralelo(tiempo))
            sum += 1
        print('[SUCCESS]:> Escritura Finalizada con Exito: {}'.format(NOMBRE_DOC_PARELELO))
        print('-------------------------------------------')
    doc_paralelo.closed


manifiesto_navegacion()

