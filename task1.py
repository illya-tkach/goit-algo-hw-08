"""Завдання 1: пошук найменшого значення в AVL-дереві (двійковому дереві пошуку)."""

from avl_tree import build_tree


def find_min(root):
    """Повертає найменше значення в дереві або None, якщо дерево порожнє.

    У двійковому дереві пошуку найменше значення завжди знаходиться
    в найлівішому вузлі, тож достатньо йти ліворуч, доки це можливо.
    Складність: O(h), для AVL-дерева h = O(log n).
    """
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key


if __name__ == "__main__":
    keys = [10, 20, 30, 25, 28, 27, -1, 5, 42, 3]
    root = build_tree(keys)
    print("Дерево:")
    print(root)
    print("Значення:", keys)
    print("Найменше значення:", find_min(root))
    assert find_min(root) == min(keys)
    assert find_min(None) is None
