# -*- coding: utf-8 -*-

# Base class of box generators
import FreeCAD as App
from FreeCAD import Base
import FreeCADGui as Gui
import Part, PartGui
import cfg          # globally available
import support      #utility classes
import Sketcher

class BaseVariant(object):
    # these are set by initial plate calculations so usage is consistent between plates
    base_xDelta = 0.0   # horizontal distance between vertices on bottom/top plates
    base_yDelta = 0.0   # vertical distance..
    base_tabExtra = 0.0 # extra width of top/bottom tabs due to rounding
    vert_xDelta = 0.0   # horizontal distance between vertices on side plates
    vert_yDelta = 0.0   # vertical distance...
    vert_gapExtra = 0.0 # extra width of initial/end gaps to match horizontal tabs
    vert_tabExtra = 0.0 # extra width of tab at top of side plates due to rounding

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
        self.plateVertices = []     # generated vertices for entire
        self.plateLines = []        # created from vertices (wires?)
        self.plateShapes = []       # created from lines

    def makeStockFrame(self, loc, sizeX, sizeY):
        '''
        Create a rect for a stock piece at the given location and size
        Create shape in construction vector mode
        It is added by the caller to the stockFrames list when constructed
          [so it can be moved if needed before appending to list]
        '''
        Sketcher.toggleConstruction()       #turn on [should this be normal line?]
        initPlate()
        # construct rectangle here
        #self.plateVertices.append(Base.Vertex(loc.X, loc.Y, 0))     #BL
        self.plateVertices.append(Vector(loc.X, loc.Y, 0))  #BL
        self.plateVertices.append(Base.Vertex(loc.X, loc.Y+sizeY, 0)) #TL
        self.plateVertices.append(Base.Vertex(loc.X+sizeX, loc.Y+sizeY, 0))   #TR
        self.plateVertices.append(Base.Vertex(loc.X+sizeX, loc.Y, 0))   #BR
        #vertices->lines
        Sketcher.toggleConstruction()       #turn off
        self.stockFrames.append(self.plateVertices)     #should this be shapes?

    def adjustGap(self, align=support.CutAlign.IN, edgeDir=support.RectEdge.L, useSaved=False):
        '''
        adjusts nominal gap value for path compensation (inside, on, outside)
        also adjusts for slotFit (looseness of fit)
        adjusted value saved in class variable
        '''
        if useSaved:
            if edgeDir==support.RectEdge.L or edgeDir==support.RectEdge.R:
                pass
            else:
                pass

    def tabCalc(self, tabWidth=3, edgeDir=support.RectEdge.L):
        '''
        values are in mm
        returns tab width, end tab width (distributes extra width between 2 end tabs)
        gap width == tab width
        adjustGap() called after this to compensate for mill diameter, fit looseness correctly
        '''
        tabW = tabWidth
        endtabW = tabWidth
        ''' calcs here '''
        if edgeDir == support.RectEdge.L or edgeDir== support.RectEdge.R:
            edgelen = self.basics.getBoxHeight()
        else:
            edgelen = self.basics.getBoxWidth()
        tCount = edgelen // tabWidth
        extra = edgelen - (tCount * tabWidth)   # edge likely not even number of tabs, so extra will need to be distributed
        if extra > 0:
            tabadjust = extra / 2.0
        else:
            tabadjust = 0.0
        endtabW = tabWidth + tabadjust
        # need to save in class variable somehow ?
        return tabW, endtabW

    def buildTabEdge(self, edgeDir=support.RectEdge.L):
        pass

    def buildStraightEdge(self, edgeDir=support.RectEdge.L):
        pass

    '''
    All plates are constructed with the inner side UP
    MAY only implement these in derived classes
    '''

    def makeBottomPlate(self):
        initPlate()
        leftTab, leftBigTab = self.tabCalc(self.basics,getStockThickness(), support.RectEdge.L)
        self.adjustGap(support.CutAlign.IN, support.RectEdge.L, False)

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

    '''
    support routines needed for overall process
    '''

    def additionalStockFrames(self):
        '''
        determine if additional stock frames are needed, and create them if so
        '''
        plateShapes



