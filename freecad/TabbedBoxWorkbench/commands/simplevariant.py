# -*- coding: utf-8 -*-

import FreeCAD as App
from FreeCAD import Base
import FreeCADGui as Gui
import Part, PartGui
import cfg      # globally available
import support      #utility classes
import basevariant

class SimpleVariant(basevariant.BaseVariant):

    def __init__(self):
        ''' specific stuff for this variant '''
        super(SimpleVariant, self).__init__()

    def makePlates(self):
        makeBottomPlate()
        makeLeftPlate()
        makeTopPlate()
        makeRightPlate()
        makeBackPlate()
        makeTopPlate()

    def doToolPaths(self):
        # Path methods
        pass
