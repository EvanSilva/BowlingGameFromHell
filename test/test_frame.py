import pytest
from src.scoreCard import ScoreCard

def test_getPins():
    assert ScoreCard('12345123451234512345').getPins() == '12345123451234512345'

@pytest.mark.totalScoreHittingPins
def test_totalScoreHittingPins():
	assert ScoreCard("12345123451234512345").getTotalScore() == 60

@pytest.mark.totalScoreHittingPinsFail
def test_totalScoreHittingPinsFail():
	assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").getTotalScore() == 90
	assert ScoreCard("9-3561368153258-7181").getTotalScore() == 82

@pytest.mark.getFrames
def test_getFrames():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-XXX').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', 'XXX']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-X1/').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', 'X1/']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-X11').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', 'X11']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/1').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '1/1']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/X').getFrames() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '1/X']
    assert ScoreCard('X9-1/56--XX9-9/XX-').getFrames() == ['X', '9-', '1/', '56', '--', 'X', 'X', '9-', '9/', 'XX-']

@pytest.mark.changeDashToZero
def test_changeDashToZero():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').changeDashToZero() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', '90']
    assert ScoreCard('X9-1/56--XX9-9/XX-').changeDashToZero() == ['X', '90', '1/', '56', '00', 'X', 'X', '90', '9/', 'XX0']

@pytest.mark.frameScoreSpare
def test_frameScoreSpare():
	assert ScoreCard("5/5/5/5/5/5/5/5/5/5/5").calculateFrames() == [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
	assert ScoreCard("9-3/613/815/-/8-7/8/8").calculateFrames() == [9, 16, 7, 18, 9, 10, 18, 8, 18, 18]

@pytest.mark.frameScoreStrike
def test_frameScoreStrike():
	assert ScoreCard("X9-9-9-9-9-9-9-9-9-").calculateFrames() == [19, 9, 9, 9, 9, 9, 9, 9, 9, 9]
	assert ScoreCard("XXX9-9-9-9-9-9-9-").calculateFrames() == [30, 29, 19, 9, 9, 9, 9, 9, 9, 9]


@pytest.mark.totalScoreSpare
def test_totalScoreSpare():
	assert ScoreCard("5/5/5/5/5/5/5/5/5/5/5").getTotalScore() == 150
	assert ScoreCard("9-3/613/815/-/8-7/8/8").getTotalScore() == 131
	
@pytest.mark.totalScoreStrike
def test_totalScoreStrike():
	assert ScoreCard('X9-9-9-9-9-9-9-9-9-').getTotalScore() == 100
	assert ScoreCard("9-9-9-9-9-9-9-9-9-X9-").getTotalScore() == 100
	assert ScoreCard("X9-X9-9-9-9-9-9-9-").getTotalScore() == 110
	assert ScoreCard("XX9-9-9-9-9-9-9-9-").getTotalScore() == 120
	assert ScoreCard("XXX9-9-9-9-9-9-9-").getTotalScore() == 141
	assert ScoreCard("9-9-9-9-9-9-9-9-9-XXX").getTotalScore() == 111
	assert ScoreCard("XXXXXXXXXXXX").getTotalScore() == 300
	assert ScoreCard("8/549-XX5/53639/9/X").getTotalScore() == 149
	assert ScoreCard("X5/X5/XX5/--5/X5/").getTotalScore() == 175


@pytest.mark.scoreByFrames
def test_scoreByFrames():
	assert ScoreCard('12345123451234512345').getScoreByFrames() == [3, 10, 16, 21, 30, 33, 40, 46, 51, 60]
	assert ScoreCard('X9-9-9-9-9-9-9-9-9-').getScoreByFrames() == [19, 28, 37, 46, 55, 64, 73, 82, 91, 100]
	assert ScoreCard("XXXXXXXXXXXX").getScoreByFrames() == [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
	





