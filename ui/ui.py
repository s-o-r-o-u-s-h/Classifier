__author__ = 'soroush'
from PyQt4 import QtGui, uic
from core import training

form_ui = uic.loadUiType("ui/mainWindow.ui")[0]


class PrimaryWindow(QtGui.QMainWindow, form_ui):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.data_path = None                   # dataset's path
        self.class_col = 'last'                 # class's column in dataset,by default it's the last column
        self.train_data = 50                    # amount of training data based on percent,by default is 50%
        self.tr = None
        self.rd_last.setChecked(True)


        self.sldr_data.valueChanged.connect(self.slider_value)
        self.btn_choose_dataset.clicked.connect(self.check_file)
        self.show_step(self.grp_step1)

        '''     set shortcuts for menu items    '''

        self.action_Exit.setShortcut('Alt+F4')
        self.action_Exit.triggered.connect(QtGui.qApp.quit)
        self.action_Help.setShortcut('F1')

    '''     State handling
        Whenever a step completed successfully,app should hide it
        and shows next step, The following function will take care of that.
        Note that we first hide all group boxes and then, We show the desired
        group box.
    '''

    def show_step(self, a):
        self.grp_step1.hide()
        self.grp_step2.hide()
        a.show()

    '''     functions for step1     '''

    def check_file(self):
        self.inp_dataset.setText(QtGui.QFileDialog.getOpenFileName())
        self.data_path = self.inp_dataset.text()
        if ".txt" in self.data_path[-4:]:
            self.lbl_step1_status.setText("Database loaded successfully!")
            self.lbl_step1_status.setStyleSheet("color:green;")
            self.show_step(self.grp_step2)
        else:
            self.lbl_step1_status.setText("Incorrect format! Please choose a .txt dataset")
            self.lbl_step1_status.setStyleSheet("color:red;")

    '''     functions for step2     '''

    def set_class_col(self):
        if self.rd_first.isChecked():
            self.class_col = 'first'
        elif self.rd_last.isChecked():
            self.class_col = 'last'

    def slider_value(self):
        self.train_data = self.sldr_data.value()
        self.lcd_data.display()
        self.lbl_step2_status.setText(str(self.train_data)+"% of dataset will be used as Training data.")
        self.lbl_step2_status.setStyleSheet("color:green;")

    def split_tr_data(self):
        self.set_class_col()
        self.tr = training.Training(self.data_path, self.class_col, self.train_data)
