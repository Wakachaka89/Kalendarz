
class NumberValidator():            #sprawdza czy ma cyfry od 0-9
    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        for n in range(0 ,10):
            if str(n) in self.text:
                return True

        return False

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

class TextValidator():
    def __init__(self,input) -> None:
        self.input = input
        self.validators = [
            LengthValidator,
            NumberValidator,
            SpecialCharactersValidator
        ]
    def is_valid(self):
        for class_name in self.validators:
            validator = class_name(self.input)
            if validator.is_valid() is False:
                return False
        return True

text = TextValidator('l1l!567890')
print(text.is_valid())