import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

import start_layout
import main_layout

version = "v1.0"


# Данный класс отвечает за первое (начальное) окно
class StartMatches(QtWidgets.QMainWindow, start_layout.Ui_MainWindow):
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

            self.close()  # закрытие StartMatches
            self.main_window = MainMatches(self.quantity_matches,  # создание экземпляра класса MainMatches с
                                           self.AI_or_player)  # данными о выборах игрока
            self.main_window.show()  # показ main_window

        # блок обработки неправильно введённых данных
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
            self._timer.singleShot(2000, lambda: self.max_matches_line.setMaxLength(2))
            self._timer.singleShot(2000, lambda: self.AI_or_player_line.setMaxLength(1))


# Данный класс отвечает за второе (основное) окно
class MainMatches(QtWidgets.QMainWindow, main_layout.Ui_MainWindow):
    def __init__(self, quantity_matches, ai_or_player):
        super().__init__()
        self._timer = QtCore.QTimer
        self.setupUi(self)
        self.setWindowTitle("Matches {0}".format(version))
        self.setWindowIcon(QIcon('matches.png'))

        self.player_line.setDisabled(True)
        self.continue_btn.setDisabled(True)
        self.author1_line.setStyleSheet('color: rgb(240, 240, 240)')
        self.author1_line.setText(" Приветствую Вас в моей игре -Спички-")
        self.author2_line.setText(" Вы играете против игрока")
        self._timer.singleShot(2000, lambda: self.author1_line.clear())
        self._timer.singleShot(2000, lambda: self.author2_line.setText(" И так, начнём игру"))

        self._timer.singleShot(2500, lambda: self.first_launch())
        self._timer.singleShot(2500, lambda: self.continue_btn.setEnabled(True))

        self.continue_btn.clicked.connect(self.first_launch)

        self.restart_btn.clicked.connect(self.restart_game)
        self.exit_btn.clicked.connect(exit)
        self.restart_btn.setVisible(False)
        self.exit_btn.setVisible(False)

        # Главные переменные игры
        self.quantity_matches = quantity_matches
        self.AI_or_player = ai_or_player
        self.player1_take_matches = 0
        self.player2_take_matches = 0

    # Первый запуск игры
    def first_launch(self):
        self.player_line.setEnabled(True)
        self.player_line.setFocus()
        self.player_line.setPlaceholderText("Первый игрок, сколько Вы хотите взять спичек? (от 1 до 3)")

        self.continue_btn.clicked.disconnect(self.first_launch)
        self.continue_btn.clicked.connect(self.player1_turn)

    # Ход первого игрока
    def player1_turn(self):
        # игра продолжается, пока quantity_matches > 0
        if self.quantity_matches > 0:
            try:
                self.author1_line.setText(" Ходит первый игрок")
                self.author2_line.setText(" Осталось спичек - {0}".format(self.quantity_matches))

                self.player_line.setPlaceholderText("Первый игрок, сколько Вы хотите взять спичек? (от 1 до 3)")

                # если строчка не пуста, то взятые игроком спички отнимаются от их общего числа
                if self.player_line.text() != "":
                    self.player1_take_matches = int(self.player_line.text())

                    if self.player1_take_matches > 3 or self.player1_take_matches < 1:
                        raise ValueError
                    else:
                        self.quantity_matches = self.quantity_matches - self.player1_take_matches
                        self.player_line.clear()
                        self.continue_btn.setDisabled(True)

                        # конец хода 1 игрока
                        self.continue_btn.clicked.disconnect(self.player1_turn)  # кнопка отключается от player1_turn
                        self.continue_btn.clicked.connect(self.player2_turn)  # кнопка подключается к player2_turn
                        self.player2_turn()  # вызывается player2_turn

            # блок обработки неправильно введённых данных
            except ValueError:
                self.exception_handling()

        # проигрышь первого игрока, выигрышь второго игрока
        else:
            self.end_game(1)

    # Ход второго игрока
    def player2_turn(self):
        # игра продолжается, пока quantity_matches > 0
        if self.quantity_matches > 0:
            try:
                self.author1_line.setText(" Ходит второй игрок")
                self.author2_line.setText(" Осталось спичек - {0}".format(self.quantity_matches))

                self._timer.singleShot(500, lambda: self.player_line.setFocus())
                self._timer.singleShot(500, lambda: self.continue_btn.setEnabled(True))
                self.player_line.setPlaceholderText("Второй игрок, сколько Вы хотите взять спичек? (от 1 до 3)")

                # если строчка не пуста, то взятые игроком спички отнимаются от их общего числа
                if self.player_line.text() != "":
                    self.player2_take_matches = int(self.player_line.text())

                    if self.player2_take_matches > 3 or self.player2_take_matches < 1:
                        raise ValueError
                    else:
                        self.quantity_matches = self.quantity_matches - self.player2_take_matches
                        self.player_line.clear()
                        self.continue_btn.setDisabled(True)

                        self.continue_btn.clicked.disconnect(self.player2_turn)  # кнопка отключается от player2_turn
                        self.continue_btn.clicked.connect(self.player1_turn)  # кнопка подключается к player1_turn
                        self.player1_turn()  # вызывается player1_turn

            # блок обработки неправильно введённых данных
            except ValueError:
                self.exception_handling()

        # проигрышь второго игрока, выигрышь первого игрока
        else:
            self.end_game(2)

    # Подведение итогов
    def end_game(self, player):
        if player == 1:
            self.author1_line.setText(" Выиграл первый игрок")
            self.continue_btn.clicked.disconnect(self.player1_turn)
        elif player == 2:
            self.author1_line.setText(" Выиграл второй игрок")
            self.continue_btn.clicked.disconnect(self.player2_turn)

        self.author2_line.setText(" Хотите начать заново?")
        self.player_line.setPlaceholderText("")
        self.player_line.setDisabled(True)

        self.continue_btn.setVisible(False)

        self.restart_btn.setVisible(True)
        self.exit_btn.setVisible(True)

    # Перезапуск игры
    def restart_game(self):
        self.close()  # закрытие MainMatches
        self.start_window = StartMatches()  # создание экземпляра класса StartMatches
        self.start_window.show()  # показ start_window

    # Обработка исключений
    def exception_handling(self):
        self.player_line.setText("Введённые данные неправильны")
        self.player_line.setStyleSheet('color: red')
        self._timer.singleShot(2000, lambda: self.player_line.clear())
        self._timer.singleShot(2000, lambda: self.player_line.setStyleSheet('color: black'))


# Запуск игры
def main():
    start_app = QtWidgets.QApplication(sys.argv)
    start_window = StartMatches()
    start_window.show()
    sys.exit(start_app.exec_())


if __name__ == '__main__':
    main()
