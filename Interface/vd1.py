import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 483)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Text Input Field
        self.TextInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextInput.setGeometry(QtCore.QRect(110, 120, 441, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TextInput.setFont(font)
        self.TextInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.TextInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.TextInput.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TextInput.setPlainText("")
        self.TextInput.setOverwriteMode(True)
        self.TextInput.setObjectName("TextInput")
        
        # Analysis Button
        self.analysis = QtWidgets.QPushButton(self.centralwidget)
        self.analysis.setGeometry(QtCore.QRect(590, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(13)
        font.setBold(True)
        self.analysis.setFont(font)
        self.analysis.setObjectName("analysis")
        
        # Vertical Layout for Output
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 340, 111, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Output Label
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        # Title Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        # Footer Label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 410, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # Input Label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        # Output Label
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 350, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        # Empty Label
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 340, 47, 41))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        
        # Set Central Widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Set the window title and labels text
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sentiment Analysis"))
        self.analysis.setText(_translate("MainWindow", "Analysis"))
        self.label_2.setText(_translate("MainWindow", "CHƯƠNG TRÌNH PHÂN TÍCH CẢM XÚC BÌNH LUẬN"))
        self.label_3.setText(_translate("MainWindow", "Design by Nguyen Thoai Linh and Nguyen Quoc Thai "))
        self.label_4.setText(_translate("MainWindow", "INPUT"))
        self.label_5.setText(_translate("MainWindow", "OUTPUT"))

# Main function to run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
