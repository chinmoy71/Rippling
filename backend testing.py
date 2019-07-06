
def alphabet_position(text):
    dictt = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8',
             'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17',
             'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
             }
    arr = []
    value = 0
    new_text = text.lower()
    for i in list(new_text):
        for k, j in dictt.items():
            if k == i:
                arr.append(j)
                for i in arr:
                    value += int(i)
    return value


def count_value_sentence(s):
    arr = 0
    arr_value = []
    words = s.split(' ')
    print(words)
    for word in words:
        arr = alphabet_position(word)
        arr_value.append(arr)
    d = dict(zip(arr_value, words))
    print(d)
    d = dict(sorted(d.items()))
    print(d)
    return ' '.join(d.values())


print(count_value_sentence('a cat runs faster than the tortoise'))
