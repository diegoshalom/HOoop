class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        #pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        senal_out = list(senal)
        deltatime = (tiempo_final - tiempo_inicial)  / len(senal)
        for i,j in enumerate(senal):
            tiempo_senal = tiempo_inicial + (deltatime * i)
            if (tiempo_senal >  self.tiempo_inicial  and tiempo_senal <  self.tiempo_final):
                senal_out[i] = senal[i] + self.amplitud
            else:
                senal_out[i] = senal[i]
        return senal_out
                
        
        
        
        
        
