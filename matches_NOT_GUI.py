class Matches:
    def __init__(self):
        # Главные константы игры
        self.game_running = 1
        self.max_matches = 20
        self.max_take_matches = 3

        self.chose_matches = 0
        self.AI_or_player = None
        self.player1_take_matches = 0
        self.player2_take_matches = 0

    def main(self):
        while self.game_running:
            print("\n====   Приветствую Вас в моей игре -Спички-   ====\n"
                  "====   Для начала, нужно указать параметры игры   ====")
            self.chose_matches = int(input("Первое, установите количество спичек в игре (от 6 до 20): "))

            if self.chose_matches > self.max_matches or self.chose_matches < 6:  # or 1 > self.num_take_matches or self.max_take_matches < self.num_take_matches
                print("Введено неправильное значение")
                self.game_running = 0

            # Сама игра
            else:
                self.AI_or_player = int(input("Второе, выберите против кого будете играть (0 - ИИ, 1 - игрок): "))

                if self.AI_or_player == 0:
                    self.vs_ai()

                elif self.AI_or_player == 1:
                    self.vs_player()
                    self.game_running = int(input("Хотите повторить? (1 - да, 0 - нет): "))

                else:
                    print("Введено неправильное значение")
                    self.game_running = 0

    # диапазон количества спичек
    def range_take_matches(self, player):
        if (self.player1_take_matches > 3 or self.player1_take_matches < 1) or \
                (self.player2_take_matches > 3 or self.player2_take_matches < 1):
            print("Неправильно, попробуйте ещё раз")
            if player == 1:
                self.player1_take_matches = int(input("Первый игрок, сколько Вы хотите взять спичек? (от 1 до 3): "))
            if player == 2:
                self.player2_take_matches = int(input("Второй игрок, сколько Вы хотите взять спичек? (от 1 до 3): "))

    # игра против ИИ
    def vs_ai(self):
        pass

    # игра против игрока
    def vs_player(self):
        print("==== Вы выбрали режим игры -Против игрока- ====")

        vs_player_running = True
        while vs_player_running:
            print("==== Ходит первый игрок ====")
            self.player1_take_matches = int(input("Первый игрок, сколько Вы хотите взять спичек? (от 1 до 3): "))
            self.range_take_matches(1)
            self.chose_matches = self.chose_matches - self.player1_take_matches
            if self.chose_matches <= 0:
                print("Проигрышь 1")
                break
            print("==== Ход сделан ====")
            print(f"Количество спичек - {self.chose_matches}")
            print("==== Ходит второй игрок ====")
            self.player2_take_matches = int(input("Второй игрок, сколько Вы хотите взять спичек? (от 1 до 3): "))
            self.range_take_matches(2)
            self.chose_matches = self.chose_matches - self.player2_take_matches
            if self.chose_matches <= 0:
                print("Проигрышь 2")
                break
            print("==== Ход сделан ====")
            print(f"Количество спичек - {self.chose_matches}")


if __name__ == '__main__':
    matches = Matches()
    matches.main()
