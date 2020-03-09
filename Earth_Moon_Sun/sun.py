class SunObject():
    def __init__(self):
        self.mouse_X = mouseX
        self.mouse_Y = mouseY
        return
        
    def drawSun(self):
        sunRatio = 5 # la relation taille fenetre et taille soleil
        windowXYRatio = float(width)/float(height) # relation largeur fenetre hauteur fenetre
        sunHeight = height/(sunRatio)
        sunWidth = width/(sunRatio*windowXYRatio)
        self.windowBound(sunWidth, sunHeight)
        ellipse(self.mouse_X, self.mouse_Y, sunWidth, sunHeight) # emplacement soleil
        fill(255, 255, 0)
        return
    
    def windowBound(self, sunWidth, sunHeight):
        if (self.mouse_X <= sunWidth/2):
            self.mouse_X = sunWidth/2
        elif (self.mouse_X >= width-sunWidth/2):
            self.mouse_X = width-sunWidth/2
        if (self.mouse_Y <= sunHeight/2):
            self.mouse_Y = sunHeight/2
        elif (self.mouse_Y >= height-sunHeight/2):
            self.mouse_Y = height-sunHeight/2
        return        
