from validate import NumberValidator, SpecialCharactersValidator, LengthValidator

def test_if_has_number_validator_positive():
    # input
    validator = NumberValidator('abc123')
    # when
    result = validator.is_valid()
    # then
    assert result is True

def test_if_has_number_validator_negative():
    # input
    validator = NumberValidator('abc')
    # when
    result = validator.is_valid()
    # then
    assert result is False

def test_if_has_special_character_validator_positive():
    # input
    validator = SpecialCharactersValidator('abc123,:.- ')
    # when
    result = validator.is_valid()
    # then
    assert result is True


def test_if_has_special_character_validator_negative():
    # input
    validator = SpecialCharactersValidator('abc')
    # when
    result = validator.is_valid()
    # then
    assert result is False

def test_if_length_validator_positive():
    # input
    validator = LengthValidator('17.07.1989')
    # when
    result = validator.is_valid()
    # then
    assert result is True

    validator = LengthValidator('17:44',5)      # znaki i jako 2 wartość ilość znaków aby wyszło true
    # when
    result = validator.is_valid()
    # then
    assert result is True

def test_if_length_validator_negative():
    # input
    validator = LengthValidator('abc')
    # when
    result = validator.is_valid()
    # then
    assert result is False

    validator = LengthValidator('17:44',6)      # znaki i 6 jako ilość znaków aby wyszedłó false (jest 5)
    # when
    result = validator.is_valid()
    # then
    assert result is False