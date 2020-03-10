#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class SunObject(object):
    def __init__(self):
        self.mouse_X = mouseX
        self.mouse_Y = mouseY
        sunRatio = 5 # la relation taille fenetre et taille soleil
        windowXYRatio = float(width)/float(height) # relation largeur fenetre hauteur fenetre
        self.sunHeight = height/(sunRatio)
        self.sunWidth = width/(sunRatio*windowXYRatio)
        return

    def drawSun(self):
        self.windowBound()
        fill(255, 255, 0)
        ellipse(self.mouse_X, self.mouse_Y, self.sunWidth, self.sunHeight) # emplacement soleil
        return

    def windowBound(self):
        if (self.mouse_X <= self.sunWidth/2):
            self.mouse_X = self.sunWidth/2
        elif (self.mouse_X >= width-self.sunWidth/2):
            self.mouse_X = width-self.sunWidth/2
        if (self.mouse_Y <= self.sunHeight/2):
            self.mouse_Y = self.sunHeight/2
        elif (self.mouse_Y >= height-self.sunHeight/2):
            self.mouse_Y = height-self.sunHeight/2
        return

    def passSunCoords(self):
        self.windowBound()
        # sun_up_line_Y = self.mouse_Y - self.sunWidth/2
        # sun_down_line_Y = self.mouse_Y + self.sunWidth/2
        return self.mouse_X, self.mouse_Y


class Shadows(SunObject):
    def __init__(self):
        super(Shadows, self).__init__()
        self.rayCoordTable = super(Shadows, self).passSunCoords() # Index 0 = X coord of Sun, Index 1 = Y coord of Sun
        self.upperRay = self.rayCoordTable[1]-self.sunWidth/2 # Y coord upper ray
        self.lowerRay = self.rayCoordTable[1]+self.sunWidth/2 # Y coord lower ray
        self.targetX = 500
        self.targetY = 500
        return

    def rays(self):
        line(self.rayCoordTable[0], self.upperRay, self.targetX, self.targetY)
        line(self.rayCoordTable[0], self.lowerRay, self.targetX, self.targetY)

    def calcAngleToMoon(self):

        angleX = abs(self.rayCoordTable[0] - self.targetX)
        angleY = abs(self.rayCoordTable[0] - self.targetY)
        # line(self.rayCoordTable[0], self.rayCoordTable[1], angleX, self.rayCoordTable[1])
        # line(self.rayCoordTable[0], self.rayCoordTable[1], self.rayCoordTable[0], angleY)
        #print(self.targetX, self.targetY, self.rayCoordTable[0], self.rayCoordTable[1])
        distanceToMoon = sqrt(angleX**2 + angleY**2)
        # print(distanceToMoon)
        try:
            angleX = abs(self.rayCoordTable[0] - self.targetX)
            angleY = abs(self.rayCoordTable[0] - self.targetY)
            sinAngleToMoon = sin(angleX/angleY)
            cosAngleToMoon = cos(angleY/angleX)
            print(sinAngleToMoon, cosAngleToMoon)
            pointXSunTest = distanceToMoon*sinAngleToMoon + self.targetX
            pointYSunTest = distanceToMoon*cosAngleToMoon + self.targetY
            # print(pointXSunTest, pointYSunTest)
            line(pointXSunTest, pointYSunTest, self.rayCoordTable[0], self.rayCoordTable[1])
            # line(self.targetX, self.targetY , pointXSunTest, pointYSunTest)
        except:
            pass
        return
