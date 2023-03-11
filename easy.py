# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easy.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.resize(800, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.folder_btn = QtWidgets.QPushButton(Form)
        self.folder_btn.setObjectName("folder_btn")
        self.verticalLayout.addWidget(self.folder_btn)
        self.listOfImage = QtWidgets.QListWidget(Form)
        self.listOfImage.setObjectName("listOfImage")
        self.verticalLayout.addWidget(self.listOfImage)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_lbl = QtWidgets.QLabel(Form)
        self.img_lbl.setObjectName("img_lbl")
        self.verticalLayout_2.addWidget(self.img_lbl)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_btn = QtWidgets.QPushButton(Form)
        self.left_btn.setObjectName("left_btn")
        self.horizontalLayout_2.addWidget(self.left_btn)
        self.right_btn = QtWidgets.QPushButton(Form)
        self.right_btn.setObjectName("right_btn")
        self.horizontalLayout_2.addWidget(self.right_btn)
        self.mirror_btn = QtWidgets.QPushButton(Form)
        self.mirror_btn.setObjectName("mirror_btn")
        self.horizontalLayout_2.addWidget(self.mirror_btn)
        self.sharp_btn = QtWidgets.QPushButton(Form)
        self.sharp_btn.setObjectName("sharp_btn")
        self.horizontalLayout_2.addWidget(self.sharp_btn)
        self.baw_btn = QtWidgets.QPushButton(Form)
        self.baw_btn.setObjectName("baw_btn")
        self.horizontalLayout_2.addWidget(self.baw_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 19)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Easy Editor v1.0"))
        self.folder_btn.setText(_translate("Form", "Папка"))
        self.img_lbl.setText(_translate("Form", "Зображення"))
        self.left_btn.setText(_translate("Form", "Ліворуч"))
        self.right_btn.setText(_translate("Form", "Праворуч"))
        self.mirror_btn.setText(_translate("Form", "Дзеркало"))
        self.sharp_btn.setText(_translate("Form", "Різкість"))
        self.baw_btn.setText(_translate("Form", "Ч/Б"))
class Window(Ui_Form):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(Window, self).__init__()
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)
    