class Remote:
    def isPressedLeft():
        pass
class Player:
    def moveLeft():
        pass
    
    def moveRight():
        pass
    def moveUp():
        pass

Remote1=Remote()
Player1=Player()

if(Remote1.isPressedLeft()):
    Player1.moveLeft()
else:
    Player1.moveRight()
