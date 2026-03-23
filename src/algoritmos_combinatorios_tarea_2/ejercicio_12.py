import math
from typing import List

def perm_lex_rank(n: int, pi: List[int]) -> int:
    """
    Computa el rango lexicográfico de una permutación pi de tamaño n.
    :param n: Cardinalidad del conjunto subyacente.
    :param pi: Lista representativa de la permutación (elementos en {1, ..., n}).
    :return: Entero r en el intervalo [0, n! - 1].
    """
    r = 0
    # Creamos una copia local para no mutar el parámetro de entrada
    rho = pi.copy()
    
    # El índice j iterará de 0 a n-1 (equivalente a 1 a n en seudocódigo)
    for j in range(n):
        # rho[j] contiene valores de 1 a n, por ello la resta rho[j] - 1
        r += (rho[j] - 1) * math.factorial(n - (j + 1))
        
        # Ajuste de los elementos subsecuentes (inversiones)
        for i in range(j + 1, n):
            if rho[i] > rho[j]:
                rho[i] -= 1
                
    return r

def perm_lex_unrank(n: int, r: int) -> List[int]:
    """
    Genera la permutación de tamaño n correspondiente al rango lexicográfico r.
    :param n: Cardinalidad del conjunto subyacente.
    :param r: Rango objetivo (0 <= r < n!).
    :return: Lista representativa de la permutación pi.
    """
    pi = [0] * n
    # Inicialización del último elemento (índice n-1 en Python)
    pi[n - 1] = 1
    
    # Extracción en base factorial (j itera de 1 a n-1)
    for j in range(1, n):
        fact_j = math.factorial(j)
        fact_j_plus_1 = math.factorial(j + 1)
        
        # Aislamiento del dígito d asociado a la base j!
        d = (r % fact_j_plus_1) // fact_j
        r -= d * fact_j
        
        # Inserción del elemento relativo (índice n - 1 - j en Python)
        pi[n - 1 - j] = d + 1
        
        # Desplazamiento de los elementos a la derecha para mantener la biyección
        for i in range(n - j, n):
            if pi[i] > d:
                pi[i] += 1
                
    return pi