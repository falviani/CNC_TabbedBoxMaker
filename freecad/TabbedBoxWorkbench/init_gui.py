# -*- coding: utf-8 -*-

# mandatory file if you have a gui (which we do)

import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.TabbedBoxWorkbench import RESPATH

#use this to track workbench versioning
TEMPLATEWB_VERSION = '(0.0.1)'


class tabbedBoxWorkbench(Gui.Workbench):
    MenuText = "Tabbed Box Workbench"
    ToolTip = "CNC-oriented tabbed box creator"
    Icon = os.path.join(RESPATH, "gear1.svg")

    #Constants for UI locations for toolboxes (bit flags)
    MENU = 1
    TOOLBAR = 2
    # CONTEXT = 4

    #Workbench GUI-specific attributes
    MenuText = "Tabbed Box Workbench " + TEMPLATEWB_VERSION
    toolbox = []

    def __init__(self):
        self.command_ui = {
            'TabbedBoxes' : {
                'gui': self.MENU,
                'cmd': ['Cmd_Globals']
            },
            'TabbedBoxesTab': {
                'gui': self.TOOLBAR,
                'cmd': ['Cmd_Globals']
            },
            'PickBox':{
                'gui': self.MENU,
                'cmd': ['Cmd_pickBox']
            },
            'PicBoxTab': {
                'gui': self.TOOLBAR,
                'cmd': ['Cmd_pickBox']
            },
            'SimpleBox': {
                'gui': self.MENU,
                'cmd': ['Cmd_simple']
            },
            'SimpleBoxTab': {
                'gui': self.TOOLBAR,
                'cmd': ['Cmd_simple']
            }
        }

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        Import commands here
        """
        from .commands import cmd_globals,cmd_pickBox,cmd_simple        #
        for _k, _v in self.command_ui.items():
            if _v['gui'] & self.TOOLBAR:
                self.appendToolbar(_k, _v['cmd'])

            if _v['gui'] & self.MENU:
                self.appendMenu(_k, _v['cmd'])

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

        print(Gui)
        #Add diagnostic code or other start-up related activities here
        App.Console.PrintMessage("\n\tSwitching to tabbed box workbench")

    def Activated(self):
        return
 
    def Deactivated(self):
        return
 
    def ContextMenu(self, recipient):
        # self.appendContextMenu("My commands", self.list)
        pass
 
    def GetClassName(self):
        return "Gui::PythonWorkbench"
 
Gui.addWorkbench(tabbedBoxWorkbench())
