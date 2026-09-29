"""
Modul-Dokumentation -- Ähnlich zu Javadoc.
Wird angezeigt z.B. mit help(__name__).
Dieses Modul beinhaltet Funktionen zur berechnung der McCarthy-91-Funktion
Bsp:
>>> M(0)
91
"""

# Metadaten zu dieser Datei:
__author__ = "Tobias Wiedeck"
__example__ = "SEW4/01/F3"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "29.09.2026"
__license__ = "GNU GPLv3"


def M(n: int) -> int:
    """
    Eine Funktion die für alle Zahlen kleiner gleich 100 91 zurückgibt
    :param n: Startwert
    :return: 91 wenn n <= 100 sonst n -10
    >>> M(0)
    91
    >>> M(99)
    91
    >>> M(100)
    91
    >>> M(101)
    91
    >>> M(150)
    140
    >>> M(-1)
    91
    >>> M(-100)
    91
    >>> M(91)
    91
    >>> M(200)
    190
    >>> M(1000)
    990
    """
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10


def main() -> None:
    m_list: list[int] = []
    for i in range(200):
        m_list.append(M(i))
    m_dict = dict(enumerate(m_list))
    print(m_list)
    print(m_dict)


if __name__ == "__main__":
    main()
