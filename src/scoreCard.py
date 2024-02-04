class ScoreCard:

    def __init__(self,pins):
        self.pins = pins
    
    def getPins(self):
        return self.pins

    def getTotalScore(self):
        total = 0
        for pin in self.asignFormat():
            total += int(pin)
        return total
       # return sum(int(pin) for pin in self.getPins())
    
    def asignZero(self):
        return self.getPins().replace("-","0")
    
    def asignFormat(self):
        return self.asignZero()