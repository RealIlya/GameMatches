import main_layout
from start_win import *


# Данный класс отвечает за второе окно, игра идёт против игрока
class MainWinPVP(QtWidgets.QMainWindow, main_layout.Ui_MainWindow):
    def __init__(self, quantity_matches):
        super().__init__()
        self._timer = QtCore.QTimer
        self.setupUi(self)
        self.setWindowTitle("MatchesPVP")
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
        self.exit_btn.clicked.connect(sys.exit)
        self.restart_btn.setVisible(False)
        self.exit_btn.setVisible(False)

        # Главные переменные игры
        self.quantity_matches = quantity_matches
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
        self.close()  # закрытие MainWinPVP
        self.start_win = StartWin()  # создание экземпляра класса StartWin
        self.start_win.show()  # показ start_win

    # Обработка исключений
    def exception_handling(self):
        self.player_line.setText("Введённые данные неправильны")
        self.player_line.setStyleSheet('color: red')
        self._timer.singleShot(2000, lambda: self.player_line.clear())
        self._timer.singleShot(2000, lambda: self.player_line.setStyleSheet('color: black'))
