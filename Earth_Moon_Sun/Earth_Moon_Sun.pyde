from earth import EarthObject

def setup():
    fullScreen()
    
    
def draw():
    background(0)
    terre = EarthObject()
    terre.earthDraw()
    
