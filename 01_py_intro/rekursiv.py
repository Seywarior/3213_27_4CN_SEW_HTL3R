"""
Modul-Dokumentation -- Ähnlich zu Javadoc.
Wird angezeigt z.B. mit help(__name__).
Dieses Modul beinhaltet Funktionen zur berechnung der McCarthy-91-Funktion
"""

def M(n: int) -> int:
    """
    :param n:
    :return:
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
    """
    if n <= 100:
        return M(M(n+11))
    else:
        return n - 10

def main() -> None:
    pass

if __name__ == "__main__":
    main()