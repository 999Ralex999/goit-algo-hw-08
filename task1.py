import heapq

def min_cost_to_connect_cables(cables):
    """
    Знаходить мінімальні загальні витрати на об'єднання всіх мережевих кабелів.

    Args:
        cables (list): Список довжин кабелів.

    Returns:
        int: Мінімальні сумарні витрати на об'єднання кабелів.
    """
    if not cables:
        return 0  

    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
     
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        cost = first + second
        total_cost += cost

        heapq.heappush(heap, cost)

    return total_cost

if __name__ == "__main__":
 
    test_cases = [
        [4, 3, 2, 6],    # результат: 29
        [1, 2, 3, 8],    # результат: 19
        [5, 5, 5, 5],    # результат: 40
        [],              # результат: 0
        [7],             # результат: 0
    ]

    for cables in test_cases:
        result = min_cost_to_connect_cables(cables)
        print(f"Довжини кабелів: {cables} => Мінімальні витрати: {result}")
