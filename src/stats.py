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


def ecart_type(L):
    """Renvoie l'écart-type d'une liste de nombres non vide."""
    m = moyenne(L)
    return (sum((x - m) ** 2 for x in L) / len(L)) ** 0.5
