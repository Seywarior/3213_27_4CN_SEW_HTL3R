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
    :param s:
    >>> is_palindrom('Anna')
    True
    >>> is_palindrom('Anno')
    False
    >>> is_palindrom('Was it a cat you saw')
    False
    >>> is_palindrom('420024')
    True
    >>> is_palindrom(420024)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'lower'
    """
    s = s.lower()
    return s == s[::-1]

def is_palindrom_sentence(s:str) -> bool:
    """
    :param s: str
    >>> is_palindrom_sentence('Anna')
    True
    >>> is_palindrom_sentence('Anno')
    False
    >>> is_palindrom_sentence('Was it a car or a cat I saw')
    True
    >>> is_palindrom_sentence('Was it a cat you saw')
    False
    >>> is_palindrom_sentence(420)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'lower'
    """

    s = s.lower().replace(' ', '')
    return s == s[::-1]

def main() -> None:
    is_palindrom('Anna')
    is_palindrom_sentence("Was it a car or a cat I saw")

if __name__ == "__main__":
    main()