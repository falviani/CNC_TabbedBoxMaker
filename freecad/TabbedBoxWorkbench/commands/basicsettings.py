# -*- coding: utf-8 -*-

"""
Collects basic values required for all boxes regardless of design
Passed to box-picking command, which in turn will save it to be
available to the selected box design
"""

class BasicSettings():

    """ fields - all dimensions are mm only """
    def __init__(self):
        # user-entered data
        self.boxWidth = 0.0     #X - using conventional axis view
        self.boxHeight = 0.0    #Z
        self.boxDepth = 0.0     #Y
        self.isInside = True
        self.stockWidth = 0.0
        self.stockHeight = 0.0
        self.stockThickness = 0.0
        self.stockMargin = 0.0
        self.endMillDia = 0.0   #diameter
        self.cutAllowance = 0.0 #extra added to stock thickness for profile depth
        self.slotFit = 0.0      # extra space to adjust fit of tag/slot - 0-press, 1=very loose
        # computed data for construction code
        self.inX = 0.0      # inside dimensions
        self.inZ = 0.0
        self.inY = 0.0
        self.outX = 0.0     # outside dimensions
        self.outZ = 0.0
        self.outY = 0.0

    """ accessors & validators for each field """
    def getboxWidth(self):
        return self.boxWidth

    def setboxWidth(self, w):
        self.boxWidth = w

    def getboxHeight(self):
        return self.boxHeight

    def setboxHeight(self, h):
        self.boxHeight = h

    def getboxDepth(self):
        return self.boxDepth

    def setboxDepth(self, d):
        self.boxDepth = d

    def getIsInside(self):
        return self.getIsInside

    def setIsInside(self, inside):
        self.isInside = inside

    def getStockWidth(self):
        return self.getStockWidth

    def setStockWidth(self, w):
        self.stockWidth = w

    def getStockHeight(self):
        return self.getStockHeight

    def setStockHeight(self, h):
        self.stockHeight = h

    def getStockThickness(self):
        return self.stockThickness

    def setStockThickness(self, s):
        self.stockThickness = s

    def setStockMargin(self, m):
        self.stockMargin = m

    def getStockMargin(self):
        return self.stockMargin

    def getEndmill(self):
        return self.endMillDia

    def setEndmill(self, e):
        self.endMillDia = e

    def getCutAllowance(self):
        return self.getCutAllowance

    def setCutAllowance(self, a):
        self.cutAllowance = a

    def setSlotFit(self, f):
        self.slotFit = f

    def getSlotFit(self):
        return self.slotFit

    """
    accessors to retrieve constuction dimensions
    """
    def getInX(self):
        return self.inX

    def getInY(self):
        return self.inY

    def getInZ(self):
        return self.inZ

    def getoutX(self):
        return self.outX

    def getOutY(self):
        return self.outY

    def getOutZ(self):
        return self.outZ

    """
    Additional utilities
    """

    def setConstructionDimensions(self):
        """
        ensure both inside and outside dimensions are calculated
        to be used during the construction process
        """
        if self.isInside:
            self.inX = self.boxWidth
            self.inY = self.boxDepth
            self.inZ = self.boxHeight
            self.outX = self.inX + self.stockThickness
            self.outY = self.inY + self.stockThickness
            self.outZ = self.inZ + self.stockThickness
        else:
            self.inX = self.boxWidth - self.stockThickness
            self.inY = self.boxDepth - self.stockThickness
            self.inZ = self.boxHeight - self.stockThickness
            self.outX = self.boxWidth
            self.outY = self.boxDepth
            self.outZ = self.boxHeight

    def minInsideDim(self):
        if self.inX == 0:
            setConstructionDimensions()
        m = 0.0
        if self.inX <= self.inY and self.inX <= self.inZ:
            m = self.inX
        else:
            if self.inY <= self.inZ:
                m = self.inY
            else:
                m = self.inZ
        return m

    def minOutsideDim(self):
        if self.outX == 0:
            setConstructionDimensions()
        m = 0.0
        if self.outX <= self.outY and self.outX <= self.outZ:
            m = self.outX
        else:
            if self.outY <= self.outZ:
                m = self.outY
            else:
                m = self.outZ
        return m

