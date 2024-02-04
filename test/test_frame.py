import pytest
from src.scoreCard import ScoreCard

def test_getPins():
    assert ScoreCard('12345123451234512345').getPins() == '12345123451234512345'

def test_getScoreAvarage():
    assert ScoreCard('12345123451234512345').getTotalScore() == 60
    
def test_getScoreWithNull():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getTotalScore() == 90