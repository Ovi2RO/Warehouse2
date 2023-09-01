from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_App(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 862)
        MainWindow.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                "border-color: rgb(103, 103, 103);\n"
                                "color: rgb(212, 212, 212);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.navbar_frame = QtWidgets.QFrame(self.centralwidget)
        self.navbar_frame.setGeometry(QtCore.QRect(0, 0, 941, 80))
        self.navbar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar_frame.setObjectName("navbar_frame")

        self.wh_label = QtWidgets.QLabel(self.navbar_frame)
        self.wh_label.setGeometry(QtCore.QRect(10, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.wh_label.setFont(font)
        self.wh_label.setObjectName("wh_label")

        self.welcome_label = QtWidgets.QLabel(self.navbar_frame)
        self.welcome_label.setGeometry(QtCore.QRect(660, 10, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")

        self.username_output = QtWidgets.QLabel(self.navbar_frame)
        self.username_output.setGeometry(QtCore.QRect(660, 30, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_output.setFont(font)
        self.username_output.setAlignment(QtCore.Qt.AlignCenter)
        self.username_output.setObjectName("username_output")

        self.pushButton = QtWidgets.QPushButton(self.navbar_frame)
        self.pushButton.setGeometry(QtCore.QRect(750, 53, 91, 20))
        self.pushButton.setObjectName("pushButton")

        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 80, 941, 741))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")

        self.list_output = QtWidgets.QLabel(self.main_frame)
        self.list_output.setGeometry(QtCore.QRect(26, 24, 891, 671))
        self.list_output.setText("")
        self.list_output.setObjectName("list_output")

        self.refresh_button = QtWidgets.QPushButton(self.main_frame)
        self.refresh_button.setGeometry(QtCore.QRect(160, 700, 141, 31))
        self.refresh_button.setObjectName("refresh_button")

        self.add_button = QtWidgets.QPushButton(self.main_frame)
        self.add_button.setGeometry(QtCore.QRect(310, 700, 141, 31))
        self.add_button.setObjectName("add_button")

        self.remove_button = QtWidgets.QPushButton(self.main_frame)
        self.remove_button.setGeometry(QtCore.QRect(460, 700, 141, 31))
        self.remove_button.setObjectName("remove_button")

        self.modify_button = QtWidgets.QPushButton(self.main_frame)
        self.modify_button.setGeometry(QtCore.QRect(610, 700, 141, 31))
        self.modify_button.setObjectName("modify_button")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wh_label.setText(_translate("MainWindow", "WareHouse"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome"))
        self.username_output.setText(_translate("MainWindow", "UserName"))
        self.pushButton.setText(_translate("MainWindow", "Sign Out"))
        self.refresh_button.setText(_translate("MainWindow", "View products"))
        self.add_button.setText(_translate("MainWindow", "Add product"))
        self.remove_button.setText(_translate("MainWindow", "Remove product"))
        self.modify_button.setText(_translate("MainWindow", "Modify entry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_App()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
