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

def test_if_length_validator_negative():
    # input
    validator = LengthValidator('abc')
    # when
    result = validator.is_valid()
    # then
    assert result is False