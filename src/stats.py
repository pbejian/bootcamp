def mediane(L):
    """Renvoie la médiane d'une liste de nombres non vide."""
    T = sorted(L)
    n = len(T)
    if n % 2 == 1:
        return T[n // 2]
    return (T[n // 2 - 1] + T[n // 2]) / 2


def moyenne(L):
    """Renvoie la moyenne d'une liste de nombres non vide."""
    return sum(L) / len(L)
