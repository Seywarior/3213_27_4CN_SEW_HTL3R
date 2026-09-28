"""
Modul-Dokumentation -- Ähnlich zu Javadoc.
Wird angezeigt z.B. mit help(__name__).
Dieses Modul beinhaltet Funktionen zur berechnung der Collatz Folge
Beispiel:
>>> is_palindrom('Anna')
True
"""

# Metadaten zu dieser Datei:
__author__ = "Tobias Wiedeck"
__example__ = "SEW4/01/F2"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"


def collatz(n:int) -> int:
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1

def collatz_sequence(number:int) -> list:
    collatzSequence = []
    while number > 1:
        collatzSequence.append(number)
        number = collatz(number)
    return collatzSequence

def main() -> None:
    print(collatz_sequence(19))


if __name__ == "__main__":
    main()