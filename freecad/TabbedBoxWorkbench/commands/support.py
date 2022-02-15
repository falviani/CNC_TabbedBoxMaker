# -*- coding: utf-8 -*-

import FreeCAD as App
import FreeCADGui as Gui
from FreeCAD import Base
import Part, PartGui
from PySide2 import QtWidgets
import enum
import cfg
from datetime import date

"""
Support classes and common functions
"""

''' clockwise from bottom left '''
class Corner(enum.IntEnum):
    BL = 0        #bottomleft
    TL = 1
    TR = 2
    BR = 3

class RectEdge(enum.IntEnum):
    L = 0
    T = 1
    R = 2
    B = 3

class CutAlign(enum.IntEnum):
    IN = 0
    ON = 1
    OUT = 2

class SegmentData():
    '''
    includes constraints for Sketcher data
    '''
    def __init__():
        self.Part.LineSegment
        self.constraints = []

class PlateData():
    '''
    All required data about 1 plate
    '''

    def __init__():
        self.label = 'lbl'
        self.cut = CutAlign.OUT
        self.shape = None

class PlateGroup():
    '''
    All plates that fit on a single stock piece, as laid out
    '''

    def __init__():
        self.groupLabel = '1'
        self.plates = {}        # use list instead?

"""
Common utility functions
"""
def checkDims():
    """
    check to ensure user has set sizes, bail if not
    """
    if cfg.boxData is None:
        errbox = QtWidgets.QMessageBox();
        errbox.setText("Basic dimensions were not set. Please do that to continue.")
        errbox.exec()
        return 0
    else:
        return 1

def initBasicObs():
    """
    Universally used. Call this after checkDims() has verified we have basic data to proceed
    """
    d = App.activeDocument()
    t = date.today()
    if d is None:
        #nD = App.newDocument("unnamed")
        #App.setActiveDocument(nD)
        #d = App.getActiveDocument()
        pass
    d.Label = "TabbedBox-{0}_{1}_{2}".format(t.day,t.month, t.year)
    cfg.setDoc(d)
    Gui.activeDocument = cfg.getDoc()

def createBody(boxType):
    '''
    All generated plates need to be on sketches, which need to be in a body
    '''
    if boxType is None:
        bodyName = "body"
    else:
        bodyName = boxType
    cfg.setBodyName(bodyName)
    cfg.getDoc().addObject("PartDesign::Body", bodyName)
    cfg.setBody(cfg.getDoc().getObject(bodyName))
    Gui.activeView().setActiveObject('abody', cfg.getBody())
    Gui.Selection.clearSelection()
    Gui.Selection.addSelection(cfg.getBody())
    App.ActiveDocument.recompute()
