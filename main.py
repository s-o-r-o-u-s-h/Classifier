__author__ = 'soroush'
import sys
from ui import ui
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
window = ui.PrimaryWindow(None)
window.show()
sys.exit(app.exec_())