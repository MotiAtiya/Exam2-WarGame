class UserInput:
    @staticmethod
    def ask_choice(minimum, maximum):
        while True:
            try:
                choice = int(input(f"Enter your choice [{minimum}-{maximum}]: "))
                if not minimum <= choice <= maximum:
                    print("Invalide choice")
                else:
                    return choice
            except ValueError:
                print("Enter only Integer number")
        