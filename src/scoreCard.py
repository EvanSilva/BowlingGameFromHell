class ScoreCard:

    
    def __init__(self,pins):
        self.pins = pins
        self.lenPins = len(self.getPins())
        self.frames = self.getFrames()
        
        
    
    def getPins(self):
        return self.pins

    def getTotalScore(self):
        total = 0
        for pin in self.getPins():
            total += int(pin)
        return total
       # return sum(int(pin) for pin in self.getPins())
    
    def asignZero(self):
        return self.getPins().replace("-","0")
    
    def getFrames(self):
        frames = []
        pins = self.getPins()
        
        position = 0
        while position < len(pins) and len(frames) < 9:
            currentPin = pins[position]

            if currentPin != "x":
                frames.append(pins[position:position+2])
                position += 2

            else:
                frames.append(currentPin)
                position += 1

        if len(frames) == 9:
            frames.append(pins[position:])
                
        return frames

    def getFrameByPosition(self,position):
        if self.getPins()[position] == "x":
            return "x"
        else:
            return self.getPins()[position:position+2]
        
