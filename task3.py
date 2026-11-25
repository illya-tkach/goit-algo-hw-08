"""Завдання 3: з'єднання мережевих кабелів з мінімальними витратами (купа)."""

import heapq


def min_connection_cost(cables):
    """Повертає (загальні витрати, порядок з'єднань).

    Жадібна стратегія з мінімальною купою: щоразу з'єднуємо два
    найкоротші кабелі, а отриманий кабель повертаємо в купу.
    Так довші кабелі входять у меншу кількість з'єднань, що мінімізує
    загальні витрати. Складність: O(n log n).
    """
    heap = list(cables)
    heapq.heapify(heap)

    total_cost = 0
    order = []
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        total_cost += cost
        order.append((first, second, cost))
        heapq.heappush(heap, cost)

    return total_cost, order


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    total, order = min_connection_cost(cables)
    print("Довжини кабелів:", cables)
    print("Порядок з'єднання:")
    for i, (a, b, cost) in enumerate(order, 1):
        print(f"  {i}. {a} + {b} = {cost} (витрати {cost})")
    print("Мінімальні загальні витрати:", total)

    assert total == 29
    assert min_connection_cost([1, 2, 3, 4, 5])[0] == 33
    assert min_connection_cost([5])[0] == 0
    assert min_connection_cost([])[0] == 0
