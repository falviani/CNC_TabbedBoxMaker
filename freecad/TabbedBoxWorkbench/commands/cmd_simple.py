# -*- coding: utf-8 -*-

import FreeCAD as App
import FreeCADGui as Gui
import Part, PartGui
import os, sys
from freecad.TabbedBoxWorkbench import RESPATH
import cfg
from PySide2 import QtCore, QtGui, QtWidgets
import simpleBox    
import basicsettings
#import basevariant
import simplevariant    # actual constuction of this box
import support          # custom data classes, etc.

class Cmd_Simple():

   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Resource definition allows customization of the command icon,
    # hotkey, text, tooltip and whether or not the command is active
    # when a task panel is open
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    resources = {
        'Pixmap': os.path.join(RESPATH,"PlainCube_box.svg"),
        'Accel': "shift+3",
        'MenuText': "Simple Box",
        'ToolTip': "Construct basic box",
        'CmdType': "ForEdit"
    }

    basics = None       #holds basic dimensions collected from user
    isBasicsNew = True
    dl = None           #holds dialog from loaded module

    def setBasics(self, basics):
        self.basics = basics

    def getBasics(self):
        return self.basics

    def on_buildBtn_clicked(self):
        """
        needed to pass self, since signals normally don't pass arguments
        """
        self.innerBuild()

    def innerBuild(self):
        '''
        Actually construct the box
        '''
        self.boxer = simplevariant.SimpleVariant()
        support.initBasicObs()  #create globals: doc to hold our construction
        support.createBody("simpleBox")
        cfg.test1()     #examine actual values
        print("building simple box")
        # make first frame. may need more depending of stock size and box size
        self.boxer.makeStockFrame((0,0,0), self.basics.getStockWidth(), self.basics.getStockHeight())
        self.boxer.makePlates()
        self.boxer.makeToolPaths()
        self.dl.hide()

    """
    'Standard' methods
    """

    '''
    def __init__(self):
        super().__init__()
    '''

    def GetResources(self):
        """
        Return the command resources dictionary
        """
        return self.resources

    def Activated(self):
        """
        Activation callback
        """
        if support.checkDims() == 0:    # if no basic dimensions just bail
            return

        self.setBasics(cfg.boxData)
        self.dl = QtWidgets.QWidget()
        self.dl.ui = simpleBox.Ui_Dialog()
        self.dl.ui.setupUi(self.dl)
        # need to connect buttons AFTER loading UI, so editing of generated *.py file not required
        self.dl.ui.buildBtn.clicked.connect(self.on_buildBtn_clicked)
        # connect to code that reacts to change in user size spinbox
        # compute minimum and maximum tab size and update labels
        self.dl.ui.minSizeValLbl.setText(str(self.basics.getStockThickness()))
        self.dl.ui.userSizeLbl.setText(str(self.basics.getStockThickness()))
        tMax = self.basics.minOutsideDim()
        self.dl.ui.maxSizeVal.setText(str(tMax / 2))
        #self.dl.ui.cancelBtn.clicked.connect(self.on_cancelBtn_clicked)
#        if self.isBasicsNew:     #if existing values when opening this, reload them
#            self.loadUIFromBasics(self)

        self.dl.show()

        print('\n\tRunning Simple Box Constructor...')

    def IsActive(self):
        """
        Returns always active
        """
        return True # boxData is not None  # App.ActiveDocument is not None

Gui.addCommand('Cmd_simple', Cmd_Simple())
