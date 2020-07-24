abc_en: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

key_dict: dict = {
    'a': 'c',
    'b': 'z',
    'z': '('
}

text: str = 'abba'



def encode_dict(string, keys):
    """
    Encodes a string making use of a dictionary where the keys are the alphabet characters and the values the characters
    to encode to.
    :param string:
    :param keys:
    :return coded string:
    """
    for key in keys:
        while key in string:
            string = string.replace(key, keys[key])
    return string

def decode_dict(string, keys):
    """
    Decodes a string making use of a dictionary where the keys are the alphabet characters and the values the characters
    to encode to.
    :param string:
    :param keys:
    :return decoded string:
    """
    for key in keys:
        while keys[key] in string:
            string = string.replace(keys[key], key)
    return string


def encode_cesar(string, shift, abc=None):
    """
    Encodes a string with cesar method
    :param string:
    :param shift:
    :param abc:
    :return coded string:
    """
    if abc is None:
        abc = abc_en.copy()
    if not (type(abc) == tuple or type(abc) == list):
        return False
    string = str(string)
    chars = []
    for char in string:
        if not char in chars:
            if abs(shift) > len(abc):
                this_shift = shift - (int(shift / len(abc)) * len(abc))
            else:
                this_shift = shift
            try:
                new_index = abc.index(char) + this_shift
            except ValueError:
                break
            if abs(new_index) > len(abc):
                diff = new_index - len(abc)
                print('-difference is: {}'.format(diff))
                new_index = (-(new_index / abs(new_index))) * diff
                print('-new_index is: {}'.format(new_index))
            string = string.replace(char, abc[int(new_index)])
        chars.append(char)
    return string

def decode_cesar(string, shift, abc=None):
    """
    Decodes a string with cesar method
    :param string:
    :param shift:
    :param abc:
    :return decoded string:
    """
    if abc is None:
        abc = abc_en.copy()
    if not (type(abc) == tuple or type(abc) == list):
        return False
    string = str(string)
    chars = []
    for char in string:
        if not char in chars:
            if abs(shift) > len(abc):
                this_shift = shift - (int(shift / len(abc)) * len(abc))
            else:
                this_shift = shift
            try:
                new_index = abc.index(char) - this_shift
            except ValueError:
                break
            string = string.replace(char, abc[new_index])
            chars.append(char)
    return string


def encode_affine(string, a, b, abc=None):
    """
    Encodes a string with the affine method
    :param string:
    :param a:
    :param b:
    :param abc:
    :return coded string:
    """
    if abc is None:
        abc = abc_en.copy()
    if type(abc) == list:
        abc = abc.copy()
    if not type(abc) == tuple:
        return False
    string = str(string)
    new_string = ''
    for char in string:
        try:
            new_index = a * abc.index(char) + b
        except ValueError:
            new_string += char
            continue
        if abs(new_index) > len(abc):
            new_index = new_index - (int(new_index / len(abc)) * len(abc))
        new_string += abc[int(new_index)]
    return new_string

def decode_affine(string, a, b, abc=None):
    """
    Decodes a string with the affine method.
    =!= DOESN'T SEEM TO WORK PROPERLY =!=
    :param string:
    :param a:
    :param b:
    :param abc:
    :return decoded string:
    """
    # set alphabet
    if abc is None:
        abc = abc_en.copy()  # default
    elif type(abc) == list:
        abc = abc.copy()  # copies list for security
    elif type(abc) != tuple:
        return False  # returns False and ends de function if the type is not list or tuple
    string = str(string)  # converts string param to string for safety
    new_string = ''  # string for storage of result
    chars = []  # storage for chars already mapped
    for char in string:
        try:
            new_index = (abc.index(char) - b) / a
        except ValueError:
            new_string += char
            continue
        if abs(new_index) > len(abc):
            new_index = new_index - (int(new_index / len(abc)) * len(abc))
        new_string += abc[int(new_index)]
    return new_string


def encode_reverse(string):
    """
    Encodes a string with the reverse ciphering method
    :param string:
    :return encoded string:
    """
    return str(string)[::-1]  # reverse string

def decode_reverse(string):
    """
    Encodes a string with the reverse ciphering method
    :param string:
    :return decoded string:
    """
    return str(string)[::-1]  # reverse string


def encode_atbash(string, abc=None):
    """
    Encodes a string with the classic atbash ciphering method
    :param string:
    :param abc:
    :return coded string:
    """
    if abc is None:
        abc = abc_en.copy()
    elif type(abc) == list:
        abc = abc.copy()
    elif type(abc) != tuple:
        return False
    abc_rev = list(reversed(abc))
    new_string = ''
    for char in string:
        try:
            new_string += abc_rev[abc.index(char)]
        except ValueError:
            new_string += char
    return new_string

def decode_atbash(string, abc=None):
    """
    Decodes a string with the classic atbash ciphering method
    :param string:
    :param abc:
    :return decoded string:
    """
    if abc is None:
        abc = abc_en.copy()
    elif type(abc) == list:
        abc = abc.copy()
    elif type(abc) != tuple:
        return False
    abc_rev = list(reversed(abc))
    new_string = ''
    for char in string:
        try:
            new_string += abc[abc_rev.index(char)]
        except ValueError:
            new_string += char
    return new_string


if __name__ == "__main__":
    print(abc_en)
    print(type(abc_en))
    text = encode_dict(text, key_dict)
    print(text)
    text = decode_dict(text, key_dict)
    print(text)
    print("~~~ CESAR ~~~")
    print('+++ Encode +++')
    text = encode_cesar(text, 36)
    print(text)
    print("+++ Decode +++")
    text = decode_cesar(text, 36)
    print(text)
    text = decode_cesar(text, 3)
    print(text)
    count = 1
    """
  while not text == 'abba':
    text = decode_cesar(text, 3)
    count += 1
    print ('Execution N' + str(count))
  """
    text ='[llul]'
    print("~~~ AFFIN ~~~")
    print('+++ Encode +++')
    text = encode_affine(text, 3, 54)
    print(text)
    print("+++ Decode +++")
    text = decode_affine(text, 3, 54)
    print(text)

    text = 'lolito my friend]'
    print("~~~ REVERSE ~~~")
    print('+++ Encode +++')
    text = encode_reverse(text)
    print(text)
    print("+++ Decode +++")
    text = decode_reverse(text)
    print(text)

    print("~~~ ATBASH ~~~")
    print('+++ Encode +++')
    text = encode_atbash(text)
    print(text)
    print("+++ Decode +++")
    text = decode_atbash(text)
    print(text)
