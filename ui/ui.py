__author__ = 'soroush'
from PyQt4 import QtGui, uic
from core import training, testing
from math import sqrt

form_ui = uic.loadUiType("ui/mainWindow.ui")[0]


class PrimaryWindow(QtGui.QMainWindow, form_ui):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.data_path = None                   # dataset's path
        self.class_col = 'last'                 # class's column in dataset,by default it's the last column
        self.train_data = 50                    # amount of training data based on percent,by default is 50%
        self.tr = None
        self.selection_type = 'F'               # selection type of choosing training data,default is from first
        self.rd_last.setChecked(True)
        self.rd_from_first.setChecked(True)
        self.tree = None
        self.testing = None
        self.sldr_data.valueChanged.connect(self.slider_value)
        self.btn_choose_dataset.clicked.connect(self.check_file)
        self.btn_split_data.clicked.connect(self.split_tr_data)
        self.btn_begin_train.clicked.connect(self.begin_training)
        self.btn_begin_test.clicked.connect(self.begin_testing)
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
        self.grp_step3.hide()
        self.grp_step4.hide()
        self.grp_results.hide()
        a.show()

    def show_steps(self, a, b):
        self.grp_step1.hide()
        self.grp_step2.hide()
        self.grp_step3.hide()
        self.grp_step4.hide()
        self.grp_results.hide()
        a.show()
        b.show()

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

    def set_selection_type(self):
        if self.rd_from_first.isChecked():
            self.selection_type = 'F'
        elif self.rd_from_end.isChecked():
            self.selection_type = 'E'
        elif self.rd_from_random.isChecked():
            self.selection_type = 'R'

    def set_class_col(self):
        if self.rd_first.isChecked():
            self.class_col = 'first'
        elif self.rd_last.isChecked():
            self.class_col = 'last'

    def slider_value(self):
        self.train_data = self.sldr_data.value()
        self.lcd_data.display(self.train_data)
        self.lbl_step2_status.setText(str(self.train_data)+"% of dataset will be used as Training data.")
        self.lbl_step2_status.setStyleSheet("color:green;")

    def split_tr_data(self):
        self.set_class_col()
        self.set_selection_type()
        self.tr = training.Training(self.data_path, self.class_col, self.train_data, self.selection_type)
        self.show_steps(self.grp_step2, self.grp_step3)
        self.lbl_training_amount.setText('total rows of training data:'+str(self.tr.train_rows))
        self.lbl_all_amount.setText('total rows of whole data:'+str(self.tr.total_rows))

    def begin_training(self):
        self.show_step(self.grp_step3)
        c, d, e = self.tr.start_training()
        self.lbl_step3_status.setText('Tree created successfully!')
        self.lbl_step3_status.setStyleSheet("color:green;")
        self.show_step(self.grp_step4)
        self.testing = testing.Testing(c, d, e)

    def begin_testing(self):
        error = self.testing.start_testing()
        self.lbl_step4_status.setText("{0:.3f}".format(error)+'% of test data is error')
        self.show_steps(self.grp_step4, self.grp_results)
        predict = 100-error
        self.lbl_predict.setText("{0:.3f}".format(predict)+'%')
        standard = sqrt((error/100)*(predict/100)/100)
        self.lbl_standard.setText("{0:.3f}".format(standard))
        up_bound = predict+(1.96*standard)
        down_bound = predict-(1.96*standard)
        self.lbl_up_bound.setText("{0:.3f}".format(up_bound))
        self.lbl_down_bound.setText("{0:.3f}".format(down_bound))
        pass