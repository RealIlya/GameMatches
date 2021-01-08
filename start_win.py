import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

import start_layout
import PVP
import PVE

version = "v1.0.2 BETA"


# Данный класс отвечает за первое (начальное) окно
class StartWin(QtWidgets.QMainWindow, start_layout.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._timer = QtCore.QTimer
        self.setupUi(self)
        self.setWindowTitle("Matches {0}".format(version))
        self.setWindowIcon(QIcon('matches.png'))

        self.continue_btn.clicked.connect(self.record)

        self.quantity_matches = 0
        self.AI_or_player = None

    # Запись выборов игрока: сколько будет спичек в игре, против кого он будет играть
    def record(self):
        # попытка записи введённых данных в переменные
        try:
            self.quantity_matches = int(self.max_matches_line.text())
            self.AI_or_player = int(self.AI_or_player_line.text())
            if self.quantity_matches > 20 or self.quantity_matches < 6:
                raise ValueError
            elif self.AI_or_player > 1 or self.AI_or_player < 0:
                raise ValueError

            self.close()  # закрытие StartWin
            if self.AI_or_player == 0:
                self.main_win_pve = PVE.MainWinPVE(self.quantity_matches
                                                   )
                self.main_win_pve.show()

            if self.AI_or_player == 1:
                self.main_win_pvp = PVP.MainWinPVP(self.quantity_matches  # создание экземпляра класса MainWinPVP с
                                                   )  # данными о выборах игрока
                self.main_win_pvp.show()  # показ main_win_pvp

        # блок обработки неправильно введённых данных
        except ValueError:
            self.max_matches_line.setText("Введённые данные неправильны")
            self.AI_or_player_line.setText("Введённые данные неправильны")
            self.max_matches_line.setStyleSheet('color: red')
            self.AI_or_player_line.setStyleSheet('color: red')
            self._timer.singleShot(2000, lambda: self.max_matches_line.clear())
            self._timer.singleShot(2000, lambda: self.AI_or_player_line.clear())
            self._timer.singleShot(2000, lambda: self.max_matches_line.setStyleSheet('color: black'))
            self._timer.singleShot(2000, lambda: self.AI_or_player_line.setStyleSheet('color: black'))


# Запуск игры
def main():
    start_app = QtWidgets.QApplication(sys.argv)
    start_win = StartWin()
    start_win.show()
    sys.exit(start_app.exec_())


if __name__ == '__main__':
    main()
