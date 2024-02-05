import pytest
from src.scoreCard import ScoreCard

def test_getPins():
    assert ScoreCard('12345123451234512345').getPins() == '12345123451234512345'

def test_getScoreAvarage():
    assert ScoreCard('12345123451234512345').getTotalScore() == 60
    
'''   
def test_getScoreWithNull():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getTotalScore() == 90  ''' 
    
def test_getFrames():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', 'x']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-xxx').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', 'xxx']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x1/').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', 'x1/']
    assert ScoreCard('x9-1/56--xx9-9/xx-').getFrames() == ['x', '9-', '1/', '56', '--', 'x', 'x', '9-', '9/', 'xx-']
    
def test_getFrameByPosition():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getFrameByPosition(2) == "9-"
    assert ScoreCard('9-x9-').getFrameByPosition(2) == "x" 