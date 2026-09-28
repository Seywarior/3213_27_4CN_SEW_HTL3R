"""
Modul-Dokumentation -- Ähnlich zu JavaDoc.
Wird angezeigt z.B. mit help(__name__)
Dieses Modul beinhaltet Funktionen zur Bestimmung von Palindromen
Beispiel:
>>> is_palindrom('Anna')
True
"""

from re import sub

# Metadaten zu dieser Datei:
__author__ = "Tobias Wiedeck"
__example__ = "SEW4/01/F"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"


def is_palindrom(s: str) -> bool:
    """
    Diese Funktion überprüft ob der String s ein Palindrom ist.
    :param s: Der String der überprüft wird
    >>> is_palindrom('Anna')
    True
    >>> is_palindrom('Anno')
    False
    >>> is_palindrom('Was it a cat you saw?')
    False
    >>> is_palindrom('420024')
    True
    >>> is_palindrom(420024)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'lower'
    """
    s = s.lower()
    s = sub(r"[\s\W_]+", "", s)
    return s == s[::-1]


def is_palindrom_sentence(s: str) -> bool:
    """
    Diese Funktion hat zusätzlich zur oberen die Möglichkeit
    ganze Sätze auf Palindrome zu checken.
    :param s: str Ist der String der überprüft wird
    >>> is_palindrom_sentence('Anna')
    True
    >>> is_palindrom_sentence('Anno')
    False
    >>> is_palindrom_sentence('Was it a car or a cat I saw?')
    True
    >>> is_palindrom_sentence('Was it a cat you saw?')
    False
    >>> is_palindrom_sentence(420)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'lower'
    """

    s = s.lower().replace(' ', '')
    s = sub(r"[\s\W_]+", "", s)
    return s == s[::-1]


def palindrom_product(x: int) -> int:
    """
    Diese Funktion berechnet das größt mögliche
    Palindrom von zwei 3 stelligen Zahlen.
    :param x: Bestimmt die Obergrenze des Palindroms
    :return: Gibt das Produkt zurück
    >>> palindrom_product(1000000)
    906609
    >>> palindrom_product(1000)
    0
    >>> palindrom_product(100000)
    99999
    >>> palindrom_product(906609)
    888888
    >>> palindrom_product(906610)
    906609
    >>> palindrom_product(1)
    0
    """
    biggest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if i * j < x and is_palindrom(str(i * j)):
                if i * j > biggest:
                    biggest = i * j
    return biggest


def get_dec_hex_palindrom(x: int) -> int:
    """
    Diese Funktion überprüft ob eine Zahl kleiner x sowohl in
    Dezimal als auch in Hexadezimal Darstellung ein Palindrom ist.
    :param x: Obergenze die das Palindrom annehmen kann
    :return: Gibt die Zahl zurück die die Kriterien erfüllt
    """
    if x <= 0:
        return 0
    for i in range(x - 1, 0, -1):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            return i
    return 0


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    """
    num = ''
    if base < 0:
        base = abs(base)
    if number == 0:
        return '0'
    if 0 < base <= 36:
        ZIFFERN = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z')
        while number > 0:
            num += ZIFFERN[number % base]
            number //= base
    return num[::-1]


def main() -> None:
    """
    is_palindrom('Anna')
    is_palindrom_sentence("Was it a car or a cat I saw")
    palindrom_product(1)
    :return:
    """
    to_base(10, 10)


if __name__ == "__main__":
    main()
