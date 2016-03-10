"""
Define el simulador del Radar
"""


class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector


    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        import matplotlib.pyplot  as plt

            
            
        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
           
        #print una_senal   
        
        sent, = plt.plot(una_senal,label='Sent')          
          
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, tiempo_final)
        
        received, = plt.plot(una_senal_reflejada,label='Received')
        plt.ylabel('Signal')
        plt.grid(True)
        plt.xlabel('Time (au)')
        plt.legend(handles = [sent,received])
        plt.show()

        
        
        return self.detector.detectar(una_senal_reflejada)
 
    #TODO agregar el metodo plotear_senal

