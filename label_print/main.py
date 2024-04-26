import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
from ui.mainWindow import Ui_MainWindow # Это наш конвертированный файл дизайна
from ui.card import Ui_HistoryCardFrame


class HistoryCard(QtWidgets.QFrame, Ui_HistoryCardFrame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
    
    def SettingsButtonClick(self):
        areaHeight = 0
        for i in range(5):
            card = HistoryCard()
            y = 10 + (card.height() + 10) * i
            card.addToWidget(self.scrollAreaWidgetContents, 20, y)
            areaHeight = y + card.height() + 10
        self.scrollAreaWidgetContents.setMinimumSize(
            QtCore.QSize(0, areaHeight)
        )


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()