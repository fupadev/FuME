# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(487, 410)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Settings)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Settings)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept)
        self.buttonBox.rejected.connect(Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Einstellungen"))
        self.groupBox.setTitle(_translate("Settings", "Cookies"))
        self.label_3.setText(_translate("Settings", "<html><head/><body><p>Erstelle hier deinen Cookie für die Vereinsverwaltung. Diesen benötigst du z.B. fürs Reservieren von Spielen. Es werden keine Passwörter gespeichert. <a href=\"https://www.google.com/chrome/browser/desktop/index.html\"><span style=\" text-decoration: underline; color:#0000ff;\">Google Chrome</span></a> wird benötigt.</p></body></html>"))
        self.label.setText(_translate("Settings", "E-Mail:"))
        self.lineEdit.setText(_translate("Settings", "beispiel@domain.de"))
        self.label_2.setText(_translate("Settings", "Passwort:"))
        self.lineEdit_2.setText(_translate("Settings", "Beispiel"))
        self.pushButton.setText(_translate("Settings", "Cookie erzeugen"))
        self.groupBox_2.setTitle(_translate("Settings", "Erweiterte Einstellungen"))
        self.pushButton_2.setText(_translate("Settings", "Einstelungen zurücksetzen"))
        self.pushButton_3.setText(_translate("Settings", "Datenbank zurücksetzen"))
        self.checkBox.setToolTip(_translate("Settings", "Browser Fenster verstecken"))
        self.checkBox.setText(_translate("Settings", "Google Chrome headless (macOS: Chrome 59/Windows: Chrome 60)"))

