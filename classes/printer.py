import os
from .card import Card


class Printer:
    @staticmethod
    def display_round_result(player_card:Card, computer_card:Card, winner, player_card_numbers, computer_card_numbers):
        Printer.claer_screen()
        print("========== TURN ==========\n")
        print("Player:".ljust(15), "Computer:")
        Printer.show_two_cards(player_card, computer_card)

        if winner is None:
            print("It's a draw!")
        else:
            print(winner, "won the round!")
        print("Player cards:", player_card_numbers, '|', "Computer cards:", computer_card_numbers)
        print("\n==========================\n")


    @staticmethod
    def claer_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

    @staticmethod
    def display_menu(menu, title = None):
        if title:
            Printer.claer_screen()
            print('=' * (16 + len(title)))
            print(' ' * 7, title.upper(), ' ' * 7)
            print('=' * (16 + len(title)))
            print()
        for num, describe in menu.items():
            print(f"{num}. {describe}")
        print()

    @staticmethod
    def show_two_cards(p:Card, c:Card):
        print(f"""
+-------+       +-------+
| {p.get_formated_value():<2}    |       | {c.get_formated_value():<2}    |
|       |       |       |
|   {p.get_formated_type()}   |       |   {c.get_formated_type()}   |
|       |       |       |
|    {p.get_formated_value():>2} |       |    {c.get_formated_value():>2} |
+-------+       +-------+
""")