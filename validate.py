
class NumberValidator():
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        for n in range(0 ,10):
            if str(n) in self.text:
                return True

        return False

class LetterValidator():
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        pass

class LengthValidator():
    def __init__(self, text, length=10) -> None:
        self.text = text
        self.length = length

    def is_valid(self):
        if len(self.text) == self.length:
            return True

        return False
            # 2 sposób
#       return len(self.text) == self.length
class SpecialCharactersValidator():
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        #sprawdza czy po każdym znaku czy jest false czy true (chy jest znakiem spec czy nie)
        char_list = []
        for char in self.text:
            char_list.append(not char.isalnum())

        return any(char_list)
                #1 wersja
#        for character in self.text:
#            if not character.isalnum():
#               return True
#        return False
                #2 wersja
#        return any([not char.isalnum() for char in self.text])