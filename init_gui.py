# mandatory file if you have a gui (which we do)

from FreeCAD import Gui

class tabbedBoxWorkbench(Workbench):
    MenuText = "Tabbed Box Workbench"
    ToolTip = "CNC-oriented tabbed box creator"

    def Initialize(self):
        pass

    def Activated(self):
        return
 
    def Deactivated(self):
        return
 
    def ContextMenu(self, recipient):
        self.appendContextMenu("My commands", self.list)
 
    def GetClassName(self):
        return "Gui::PythonWorkbench"
 
Gui.addWorkbench(tabbedBoxWorkbench())
