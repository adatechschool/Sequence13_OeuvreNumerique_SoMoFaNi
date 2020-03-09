from sun import SunObject

def setup():
    fullScreen()
    backgroundSpace = loadImage("Images/space_background.jpg")
    image(backgroundSpace, 0, 0, width, height)
    
    
    
def draw():
    backgroundSpace = loadImage("Images/space_background.jpg")
    image(backgroundSpace, 0, 0, width, height)
    sun = SunObject()
    sun.drawSun()
