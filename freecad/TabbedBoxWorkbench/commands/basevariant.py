# -*- coding: utf-8 -*-

# Base class of box generators
import FreeCAD as App
from FreeCAD import Base
import FreeCADGui as Gui
import Part, PartGui
import cfg      # globally available
import support      #utility classes
import Sketcher

class BaseVariant():

    def __init__(self):
        self.basics = cfg.boxData   #holds basics collected from user
        self.stockFrames = []   #stock rectangles constraining plate layout
        self.plates = []        #walls of the box
        self.plateVertices = []
        self.plateLines = []
        self.plateShapes = []
        self.doc = None

    def newDoc(self):
        if self.doc is None:    #don't replace existing document!!
            self.doc = App.newDocument()
        else:
            self.doc = App.activeDocument()     #is this right?

    def initPlate(self):
        '''
        Ensure a clean start
        '''
        self.plateVertices = []
        self.plateLines = []
        self.plateShapes = []

    def makeStockFrame(self, loc, sizeX, sizeY):
        '''
        Create a rect for a stock piece at the given location and size
        Create shape in construction vector mode
        It is added by the caller to the stockFrames list when constructed
          [so it can be moved if needed before appending to list]
        '''
        Sketcher.toggleConstruction()       #turn on
        initPlate()
        # construct rectangle here
        #self.plateVertices.append(Base.Vertex(loc.X, loc.Y, 0))     #BL
        self.plateVertices.append(Vector(loc.X, loc.Y, 0))  #BL
        self.plateVertices.append(Base.Vertex(loc.X, loc.Y+sizeY, 0)) #TL
        self.plateVertices.append(Base.Vertex(loc.X+sizeX, loc.Y+sizeY, 0))   #TR
        self.plateVertices.append(Base.Vertex(loc.X+sizeX, loc.Y, 0))   #BR
        #vertices->lines
        Sketcher.toggleConstruction()       #turn off

    def tagCalc(self, tagCount=0, tagWidth=3):
        '''
        values are in mm
        returns tab width, end tab width
        '''
        tagW = tagWidth
        endTagW = tagWidth
        ''' calcs here '''
        return tagW, endTagW

    def buildTagEdge(self):
        pass

    def buildStraightEdge(self):
        pass

    '''
    All plates are constructed with the inner side UP
    MAY only implement these in derived classes
    '''

    def makeBottomPlate(self):
        initPlate()

    def makeLeftPlate(self):
        initPlate()

    def makeRightPlate(self):
        initPlate()

    def makeFrontPlate(self):
        initPlate()

    def makeBackPlate(self):
        initPlate()

    def makeTopPlate(self):
        initPlate()



