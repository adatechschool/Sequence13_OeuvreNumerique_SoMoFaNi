from shadows import Shadows, SunObject

def setup():
    fullScreen()
    
    
def draw():
    shad = Shadows()
    sun = SunObject()
    background(255)
    sun.drawSun()
    shad.rays()
    shad.calcAngleToMoon()
