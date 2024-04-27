from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardFrame(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        #QtCore.QMetaObject.connectSlotsByName(self)
        self.retranslateUi(self)
        self.setParent(parent)

    def setupUi(self):
        self.setObjectName("Card")
        self.resize(415, 103)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "border: none;\n"
            "color: navy\n"
            "font-weight: bold;\n"
            "font-size: large;"
            )
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border: none;")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("border: none;")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("CardFrame", "CardFrame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">RENOVA SG5G-1ETW(ICTDW)</span></p></body></html>"))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Смена А, 23 апреля 2024 г</span></p></body></html>"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Номера с 101 по 999</span></p></body></html>"))

    def set_title(self, value):
        self.label.setText(value)
    
    title = property(fset=set_title)