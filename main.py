import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

import start_layout
import main_layout


# Данный класс отвечает за первое (начальное) окно
class StartMatches(QtWidgets.QMainWindow, start_layout.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self._timer = QtCore.QTimer
        self.setupUi(self)
        self.continue_btn.clicked.connect(self.data_matches)
        self.continue_btn.clicked.connect(self.close_start_app)

        self.quantity_matches = 0
        self.AI_or_player = None

    # функция, отвечающая за взаимодействие пользователя с интерфейсом
    def data_matches(self):
        # попытка записи введённых данных в переменные
        try:
            self.quantity_matches = int(self.max_matches_line.text())
            self.AI_or_player = int(self.AI_or_player_line.text())
            if self.quantity_matches > 20 or self.quantity_matches < 6:
                raise ValueError

            elif self.AI_or_player > 1 or self.AI_or_player < 0:
                raise ValueError

            self.main_app = MainMatches(self.quantity_matches, self.AI_or_player)
            self.main_app.show()

        # блок обработки неправильных введённых данных
        except ValueError:
            self.max_matches_line.setMaxLength(30)
            self.AI_or_player_line.setMaxLength(30)
            self.max_matches_line.setText("Введённые данные неправильны")
            self.AI_or_player_line.setText("Введённые данные неправильны")
            self.max_matches_line.setStyleSheet('color: red')
            self.AI_or_player_line.setStyleSheet('color: red')
            self._timer.singleShot(2000, lambda: self.max_matches_line.clear())
            self._timer.singleShot(2000, lambda: self.AI_or_player_line.clear())
            self._timer.singleShot(2000, lambda: self.max_matches_line.setStyleSheet('color: black'))
            self._timer.singleShot(2000, lambda: self.AI_or_player_line.setStyleSheet('color: black'))

    def close_start_app(self):
        start_app = StartMatches()
        start_app.close()


# Данный класс отвечает за второе (основное) окно
class MainMatches(QtWidgets.QMainWindow, main_layout.Ui_MainWindow):
    def __init__(self, quantity_matches, ai_or_player):
        super().__init__()
        self._timer = QtCore.QTimer
        self.setupUi(self)

        self.player_line.setDisabled(True)
        self.continue_btn.setDisabled(True)
        self.author1_line.setText(" Приветствую Вас в моей игре -Спички-")
        self.author2_line.setText(" Вы играете против игрока")
        self.author1_line.setStyleSheet('color: rgb(245, 245, 245)')

        self._timer.singleShot(2000, lambda: self.first_launch())
        self._timer.singleShot(2000, lambda: self.continue_btn.setEnabled(True))

        self.continue_btn.clicked.connect(self.first_launch)

        # Главные константы игры
        self.start = 0
        self.max_matches = 20
        self.max_take_matches = 3

        self.quantity_matches = quantity_matches
        self.AI_or_player = ai_or_player
        self.player1_take_matches = 0
        self.player2_take_matches = 0

    def first_launch(self):
        self.player_line.setEnabled(True)
        self.player_line.setFocus()
        print("first launch")

        self.continue_btn.clicked.disconnect(self.first_launch)
        self.continue_btn.clicked.connect(self.player1_turn)

    def manager_turns(self):
        print("manager turns")

        self.back = self.player1_turn()
        if self.back == 1:
            self._timer.singleShot(1000, lambda: self.player2_turn())

    def player1_turn(self):
        print("Ход 1")
        if self.quantity_matches > 0:
            try:
                # ход первого игрока
                self.author1_line.setText(" Ходит первый игрок")
                self.author2_line.clear()
                self.player_line.setPlaceholderText("Первый игрок, сколько Вы хотите взять спичек? (от 1 до 3)")

                self.player1_take_matches = int(self.player_line.text())
                if self.player1_take_matches > 3 or self.player1_take_matches < 1:
                    raise ValueError

                else:
                    self.check_ending()

                    self.quantity_matches = self.quantity_matches - self.player1_take_matches
                    # self.author2_line.setText(f" Ход сделан - {self.player1_take_matches} спичк{self.ending}")
                    self.player_line.clear()
                    if self.player_line.text() == "":
                        pass
                    self.player_line.setDisabled(True)
                    self.continue_btn.setDisabled(True)

                    self.continue_btn.clicked.disconnect(self.player1_turn)
                    self.continue_btn.clicked.connect(self.player2_turn)
                    self.player2_turn()

            except ValueError:
                self.player_line.setText("Введённые данные неправильны")
                self.player_line.setStyleSheet('color: red')
                self._timer.singleShot(2000, lambda: self.player_line.clear())
                self._timer.singleShot(2000, lambda: self.player_line.setStyleSheet('color: black'))

            finally:
                print(self.quantity_matches)

        else:
            self.author1_line.setText(" Выиграл второй игрок")
            self.author2_line.setText(" Хотите начать заново?")
            self.player_line.setPlaceholderText("")

    def player2_turn(self):
        print("Ход 2")
        if self.quantity_matches > 0:
            try:
                self.author1_line.setText(" Ходит второй игрок")
                self._timer.singleShot(1000, lambda: self.player_line.setEnabled(True))
                self._timer.singleShot(1000, lambda: self.continue_btn.setEnabled(True))

                # ход второго игрока
                self.player_line.setPlaceholderText("Второй игрок, сколько Вы хотите взять спичек? (от 1 до 3)")

                self.player2_take_matches = int(self.player_line.text())
                if self.player2_take_matches > 3 or self.player2_take_matches < 1:
                    raise ValueError

                elif self.player_line == "":
                    print("Пусто")

                else:
                    self.check_ending()

                    self.quantity_matches = self.quantity_matches - self.player2_take_matches
                    # self.author2_line.setText(f" Ход сделан - {self.player2_take_matches} спичк{self.ending}")
                    self.player_line.clear()
                    if self.player_line.text() == "":
                        pass
                    self.player_line.setDisabled(True)
                    self.continue_btn.setDisabled(True)

                    self.continue_btn.clicked.disconnect(self.player2_turn)
                    self.continue_btn.clicked.connect(self.player1_turn)
                    self.player1_turn()

            except ValueError:
                self.player_line.setText("Введённые данные неправильны")
                self.player_line.setStyleSheet('color: red')
                self._timer.singleShot(2000, lambda: self.player_line.clear())
                self._timer.singleShot(2000, lambda: self.player_line.setStyleSheet('color: black'))

            finally:
                print(self.quantity_matches)

        else:
            self.author1_line.setText(" Выиграл первый игрок")
            self.author2_line.setText(" Хотите начать заново?")
            self.player_line.setPlaceholderText("")

    def check_ending(self):
        if self.player1_take_matches == 1:
            self.ending = "а"

        else:
            self.ending = "и"

    def starting(self):
        self.start = 1


def main():
    start_app = QtWidgets.QApplication(sys.argv)
    start_window = StartMatches()
    start_window.show()
    sys.exit(start_app.exec_())


if __name__ == '__main__':
    main()
