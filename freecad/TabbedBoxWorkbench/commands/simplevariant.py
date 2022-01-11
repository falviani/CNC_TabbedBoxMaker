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
        super.__init__()