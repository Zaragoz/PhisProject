from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class UI_MyWindow(object):
    def seupUi(self, window):
        window.setWindowTitle("Phislab")
        window.resize(500,500)
        self.BoxLayout = QtWidgets.QVBoxLayout()
        window.setLayout(self.BoxLayout)
        self.edit = QtWidgets.QTextEdit("Ctrl V TASK")
        self.StartBtn = QtWidgets.QPushButton("Start")
        self.BoxLayout.addWidget(self.edit)
        self.BoxLayout.addWidget(self.StartBtn)
        self.task = self.edit.toPlainText()



class Answer(QtWidgets.QWidget):
    def __init__(self, task, parent=None):
        super(Answer, self).__init__(parent)
        self.setWindowTitle("Answer")
        self.resize(500,500)
        self.LabelAnswer = QtWidgets.QLabel("bitch")
        self.lay = QtWidgets.QVBoxLayout()
        self.setLayout(self.lay)
        self.lay.addWidget(self.LabelAnswer)



class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UI_MyWindow()
        self.ui.seupUi(self)
        self.ui.StartBtn.clicked.connect(self.start)
    def start(self):
        self.dialog = Answer(self)
        self.dialog.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
