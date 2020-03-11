class CollisionObject():
    def __init__(self):
        return
    
    def collisionDraw(self):
        if (dist((mouseX,mouseY,width/2,height/2)) < 2(earthWidth + sunWidth )) :
            fill (255, 0, 0)
        else :
           fill(53, 210, 249)
