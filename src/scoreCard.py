class ScoreCard:

    PENULTIMATE_FRAME_POSITION = 9
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
        
        position = 0
        while position < len(self.getPins()):
            if self.getPins()[position] != "x" and len(frames) != self.PENULTIMATE_FRAME_POSITION:
                frames.append(self.getPins()[position:position+2])
                position += 2
            elif self.getPins()[position] == "x" and len(frames) != self.PENULTIMATE_FRAME_POSITION:
                frames.append(self.getPins()[position])
                position += 1
            elif len(frames) == self.PENULTIMATE_FRAME_POSITION:
                frames.append(self.getPins()[position:])
                break
            
        return frames

    def getFrameByPosition(self,position):
        if self.getPins()[position] == "x":
            return "x"
        else:
            return self.getPins()[position:position+2]
        
