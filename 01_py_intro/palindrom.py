from re import sub
"""
Modul-Dokumentation -- Ähnlich zu JavaDoc.
Wird angezeigt z.B. mit help(__name__)
Dieses Modul beinhaltet Funktionen zur Bestimmung von Palindromen
Beispiel:
>>> is_palindrom('Anna')
True
"""

# Metadaten zu dieser Datei:
__author__ = "Tobias Wiedeck"
__example__ = "SEW4/01/F" #Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"

def is_palindrom(s:str) -> bool:
    """
    Diese Funktion überprüft ob der String s ein Palindrom ist.
    :param s:
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

def is_palindrom_sentence(s:str) -> bool:
    """
    Diese Funktion hat zusätzlich zur oberen die Möglichkeit
    ganze Sätze auf Palindrome zu checken.
    :param s: str
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

def palindrom_product(x:int) -> int:
    """
    Diese Funktion berechnet das größt mögliche
    Palindrom von zwei 3 stelligen Zahlen.
    :param x:
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

def main() -> None:
    is_palindrom('Anna')
    is_palindrom_sentence("Was it a car or a cat I saw")
    palindrom_product(1)

if __name__ == "__main__":
    main()