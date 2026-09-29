"""
Modul-Dokumentation -- Ähnlich zu Javadoc.
Wird angezeigt z.B. mit help(__name__).
Dieses Modul beinhaltet Funktionen zur berechnung der Collatz Folge
Beispiel:
>>> collatz(1)
4
"""

# Metadaten zu dieser Datei:
__author__ = "Tobias Wiedeck"
__example__ = "SEW4/01/F2"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "29.09.2026"
__license__ = "GNU GPLv3"


def collatz(n: int) -> int:
    """
    Ein einzelner Schritt in der Collatz Sequenz
    :param n: Derzeitige Zahl in der Folge
    :return: Entweder n//2 oder 3*n+1
    >>> collatz(1)
    4
    >>> collatz(2)
    1
    >>> collatz(6)
    3
    >>> collatz(7)
    22
    >>> collatz(27)
    82
    >>> collatz_sequence(0)
    Traceback (most recent call last):
    ...
    ValueError: n=0 is invalid
    """
    if n <= 0:
        raise ValueError(f"n={n} is invalid")
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_sequence(number: int) -> list[int]:
    """
    Eine Rekursive Methode bei der die gesamte Collatz Sequenz, beginnend mit der Zahl number in eine Liste gespeichert wird.
    :param number: Anfangswert der Folge
    :return: Entweder die letzten 3 sich wiederholenden Elemente 4, 2, 1 oder Rekusiv die jetzige Zahl plus sich selbst mit der nächsten Zahl.
    >>> collatz_sequence(4)
    [4, 2, 1]
    >>> collatz_sequence(8)
    [8, 4, 2, 1]
    >>> collatz_sequence(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> len(collatz_sequence(27))
    112
    >>> collatz_sequence(1)
    [1]
    >>> collatz_sequence(3)
    [3, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]
    else:
        return [number] + collatz_sequence(collatz(number))


def longest_collatz_sequence(n: int) -> tuple[int, int]:
    """
    Diese Funktion findet die längste Collatz Sequenz beginnend mit einer Zahl zwischen 1 und n
    :param n: Obergrenze die der Startwert der Collatz Sequenz annehmen kann
    :return: Gibt den Startwert der längsten Collatz Sequenz inklusive seiner länge zurück
    >>> longest_collatz_sequence(1)
    (1, 1)
    >>> longest_collatz_sequence(2)
    (2, 2)
    >>> longest_collatz_sequence(3)
    (3, 8)
    >>> longest_collatz_sequence(10)
    (9, 20)
    >>> longest_collatz_sequence(30)
    (27, 112)
    >>> longest_collatz_sequence(100)
    (97, 119)

    """
    biggest_Pair = (0, 0)
    for number in range(1, n + 1):
        if biggest_Pair[1] < len(collatz_sequence(number)):
            biggest_Pair = (number, len(collatz_sequence(number)))
    return biggest_Pair


def collatz_P(n: int, p: int = 3) -> int:
    """
    Ein Schritt in der Collatz Folge allerdings statt 3 mit einem beliebigen Faktor p
    :param n: Derzeitige Zahl in der Folge
    :param p: Der Faktor mit dem multipliert wird
    :return: Entweder n//2 oder p*n+1
    >>> collatz_P(10)
    5
    >>> collatz_P(7)
    22
    >>> collatz_P(101,2)
    203
    >>> collatz_P(5,5)
    26
    >>> collatz_P(6,7)
    3
    """
    if n % 2 == 0:
        return n // 2
    else:
        return p * n + 1


def main() -> None:
    print(collatz_sequence(19))
    print(longest_collatz_sequence(100))
    print(collatz_P(101, 2))


if __name__ == "__main__":
    main()
