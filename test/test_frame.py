import pytest
from src.scoreCard import ScoreCard

def test_getPins():
    assert ScoreCard('12345123451234512345').getPins() == '12345123451234512345'

def test_getScoreAvarage():
    assert ScoreCard('12345123451234512345').getTotalScore() == 60
    
  
def test_getScoreWithNull():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getTotalScore() == 90
    
#* como implementé la función asignZero en la de getFrames tuve que cambiar todos los "-" por "0"
#* modifiqué los casos test porque modifiqué esta función para poder pasar los casos test de calculateMidle...
#* he modificado los casos test para que se completen todas las posibles combinaciones del último frame

def test_getFrames():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getFrames() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', '90']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-xxx').getFrames() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', 'x', 'x', 'x']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x1/').getFrames() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', 'x', '1/']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x11').getFrames() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', 'x', '11']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/1').getFrames() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', '1/', '1']
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/x').getFrames() == ['90', '90', '90', '90', '90', '90', '90', '90', '90', '1/', 'x']
    assert ScoreCard('x9-1/56--xx9-9/xx-').getFrames() == ['x', '90', '1/', '56', '00', 'x', 'x', '90', '9/', 'x', 'x', '0']

#* como implementé la función asignZero en la de getFrames tuve que cambiar todos los "-" por "0"

def test_getFrameByPosition():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').getFrameByPosition(2) == "90"
    #* test modificado que ponía un 2 en vez de un 1
    assert ScoreCard('9-x9-').getFrameByPosition(1) == "x" 

#* casos test para la función sumFrame
    
def test_sumFrame():
    assert ScoreCard("12-41234").sumFrame(0) == 3
    assert ScoreCard("12-41234").sumFrame(1) == 4

#* casos test para la funcion calculateMidleStrike 
    
def test_calculateMidleStrike():
    assert ScoreCard('xxx').calculateMidleStrike(0) == 30
    assert ScoreCard('x9-1/56--xx9-9/xx-').calculateMidleStrike(0) == 19
    assert ScoreCard('x9-1/56--xx9-9/xx-').calculateMidleStrike(5) == 29
    #? arreglar el código para este caso test (posible solución indicada en el otro archivo)
    #? no sé si este último caso test está bien hecho porque me lié a última hora con la lógica del programa
    assert ScoreCard('9-9-9-9-9-9-9-9-xxx').calculateMidleStrike(8) == 30

#* casos test para la funcion calculateMidleSplit
    
def test_calculateMidleSplit():
    assert ScoreCard('x9-1/x--xx9-9/xx-').calculateMidleSplit(2) == 20
    assert ScoreCard('x9-1/56--xx9-9/xx-').calculateMidleSplit(2) == 15
    #? pasa lo mismo que arriba con este caso test
    assert ScoreCard('x9-1/56--xx9-9/xx-').calculateMidleSplit(8) == 20

#* casos test para la funcion calculateLastFrame

def test_calculateLastFrame():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').calculateLastFrame() == 9
    assert ScoreCard('9-9-9-9-9-9-9-9-9-xxx').calculateLastFrame() == 30
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x1/').calculateLastFrame() == 20
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x11').calculateLastFrame() == 12
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/1').calculateLastFrame() == 11
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/x').calculateLastFrame() == 20
    assert ScoreCard('x9-1/56--xx9-9/xx-').calculateLastFrame() == 20

#* casos test para la funcion calculatePuntuation
    
def test_calculatePuntuation():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').calculatePuntuation() == 90
    assert ScoreCard('9-9-9-9-9-9-9-9-9-xxx').calculatePuntuation() == 111
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x1/').calculatePuntuation() == 101
    assert ScoreCard('9-9-9-9-9-9-9-9-9-x11').calculatePuntuation() == 93
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/1').calculatePuntuation() == 92
    assert ScoreCard('9-9-9-9-9-9-9-9-9-1/x').calculatePuntuation() == 101
    #* cambié el 56 por un 54 porque supuestamente no pueden haber más de 10 bolos, creo yo vamos
    assert ScoreCard('x9-1/54--xx9-9/xx-').calculatePuntuation() == 149