# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1012, 722)
        Form.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 891, 601))
        self.label.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_arama = QtWidgets.QLineEdit(Form)
        self.lineEdit_arama.setGeometry(QtCore.QRect(250, 90, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_arama.setFont(font)
        self.lineEdit_arama.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_arama.setText("")
        self.lineEdit_arama.setObjectName("lineEdit_arama")
        self.pushButton_Ekle = QtWidgets.QPushButton(Form)
        self.pushButton_Ekle.setGeometry(QtCore.QRect(770, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Ekle.setFont(font)
        self.pushButton_Ekle.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(52, 52, 52);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(150, 150, 150);\n"
"}")
        self.pushButton_Ekle.setObjectName("pushButton_Ekle")
        self.pushButton_cikis = QtWidgets.QPushButton(Form)
        self.pushButton_cikis.setGeometry(QtCore.QRect(880, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cikis.setFont(font)
        self.pushButton_cikis.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(176, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.pushButton_like = QtWidgets.QPushButton(Form)
        self.pushButton_like.setGeometry(QtCore.QRect(120, 610, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_like.setFont(font)
        self.pushButton_like.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 152, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 254, 0);\n"
"}")
        self.pushButton_like.setObjectName("pushButton_like")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(110, 150, 791, 451))
        self.tableWidget.setMinimumSize(QtCore.QSize(791, 451))
        self.tableWidget.setMaximumSize(QtCore.QSize(791, 451))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.pushButton_dislike = QtWidgets.QPushButton(Form)
        self.pushButton_dislike.setGeometry(QtCore.QRect(320, 610, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_dislike.setFont(font)
        self.pushButton_dislike.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_dislike.setObjectName("pushButton_dislike")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 610, 241, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Arama Çubuğu"))
        self.lineEdit_arama.setPlaceholderText(_translate("Form", "Aramak İstediğiniz Tarifi Giriniz"))
        self.pushButton_Ekle.setText(_translate("Form", "Tarif Ekle"))
        self.pushButton_cikis.setText(_translate("Form", "Çıkış Yap"))
        self.pushButton_like.setText(_translate("Form", "Beğendim"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Yemek Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Malzemeler"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tarif"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Puan"))
        self.pushButton_dislike.setText(_translate("Form", "Beğenmedim"))
        self.label_3.setText(_translate("Form", "(Her Beğeni +1 puan her beğenmeme ise -1 puan)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
