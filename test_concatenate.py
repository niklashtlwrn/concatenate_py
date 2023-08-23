from concatenate import concatenate

def test_concatenate():
    list_of_strings = ['string_1', 'string_2']
    assert 'string_1 string_2' == concatenate(list_of_strings)

def test_concatenate_empty_list():
    list_of_strings = []
    assert '' == concatenate(list_of_strings)

def test_concatenate_single_item():
    list_of_strings = ['string_1']
    assert 'string_1' == concatenate(list_of_strings)

def test_concatenate_raises_type_error():
    list_of_strings = ['string_1', 1]
    try:
        concatenate(list_of_strings)
    except TypeError:
        assert True
    else:
        assert False