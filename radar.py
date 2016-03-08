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
           
        print una_senal   
        
        def plotear_senal(senal):
            plt.plot(senal)

        plotear_senal(una_senal)          
          
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, tiempo_final)
        
        #plotear_senal(una_senal_reflejada)
        
        return self.detector.detectar(una_senal_reflejada)
 
    #TODO agregar el metodo plotear_senal

