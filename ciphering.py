# from utilities import maths

abc_en: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

key_dict: dict = {
    'a': 'c',
    'b': 'z'
}

text: str = 'abba'



def encode_dict(string, keys):
    for key in keys:
        print("=== Looking for [" + key + "] ===")
        while key in string:
            print("Found occurence of [" + key + "] in: '" + string + "'")
            string = string.replace(key, keys[key])
            print("--> Updated text: " + string)
    return string

def decode_dict(string, keys):
    for key in keys:
        print("=== Looking for [" + keys[key] + "] ===")
        while keys[key] in string:
            print("Found occurence of [" + keys[key] + "] in: '" + string + "'")
            string = string.replace(keys[key], key)
            print("--> Updated text: " + string)
    return string


def encode_cesar(string, shift, abc=None):
    if abc is None:
        abc = abc_en.copy()
    if not (type(abc) == tuple or type(abc) == list):
        return False
    string = str(string)
    chars = []
    for char in string:
        if not char in chars:
            try:
                print('=== Cesar for character [' + char + '] of abc index [' + str(abc.index(char)) + ']')
            except ValueError:
                print('=== Cesar for character [' + char + '] of abc index [?]')
            if abs(shift) > len(abc):
                this_shift = shift - (int(shift / len(abc)) * len(abc))
            else:
                this_shift = shift
            print("Updated shift is: " + str(this_shift))
            try:
                new_index = abc.index(char) + this_shift
            except ValueError:
                break
            print('Nex index is: ' + str(new_index))
            string = string.replace(char, abc[new_index])
        chars.append(char)
    return string

def decode_cesar(string, shift, abc=None):
    if abc is None:
        abc = abc_en.copy()
    if not (type(abc) == tuple or type(abc) == list):
        return False
    string = str(string)
    chars = []
    for char in string:
        if not char in chars:
            try:
                print('=== Cesar for character [' + char + '] of abc index [' + str(abc.index(char)) + ']')
            except ValueError:
                print('=== Cesar for character [' + char + '] of abc index [?]')
            if abs(shift) > len(abc):
                this_shift = shift - (int(shift / len(abc)) * len(abc))
            else:
                this_shift = shift
            print("Updated shift is: " + str(this_shift))
            try:
                new_index = abc.index(char) - this_shift
            except ValueError:
                break
            print('Nex index is: ' + str(new_index))
            string = string.replace(char, abc[new_index])
            print('--> New string is' + string + '(replaced [' + char + '] with [' + abc[new_index] + '])')
            chars.append(char)
    return string


def encode_affine(string, a, b, abc=None):
    if abc is None:
        abc = abc_en.copy()
        print(type(abc))
    if type(abc) == int:
        return True
    if not (type(abc) == tuple or type(abc) == list):
        return False
    string = str(string)
    chars = []
    for char in string:
        if not char in chars:
            try:
                print('=== Affin for character [' + char + '] of abc index [' + str(abc.index(char)) + ']')
            except ValueError:
                print('=== Affin for character [' + char + '] of abc index [?]')
            try:
                new_index = a * abc.index(char) + b
            except ValueError:
                break
            print('Unfixed new index is: ' + str(new_index))
            if abs(new_index) > len(abc):
                print('>Index is greater than len of abc by: ' + str(int(new_index / len(abc))))
                new_index = new_index - (int(new_index / len(abc)) * len(abc))
            print('Index fixed to: ' + str(new_index))
            print('--> New string is' + string + '(replaced [' + char + '] with [' + abc[new_index] + '])')
            string = string.replace(char, abc[int(new_index)])
            chars.append(char)
    return string

def decode_affine(string, a, b, abc=None):
    if abc is None:
        abc = abc_en.copy()
        print(type(abc))
    if type(abc) == int:
        return True
    if not (type(abc) == tuple or type(abc) == list):
        return False
    string = str(string)
    print(len(abc))
    chars = []
    for char in string:
        if not char in chars:
            try:
                print('=== Affin for character [' + char + '] of abc index [' + str(abc.index(char)) + ']')
            except ValueError:
                print('=== Affin for character [' + char + '] of abc index [?]')
            try:
                new_index = (abc.index(char) - b) / a
            except ValueError:
                break
            print('Unfixed new index is: ' + str(new_index))
            if abs(new_index) > len(abc):
                print('>Index is greater than len of abc by: ' + str(int(new_index / len(abc))))
                new_index = new_index - (int(new_index / len(abc)) * len(abc))
            print('Index fixed to: ' + str(new_index))
            print('--> New string is' + string + '(replaced [' + char + '] with [' + abc[int(new_index)] + '])')
            string = string.replace(char, abc[int(new_index)])
            chars.append(char)
    return string


def encode_reverse(string):
    return string[::-1]

def decode_reverse(string):
    return string[::-1]


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
    print("~~~ AFFIN ~~~")
    print('+++ Encode +++')
    text = encode_affin(text, 3, 54)
    print(text)
    print("+++ Decode +++")
    text = decode_affin(text, 3, 54)
    print(text)

    text = 'lolito my friend'
    print("~~~ REVERSE ~~~")
    print('+++ Encode +++')
    text = encode_reverse(text)
    print(text)
    print("+++ Decode +++")
    text = decode_reverse(text)
    print(text)
