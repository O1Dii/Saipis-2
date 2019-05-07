from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_ok.clicked.connect(self.ok_clicked)
        self.ui.button_clear.clicked.connect(self.clear)
        self.ui.button_quit.clicked.connect(self.quit)

    def ok_clicked(self):
        R_1 = (0.1 * self.ui.rightSpinBox_1.value() + self.ui.rightDoubleSpinBox_1.value()) / 2
        R_2 = (0.1 * self.ui.rightSpinBox_2.value() + self.ui.rightDoubleSpinBox_2.value()) / 2
        self.ui.R_1.setText(str(round(R_1, 3)))
        self.ui.R_2.setText(str(round(R_2, 3)))
        N_1 = R_1 / (R_1 + R_2)
        N_2 = R_2 / (R_1 + R_2)
        self.ui.N_1.setText(str(round(N_1, 3)))
        self.ui.N_2.setText(str(round(N_2, 3)))
        W_1 = self.ui.doubleSpinBox_1.value() * N_1 + self.ui.doubleSpinBox_4.value() * N_2
        W_2 = self.ui.doubleSpinBox_2.value() * N_1 + self.ui.doubleSpinBox_5.value() * N_2
        W_3 = self.ui.doubleSpinBox_3.value() * N_1 + self.ui.doubleSpinBox_6.value() * N_2
        self.ui.W_1.setText(str(round(W_1, 3)))
        self.ui.W_2.setText(str(round(W_2, 3)))
        self.ui.W_3.setText(str(round(W_3, 3)))
        self.ui.output.setText(f'Z1={W_1}, Z2={W_2}, Z3={W_3}')

    def clear(self):
        self.ui.doubleSpinBox_1.setValue(0)
        self.ui.doubleSpinBox_2.setValue(0)
        self.ui.doubleSpinBox_3.setValue(0)
        self.ui.doubleSpinBox_4.setValue(0)
        self.ui.doubleSpinBox_5.setValue(0)
        self.ui.doubleSpinBox_6.setValue(0)
        self.ui.rightSpinBox_1.setValue(0)
        self.ui.rightSpinBox_2.setValue(0)
        self.ui.rightDoubleSpinBox_1.setValue(0)
        self.ui.rightDoubleSpinBox_2.setValue(0)
        self.ui.R_1.clear()
        self.ui.R_2.clear()
        self.ui.N_1.clear()
        self.ui.N_2.clear()
        self.ui.W_1.clear()
        self.ui.W_2.clear()
        self.ui.W_3.clear()
        self.ui.output.clear()

    def quit(self):
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MyWindow()
    mw.show()
    sys.exit(app.exec_())
