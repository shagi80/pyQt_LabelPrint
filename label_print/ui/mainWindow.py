from PyQt5 import QtCore, QtGui, QtWidgets
from ui.storyListWidget import Ui_ListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 632)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.5, y2:0.5, stop:0 rgba(235, 235, 235, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftWidget = QtWidgets.QWidget(self.centralwidget)
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.leftWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ProductList = QtWidgets.QListView(self.leftWidget)
        self.ProductList.setAutoFillBackground(True)
        self.ProductList.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.ProductList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProductList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ProductList.setLineWidth(0)
        self.ProductList.setViewMode(QtWidgets.QListView.IconMode)
        self.ProductList.setObjectName("ProductList")
        self.verticalLayout.addWidget(self.ProductList)
        self.horizontalLayout.addWidget(self.leftWidget)
        self.rightWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightWidget.sizePolicy().hasHeightForWidth())
        self.rightWidget.setSizePolicy(sizePolicy)
        self.rightWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.rightWidget.setObjectName("rightWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.rightWidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.rightWidget)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.StoryArea = QtWidgets.QScrollArea(self.rightWidget)
        self.StoryArea.setStyleSheet("background-color: rgb(250, 250, 250);\n"
            "border-left: 1px solid rgb(200, 200, 200);\n"
            "border-top: 1px solid rgb(200, 200, 200);\n"
            "border-right: 2px solid rgb(210, 210, 210);\n"
            "border-bottom: 2px solid rgb(210, 210, 210);\n"
            "border-radius: 10px;")
        self.StoryArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StoryArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StoryArea.setLineWidth(0)
        self.StoryArea.setMidLineWidth(0)
        self.StoryArea.setWidgetResizable(True)
        self.StoryArea.setObjectName("StoryArea")


        self.StoryContents = Ui_ListWidget(self.StoryArea)
        self.StoryArea.setWidget(self.StoryContents)
        self.StoryContents.show()
        
        self.verticalLayout_2.addWidget(self.StoryArea)
        self.widget = QtWidgets.QWidget(self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 65))
        self.widget.setObjectName("widget")
        self.SettingsButton = QtWidgets.QToolButton(self.widget)
        self.SettingsButton.setGeometry(QtCore.QRect(400, 10, 52, 52))
        self.SettingsButton.setStyleSheet("")
        self.SettingsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/btnIcon/GearAndKey.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsButton.setIcon(icon)
        self.SettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.SettingsButton.setAutoRepeat(True)
        self.SettingsButton.setAutoExclusive(False)
        self.SettingsButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.SettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.SettingsButton.setAutoRaise(True)
        self.SettingsButton.setObjectName("SettingsButton")
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.rightWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.SettingsButton.clicked.connect(MainWindow.SettingsButtonClick) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def SettingsButtonClick(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Печать этикеток 2.0"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3e3e3e;\">Новое задание</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3e3e3e;\">Сохраненные задания</span></p></body></html>"))
import ui.btnIcons_rc
