import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import core.swmm.project
from ui.SWMM.frmControlsDesigner import Ui_frmControls


class frmControls(QtGui.QMainWindow, Ui_frmControls):


    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.cmdOK, QtCore.SIGNAL("clicked()"), self.cmdOK_Clicked)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.cmdCancel_Clicked)
        self.set_from(parent.project)
        self._parent = parent

    def set_from(self, project):
        # section = core.epanet.project.Control()
        section = project.find_section("CONTROLS")
        self.txtControls.setPlainText(str(section.get_text()))

    def cmdOK_Clicked(self):
        section = self._parent.project.find_section("CONTROLS")
        section.set_text(str(self.txtControls.toPlainText()))
        self.close()

    def cmdCancel_Clicked(self):
        self.close()
