# -*- coding: utf-8 -*-

"""
Collect global values useful to all variants
"""
import os, sys

import FreeCAD as App
import FreeCADGui as Gui
from freecad.TabbedBoxWorkbench import RESPATH
import cfg
from PySide2 import QtCore, QtGui, QtWidgets
import basicValues
import basicsettings
import pprint


class Cmd_Globals():

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Resource definition allows customization of the command icon,
    # hotkey, text, tooltip and whether or not the command is active
    # when a task panel is open
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    resources = {
        'Pixmap': os.path.join(RESPATH,"gear1.svg"),
        'Accel': "shift+1",
        'MenuText': "Get Globals",
        'ToolTip': "Get Common Values",
        'CmdType': "ForEdit"
    }

    basics = None       #holds basic dimensions collected from user
    isBasicsNew = True
    dl = None           #holds dialog from loaded module

    def setBasics(self, basics):
        self.basics = basics

    def getBasics(self):
        return self.basics

    def on_useBtn_clicked(self):
        """
        needed to pass self, since signals normally don't pass arguments
        """
        self.innerUse()
        print("saving values")

    def innerUse(self):
        """
        retrieve all inputs here
        store into 'basics' object
        """
        if self.basics is None:
            self.basics = basicsettings.BasicSettings()
        self.basics.setboxWidth(self.dl.ui.boxW_val.value())
        self.basics.setboxDepth(self.dl.ui.boxY_val.value())
        self.basics.setboxHeight(self.dl.ui.boxZ_val.value())
        self.basics.setIsInside(self.dl.ui.inside_chk.isChecked())
        self.basics.setStockWidth(self.dl.ui.stockX_val.value())
        self.basics.setStockHeight(self.dl.ui.stockY_val.value())
        self.basics.setStockThickness(self.dl.ui.stockZ_val.value())
        self.basics.setStockMargin(self.dl.ui.stockMargin_val.value())
        self.basics.setSlotFit(self.dl.ui.slotFit_val.value())
        # pprint.pprint(self.basics)

        self.basics.setConstructionDimensions()
        cfg.boxData = self.basics   #make globally available
        # App.ActiveDocument.recompute()    #no active document - we should do a "new" first
        self.dl.hide()

    def on_cancelBtn_clicked(self):
        self.innerCancel()

    def innerCancel(self):
        """
        do nothing except close dialog
        """
        print ("bailing out")
        self.dl.hide()

    def on_test1Button_clicked(self):
        self.innerTest1Button()

    def innerTest1Button(self):
        '''
        Set stock values for 3mm birch plywood
        '''
        if self.basics is None:
            self.basics = basicsettings.BasicSettings()
        self.basics.setStockWidth(254.0)
        self.dl.ui.stockX_val.setValue(254.0)
        self.basics.setStockHeight(254.0)
        self.dl.ui.stockY_val.setValue(254.0)
        self.basics.setStockThickness(3.3)
        self.dl.ui.stockZ_val.setValue(3.3)
        self.basics.setMargin(5)
        self.dl.ui.slotFit_val.setValue(5)
        self.basics.setEndmill(1.0)
        self.dl.ui.emDia_val.setValue(1.0)          # 1mm endmill for thin stock
        self.dl.repaint(self.dl.visibleRegion())     #refresh display

    def loadUIFromBasics(self):
        pass

    """
    'Standard' methods
    """

    def GetResources(self):
        """
        Return the command resources dictionary
        """
        return self.resources

    def Activated(self):
        """
        Activation callback
        """

        self.dl = QtWidgets.QWidget()
        self.dl.ui = basicValues.Ui_Dialog()
        self.dl.ui.setupUi(self.dl)
        # need to connect buttons AFTER loading UI, so editing of generated *.py file not required
        self.dl.ui.useBtn.clicked.connect(self.on_useBtn_clicked)
        self.dl.ui.cancelBtn.clicked.connect(self.on_cancelBtn_clicked)
        self.dl.ui.test1Button.clicked.connect(self.on_test1Button_clicked)
#        if self.isBasicsNew:     #if existing values when opening this, reload them
#            self.loadUIFromBasics(self)

        self.dl.show()
        print('\n\tRunning Pick Globals...')

        #Gui.SendMsgToActiveView('ViewFit')

    def IsActive(self):
        """
        Returns always active
        """

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # IsActive allows the command icon / menu item to be enabled
        # or disabled depending on various conditions.
        #
        # Here, the command is only enabled if a document is open.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # return App.ActiveDocument is not None
        return True

Gui.addCommand('Cmd_Globals', Cmd_Globals())
