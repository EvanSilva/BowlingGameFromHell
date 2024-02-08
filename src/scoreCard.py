class ScoreCard:

    
    def __init__(self,pins):
        self.pins = pins
        self.lenPins = len(self.getPins())
        self.frames = self.getFrames()
        
        
    
    def getPins(self):
        return self.pins

    #* tuve que cambiar el getPins por asignZero que daba error en un caso test

    def getTotalScore(self):
        total = 0
        for pin in self.asignZero():
            total += int(pin)
        return total
       # return sum(int(pin) for pin in self.getPins())
    
    #? igual se debería cambiar el nombre por pinsWithZero o algo así

    def asignZero(self):
        return self.getPins().replace("-","0")
    
    #* meto el asignZero en get frames para poder trabajar mejor a la hora de sumar

    #* cambié la lógica de la función getFrames LEER ABAJO DE TODO

    def getFrames(self):
        frames = []
        pins = self.asignZero()
        
        position = 0
        while position < len(pins):
        #while position < len(pins) and len(frames) < 9:
            currentPin = pins[position]

            if currentPin != "x":
                frames.append(pins[position:position+2])
                position += 2

            else:
                frames.append(currentPin)
                position += 1

        #if len(frames) == 9:
            #frames.append(pins[position:])
                
        return frames

    #def getFrameByPosition(self,position):
        #if self.getPins()[position] == "x":
            #return "x"
        #else:
            #return self.getPins()[position:position+2]

    #* al tener la función que te extraiga todos los frames la lógica de esta función se estropea por lo que quedaría de la siguiente forma, mucho más simplificada

    def getFrameByPosition(self,position):
        return self.getFrames()[position]
    
    #* en esta función calculo un único frame mediante la posición del frame, se usa la función de getFramesByPosition y se junta el valor uno del frame y el valor dos
    #* puse el nombre de sumFrame porque si era calculateFrame podía llegar a dar confusión a pensar que también calculaba Strikes, Semiplenos, ...

    def sumFrame(self,position):
        return int(self.getFrameByPosition(position)[0]) + int(self.getFrameByPosition(position)[1])

    #* funcion con este nombre para diferenciarlo de la futura funcion de "calculateFinalStrike". Esta funcion calcula un strike mediante la posicion de este mismo para poder acceder al siguiente frame de una forma más sencilla
    #? hay un problema con esta funcion cuando está en el penúltimo frame ya que uso la funcion sumFrame, sugiero cambiar la estructura del último frame y pasar de algo como "x12" a "x", "12", es decir, cambiarlo y dejar al final un único frame (otro ejemplo "1/3" a "1/", "3" y otro ejemplo "xxx" a "x", "x", "x") LEER ABAJO DE TODO
    #? este cambio arreglaría las funciones calculateMidleStrike y calculateMidleSplit cuando se encuentren en el penúltimo frame LEER ABAJO DE TODO

    def calculateMidleStrike(self,position):
        firstNextFrame = self.getFrameByPosition(position+1)
        secondNextFrame = self.getFrameByPosition(position+2)

        #TODO caso1 en el que el siguiente frame no es un pleno
        if firstNextFrame != "x":
            return self.sumFrame(position+1) + 10
        #TODO caso2 en el que los dos siguientes frames son plenos
        elif firstNextFrame == "x" and secondNextFrame == "x":
            return 30
        #TODO caso3 en el que los siguientes frames son un pleno y una tirada normal
        else:
            return int(secondNextFrame[0]) + 20

    #* funcion con prácticamente la misma lógica que calculateMidleStrike pero reducido a sumarle solo el siguiente tiro

    def calculateMidleSplit(self,position):
        nextFrame = self.getFrameByPosition(position+1)

        #TODO caso1 en el que el siguiente frame no sea un pleno
        if nextFrame != "x":
            return int(nextFrame[0]) + 10
        #TODO caso 2 en el que siguiente frame sea un pleno
        else:
            return 20
        
    #* funcion que calcula el último frame cambiando los plenos y semiplenos por dieces y luego sumando todo
    #? no entiendo porque el código de esta función está toda en azul a ver si le podeis echar un vistazo y arreglarla

    def calculateLastFrame(self):
        lastFrame = self.getFrames()[9:]

        for i in range(len(lastFrame)):
            if '/' in lastFrame[i] or lastFrame[i] == "x":
                lastFrame[i] = 10
            elif len(lastFrame[i]) > 1:
                lastFrame[i] = self.sumFrame(9+i)
        return sum(int(x) for x in lastFrame)
    
    def calculatePuntuation(self):
        total = 0

        for position, frame in enumerate(self.getFrames()[:9]):
            if frame != "x" and "/" not in frame:
                total += self.sumFrame(position)
            elif frame == "x":
                total += self.calculateMidleStrike(position)
            elif "/" in frame:
                total += self.calculateMidleSplit(position)

        return total + self.calculateLastFrame()



#? hay algo que no comprendo de la lógica de la puntuación, en el caso de que en el frame 9 tengas un pleno se sigue sumando los 2 siguientes no? (si es así se debe hacer lo de la línea 69). Y otra pregunta sobre el último frame, en el caso de que sean 3 plenos son 30 puntos o 90, son 30 no?
        
#* LEER AQUÍ, al final como vi que iba bien de tiempo y no tenía nada que hacer decidí ya cambiar la función getFrames para que el último frame fuese igual que el resto para pasar los casos test de calculateMidle... . Nosotros sabemos que a partir del noveno frame en adelante está todo en el mismo frame, esto lo podemos implementar en la funcionTotalScore tipo: "del frame 0 al 8 calcula de esta forma y del frame 9 en adelante de esta otra", espero haberme explicado, si teneis alguna duda mandarme un mensaje que igual ando con el móvil en la depilación
    
#* sorprendentemente el programa funciona hasta con un caso test de los dificiles ('x9-1/54--xx9-9/xx-'), como sugerencia final propongo eliminar la funcion de getTotalScore porque después de la de calculatePuntuation no sirve para nada
    
#TODO bueno chavales aquí está el código hecho por Amán ahora os toca refinarlo y hacerlo más bonito y legible mucha suerte chicos y lo siento por no estar presente para ayudaros. Un saludo, Amán