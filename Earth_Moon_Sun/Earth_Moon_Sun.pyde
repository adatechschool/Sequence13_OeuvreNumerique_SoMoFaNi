from sun import SunObject
from earth import EarthObject
from collision import CollisionObject 

def setup():
    fullScreen()
    backgroundSpace = loadImage("Images/space_background.jpg")
    image(backgroundSpace, 0, 0, width, height)
    
    
    
def draw():
    backgroundSpace = loadImage("Images/space_background.jpg")
    image(backgroundSpace, 0, 0, width, height)
    sun = SunObject()
    sun.drawSun()
    
    earth= EarthObject()
    earth.earthDraw()
    if ((dist(mouseX,mouseY,width/2,height/2) - (sun.sunWidth/2 + earth.earthWidth/2)) < 0):
        fill(255,0,0)
        earth.earthDraw()
        print("collision")
    
#    collsion= COllsionObject()
#    collision.collsionDraw
    
    #if (dist (width/2, height/2, self.mouse_X, self.mouse_Y) < ( width/(surface_terre*1.777) + height/surface_terre) + sunWidth + sunHeight )
    #{
     #fill (255)
     
   # }
    

    
   # print(dist(mouseX,mouseY,width/2,height/2))sunWarthW
