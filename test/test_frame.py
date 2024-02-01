import pytest
from src.scoreCard import ScoreCard


def test_getPins():
    assert ScoreCard('12345123451234512345').getPins() == '12345123451234512345'


def test_AverageScore():
    pass


'''
# Hitting pins total = 60
		pins = "12345123451234512345";
		int total = 60;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());
'''