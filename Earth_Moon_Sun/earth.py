class EarthObject():
    def __init__(self):
        surface_terre = 15
        fill(53, 210, 249)
        self.earthHeight = height/surface_terre
        self.earthWidth =  width/(surface_terre*1.777)
        return

    def earthDraw(self):
        
        ellipse(width/2, height/2, self.earthWidth , self.earthHeight) 
        return
