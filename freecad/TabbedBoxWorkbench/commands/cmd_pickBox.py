# -*- coding: utf-8 -*-

"""
Collect global values useful to all variants
"""

import os, sys
import FreeCAD as App
import FreeCADGui as Gui
from freecad.TabbedBoxWorkbench import RESPATH
from PySide2 import QtCore, QtGui, QtWidgets
import gallery
import basicsettings
import cfg      # globally available
import support

class Cmd_PickBox():

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Resource definition allows customization of the command icon,
    # hotkey, text, tooltip and whether or not the command is active
    # when a task panel is open
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    resources = {
        'Pixmap': os.path.join(RESPATH,"chooser.svg"),
        'Accel': "shift+2",
        'MenuText': "Box Gallery",
        'ToolTip': "Show Available Box Types",
        'CmdType': "ForEdit"
    }

    basics = None       #holds basics collected from user
    dl = None           #holds dialog from loaded module

    def setBasics(self, basics):
        self.basics = basics

    def getBasics(self):
        return self.basics

    def on_doneBtn_clicked(self):
        self.innerDone()

    def innerDone(self):
        """
        do nothing except close dialog
        """
        print ("bailing out")
        self.dl.hide()

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
        print('\n\tRunning Pick Box...')
        if support.checkDims() == 0:    # if no basic dimensions just bail
            return

        self.dl = QtWidgets.QWidget()
        self.dl.ui = gallery.Ui_dlog()
        self.dl.ui.setupUi(self.dl)
        # need to connect buttons AFTER loading UI, so editing of generated *.py file not required
        # also need to manually insert path to images, since Designer doesn't create proper form
        plain = os.path.join(RESPATH, "PlainCube_box_pixmap.png")
        topless = os.path.join(RESPATH, "ToplessCube_box_pixmap.png")
        self.dl.ui.plainBoxImg.setPixmap(QtGui.QPixmap(plain))
        self.dl.ui.toplessBoxImg.setPixmap(QtGui.QPixmap(topless))
        self.dl.ui.doneBtn.clicked.connect(self.on_doneBtn_clicked)

        self.dl.show()
        print('\n\tRunning Pick Globals...')

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

        return True # boxData is not None  # App.ActiveDocument is not None

Gui.addCommand('Cmd_pickBox', Cmd_PickBox())
