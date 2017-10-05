"""
Шифр Вижинера
"""

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

abc = [x for x in letters]
vij_table = []

for i in range(len(letters)):
    vij = [x for x in abc[i:len(letters)]]
    vij.extend([x for x in abc[0:i]])
    vij_table.append(vij)


def keygen(w, kw):
    a = len(w) // len(kw)
    b = len(w) % len(kw)

    if a == 0:
        result = kw[:b]

    result = kw * a + kw[:b]

    return result


def encrypt(w, kw):
    w = w.lower()
    kw = kw.lower()
    key = keygen(w, kw)

    result = ''

    for i, k in zip(w, key):
        if k not in abc:
            result += k
        else:
            result += vij_table[abc.index(i)][abc.index(k)]

    return result


def decrypt(cr, kw):
    cr = cr.lower()
    kw = kw.lower()
    key = keygen(cr, kw)
    result = ''

    for i, k in zip(cr, key):
        if i not in abc:
            result += i
        else:
            result += abc[vij_table[abc.index(k)].index(i)]

    return result


if __name__ == '__main__':
    text = letters.upper() + ' ' + letters[::-1] + '.'
    key = letters[::-1] + ' ' + letters.upper() + '.'

    e = encrypt(text, key)
    d = decrypt(e, key)

    print('text:', text)
    print('key:', key)
    print('encrypt:', e)
    print('decrypt:', d)
