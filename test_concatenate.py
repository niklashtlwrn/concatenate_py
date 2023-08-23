from concatenate import concatenate

def test_concatenate():
    list_of_strings = ['string_1', 'string_2']
    assert 'string_1 string_2' == concatenate(list_of_strings)