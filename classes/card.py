class Card:
    def __init__(self, card_value:int, card_type:str):
        if not 2 <= card_value <= 14:
            raise ValueError("Card value must be 2-14")
        if card_type not in ['H', 'D', 'S', 'C']:
            raise ValueError("Unsupported card type. Only: H, D, S, C")
        self.card_value = card_value
        self.card_type = card_type


    def __str__(self):
        return self.get_formated_value() + ' ' + self.get_formated_type()

    def get_formated_value(self):
        formated_value = ''
        match self.card_value:
            case 11:
                formated_value = 'J'
            case 12:
                formated_value = 'Q'
            case 13:
                formated_value = 'K'
            case 14:
                formated_value = 'A'
            case _:
                formated_value = str(self.card_value)
        return formated_value

    def get_formated_type(self) -> str:
        formated_type = ''
        match self.card_type:
            case 'H':
                formated_type = '♥'
            case 'D':
                formated_type = '♦'
            case 'S':
                formated_type = '♠'
            case 'C':
                formated_type = '♣'
        return formated_type