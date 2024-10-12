import sys
import main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox


class Ui1_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.Dialog)
        MainWindow.resize(590, 360)
        palette = QtGui.QPalette()
        palette.setBrush(MainWindow.backgroundRole(), QBrush(
            QPixmap('C:/Users/Lenovo/PycharmProjects/PyQt5-YOLOv5-master/112.jpg').scaled(MainWindow.size(),
                                                     QtCore.Qt.IgnoreAspectRatio,
                                                     QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Lenovo/PycharmProjects/PyQt5-YOLOv5-master/113.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 120, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 120, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 170, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setValidator(QtGui.QIntValidator(0, 999999))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 210, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open)
        self.lineEdit_2.editingFinished.connect(self.open)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 210, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 60, 251, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "目标检测系统"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#ffffff;\">用户名：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">密  码：</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ffffff;\">欢迎进入系统！</span></p></body></html>"))

    def open(self):
        self.username = self.lineEdit.text()  # 记录用户名
        self.userpassword = self.lineEdit_2.text()  # 记录密码
        if self.userpassword == '123456' and self.username == '123456':
            self.second = main.MainWindow()
            self.second.show()
            MainWindow.hide()
        else:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)


# 主方法设置在登录界面内
if __name__ == "__main__":
    # 创建QApplication类的实例
    app = QtWidgets.QApplication(sys.argv)
    # 创建一个窗口
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui1_MainWindow()
    # 主窗口添加控件
    ui.setupUi(MainWindow)
    # 显示窗口
    MainWindow.show()
    # 进入程序的主循环，通过EXIT确保主函数循环安全
    sys.exit(app.exec_())
