# -*- coding: utf-8 -*-

import FreeCAD as App
import FreeCADGui as Gui
from FreeCAD import Base
import Part, PartGui, Path
from PySide2 import QtWidgets
import cfg
import enum

class PathFuncs():
    '''
    Common functions for Path workbench tasks - create job, etc.
    '''