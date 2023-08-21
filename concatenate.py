import pytest

def test_concatenate():
    list_of_strings = ['string_1', 'string_2']
    expected_result = 'string_1 string_2'
    actual_result = ' '.join(list_of_strings)

    assert expected_result == actual_result


list_of_strings = ['string_1', 'string_2']

# Concatenate the strings in list_of_strings and print the result
print(' '.join(list_of_strings))