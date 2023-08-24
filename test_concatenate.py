from concatenate import concatenate

class TestConcatenate(object):
    def test_concatenate(self):
        list_of_strings = ['string_1', 'string_2']
        assert 'string_1 string_2' == concatenate(list_of_strings)

    def test_concatenate_empty_list(self):
        list_of_strings = []
        assert '' == concatenate(list_of_strings)

    def test_concatenate_single_item(self):
        list_of_strings = ['string_1']
        assert 'string_1' == concatenate(list_of_strings)

    def test_concatenate_raises_type_error(self):
        list_of_strings = ['string_1', 1]
        try:
            concatenate(list_of_strings)
        except TypeError:
            assert True
        else:
            assert False