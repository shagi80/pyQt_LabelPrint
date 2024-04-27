from PyQt5 import QtCore, QtGui, QtWidgets

from ui.storyCardFrame import Ui_CardFrame



class Ui_ListWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.retranslateUi(self)
        self.setParent(parent)

    def setupUi(self):
        self.setObjectName("historyListWidget")
        self.setGeometry(0, 0, 0, 0)
        self.setStyleSheet("background-color: rgb(235, 35, 235);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")


    def addItemList(self, itemList):
        for item in itemList:
            card = Ui_CardFrame(self)
            card.setObjectName('card' + item)
            card.title = 'test'
            self.verticalLayout.addWidget(card)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("historyListWidget", "historyListWidget"))
