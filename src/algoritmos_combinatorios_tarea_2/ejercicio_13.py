from typing import List, Optional

def prev_partition(lam: List[int]) -> Optional[List[int]]:
    """
    Calcula el predecesor lexicográfico de una partición entera lambda.
    
    :param lam: Lista de enteros decrecientes que representa la partición.
    :return: Lista con la partición previa, o None si es la partición suprema (n).
    """
    k = len(lam)
    
    # Caso base: La partición suprema (n) carece de predecesor.
    if k <= 1:
        return None
        
    # 1. Determinación del índice crítico (0-indexado)
    # Buscamos de derecha a izquierda (sin contar el último elemento k-1)
    idx = 0
    for i in range(k - 2, -1, -1):
        if i == 0 or lam[i] < lam[i - 1]:
            idx = i
            break
            
    # 2. Cálculo de la masa residual a condensar
    # Suma de todos los elementos a la derecha del índice crítico, menos 1
    # que será absorbido por lam[idx]
    tail_sum = sum(lam[idx + 1:]) - 1
    
    # 3. Ensamblaje de la nueva partición
    # Se preserva el prefijo estricto
    mu = lam[:idx]
    # Se incrementa el elemento en el índice crítico
    mu.append(lam[idx] + 1)
    # Se minimiza el sufijo topológico mediante un bloque de 1s
    mu.extend([1] * tail_sum)
    
    return mu

# --- Bloque de Verificación (Prueba de Invariante) ---
if __name__ == '__main__':
    # Transición demostrada analíticamente: (2, 2, 1) -> (3, 1, 1)
    test_partition = [2, 2, 1]
    result = prev_partition(test_partition)
    assert result == [3, 1, 1], f"Fallo de aserción: esperado [3, 1, 1], obtenido {result}"