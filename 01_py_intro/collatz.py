"""
Modul-Dokumentation -- Ähnlich zu Javadoc.
Wird angezeigt z.B. mit help(__name__).
Dieses Modul beinhaltet Funktionen zur berechnung der Collatz Folge
"""

# Metadaten zu dieser Datei:
__author__ = "Tobias Wiedeck"
__example__ = "SEW4/01/F2"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"

from ast import Tuple


def collatz(n:int) -> int:
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1

def collatz_sequence(number:int) -> list:
    if number == 4:
        return [4, 2, 1]
    else:
        return [number] + collatz_sequence(collatz(number))

def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    biggestPair = [0, 0]
    for number in range(1, n + 1):
        if biggestPair[1] < collatz_sequence(number).__len__():
            biggestPair = [number, collatz_sequence(number).__len__()]
    return biggestPair

def collatzP(n:int, p:int = 3) -> int:
    if n % 2 == 0:
        return n//2
    else:
        return p*n+1

def main() -> None:
    print(collatz_sequence(19))
    print(longest_collatz_sequence(100))
    print(collatzP(101, 2))



if __name__ == "__main__":
    main()