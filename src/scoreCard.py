class ScoreCard:

    
    def __init__(self,pins):
        self.pins = pins
        self.lenPins = len(self.getPins())
        self.frames = self.getFrames()
        

    def getPins(self):
        return self.pins

    def getTotalScore(self):
        return self.getScoreByFrames()[-1]
    
    def getScoreByFrames(self):
        scoreByFrames = []
        currentScore = 0
        for score in self.calculateFrames():
            currentScore += score
            scoreByFrames.append(currentScore)

        return scoreByFrames

    def getFrames(self):
        frames = []
        pins = self.getPins()
        
        roll = 0
        while roll < len(pins) and len(frames) < 9:
            currentPin = pins[roll]
            if currentPin != "X":
                frames.append(pins[roll:roll+2])
                roll += 2
            else:
                frames.append(currentPin)
                roll += 1
        if len(frames) == 9:
            frames.append(pins[roll:])
                
        return frames
    

    def changeDashToZero(self):
        frames = self.getFrames()
        return [frame.replace("-",'0') for frame in frames]

    def calculateFrames(self):
        frames = self.changeDashToZero()
        scoreForFrame = []

        position = 0
        while position < 9:
            currentFrame = frames[position]
            if "X" not in currentFrame and "/" not in currentFrame:
                scoreForFrame.append(int(currentFrame[0]) + int(currentFrame[1]))
            elif "/" in currentFrame:
                scoreForFrame.append(self.calculateSpareFrame(position))
            elif "X" in currentFrame:
                scoreForFrame.append(self.calculateStrikeFrame(position))
            position += 1

        if position == 9:
                scoreForFrame.append(self.calculateLastFrame())
        return scoreForFrame


    def calculateSpareFrame(self,position):
        nextFrame = self.changeDashToZero()[position+1]
        if position == 8:
            nextFrame =  self.changeDashToZero()[position+1][0]

        if nextFrame != "X":
            return 10 + int(nextFrame[0])
        else:
            return 20
        
    def calculateStrikeFrame(self,position):
        frames = self.changeDashToZero()
        nextFrame = frames[position+1]

        if position < 8:
            secondNextFrame = frames[position+2]
        else:
            secondNextFrame = frames[position+1][1]

        if "X" not in nextFrame and "/" not in nextFrame:
            return 10 +  int(nextFrame[0]) + int(nextFrame[1])
        elif "/" in nextFrame:
            return 20
        elif "X" in nextFrame and "X" not in secondNextFrame:
            return 20 + int(secondNextFrame[0])
        elif "X" in nextFrame and "X" in secondNextFrame:
            return 30
            
        
    def calculateLastFrame(self):
        lastFrame = self.changeDashToZero()[9]

        if "XXX" in lastFrame:
            return 30
        elif "XX" in lastFrame:
            return 20 + int(lastFrame[2])
        elif "X" in lastFrame:
            if "/" in lastFrame:
                return 20
            else:
                return 10 + int(lastFrame[1]) + int(lastFrame[2])
        elif "/" in lastFrame:
            return 10 + int(lastFrame[2])
        else:
            return int(lastFrame[0]) + int(lastFrame[1])

        
