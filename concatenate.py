def concatenate(list_of_strings):
    """Concatenate a list of strings into a single string."""
    
    # check if list_of_strings contains only strings
    for string in list_of_strings:
        if not isinstance(string, str):
            raise TypeError('list_of_strings must contain only strings!')
        
    # check for length of list_of_strings
    if list_of_strings == []:
        return ''
    elif len(list_of_strings) == 1:
        return list_of_strings[0]
    return ' '.join(list_of_strings)


if __name__ == '__main__':
    list_of_strings = ['string_1', 'string_2']
    print(concatenate(list_of_strings))