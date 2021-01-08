import main_layout
from start_win import *


# Данный класс отвечает за второе окно, игра идёт против Бота
class MainWinPVE(QtWidgets.QMainWindow, main_layout.Ui_MainWindow):
    def __init__(self, quantity_matches):
        super().__init__()
        self._timer = QtCore.QTimer
        self.setupUi(self)
        self.setWindowTitle("MatchesPVE")
        self.setWindowIcon(QIcon('matches.png'))

        self.player_line.setDisabled(True)
        self.continue_btn.setDisabled(True)
        self.author1_line.setStyleSheet('color: rgb(240, 240, 240)')
        self.author1_line.setText(" Приветствую Вас в моей игре -Спички-")
        self.author2_line.setText(" Режим игры - «Против Бота»")
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
        self.player_take_matches = 0
        self.bot_take_matches = 0

    # Первый запуск игры
    def first_launch(self):
        self.player_line.setEnabled(True)
        self.player_line.setFocus()
        self.player_line.setPlaceholderText("Первый игрок, сколько Вы хотите взять спичек? (от 1 до 3)")

        self.continue_btn.clicked.disconnect(self.first_launch)
        self.continue_btn.clicked.connect(self.player_turn)

    # Ход Игрока
    def player_turn(self):
        # игра продолжается, пока quantity_matches > 0
        if self.quantity_matches > 0:
            try:
                self.author1_line.setText(" Ходит первый игрок")
                self.author2_line.setText(" Осталось спичек - {0}".format(self.quantity_matches))

                self.player_line.setPlaceholderText("Игрок, сколько Вы хотите взять спичек? (от 1 до 3)")
                self.player_line.setEnabled(True)

                # если строчка не пуста, то взятые Игроком спички отнимаются от их общего числа
                if self.player_line.text() != "":
                    self.player_take_matches = int(self.player_line.text())

                    if self.player_take_matches > 3 or self.player_take_matches < 1:
                        raise ValueError
                    else:
                        self.quantity_matches = self.quantity_matches - self.player_take_matches
                        self.player_line.clear()
                        self.continue_btn.setDisabled(True)

                        # конец хода 1 игрока
                        self.continue_btn.clicked.disconnect(self.player_turn)  # кнопка отключается от player_turn
                        self.continue_btn.clicked.connect(self.bot_turn)  # кнопка подключается к bot_turn
                        self.bot_turn()  # вызывается bot_turn

            # блок обработки неправильно введённых данных
            except ValueError:
                self.exception_handling()

        # проигрышь Бота, выигрышь Игрока
        else:
            self.end_game(1)

    # Ход Бота
    def bot_turn(self):
        # игра продолжается, пока quantity_matches > 0
        if self.quantity_matches > 0:
            try:
                self.author1_line.setText(" Ходит бот")
                self.author2_line.setText(" Осталось спичек - {0}".format(self.quantity_matches))

                self._timer.singleShot(500, lambda: self.player_line.setFocus())
                self._timer.singleShot(500, lambda: self.continue_btn.setEnabled(True))
                self.player_line.setPlaceholderText("Бот делает ход...")
                self.player_line.setDisabled(True)

                turns = [3, 2, 1]
                bot_take_matches = 0
                quantity_matches = self.quantity_matches

                for i in turns:
                    bot_take_matches = bot_take_matches + quantity_matches // i
                    quantity_matches = quantity_matches % i

                bot_take_matches //= 2
                self.bot_take_matches = bot_take_matches if bot_take_matches != 0 else 1

                self.player_line.setText(str(self.bot_take_matches))

                # если строчка не пуста, то взятые Ботом спички отнимаются от их общего числа
                if self.player_line.text() != "":
                    self.quantity_matches = self.quantity_matches - self.bot_take_matches
                    self.player_line.clear()
                    self.continue_btn.setDisabled(True)
                    self.continue_btn.click()

                    self.continue_btn.clicked.disconnect(self.bot_turn)  # кнопка отключается от bot_turn
                    self.continue_btn.clicked.connect(self.player_turn)  # кнопка подключается к player_turn
                    self.player_turn()  # вызывается player_turn

            # блок обработки неправильно введённых данных
            except ValueError:
                self.exception_handling()

        # проигрышь Игрока, выигрышь Бота
        else:
            self.end_game(2)

    # Подведение итогов
    def end_game(self, player):
        if player == 1:
            self.author1_line.setText(" Выиграл игрок")
        elif player == 2:
            self.author1_line.setText(" Выиграл бот")

        self.author2_line.setText(" Хотите начать заново?")
        self.player_line.setPlaceholderText("")
        self.player_line.setDisabled(True)

        self.continue_btn.setVisible(False)

        self.restart_btn.setVisible(True)
        self.exit_btn.setVisible(True)

    # Перезапуск игры
    def restart_game(self):
        self.close()  # закрытие MainWinPVE
        self.start_win = StartWin()  # создание экземпляра класса StartWin
        self.start_win.show()  # показ start_win

    # Обработка исключений
    def exception_handling(self):
        self.player_line.setText("Введённые данные неправильны")
        self.player_line.setStyleSheet('color: red')
        self._timer.singleShot(2000, lambda: self.player_line.clear())
        self._timer.singleShot(2000, lambda: self.player_line.setStyleSheet('color: black'))
