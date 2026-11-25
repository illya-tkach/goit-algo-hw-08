"""Завдання 2: сума всіх значень в AVL-дереві (двійковому дереві пошуку)."""

from avl_tree import build_tree


def tree_sum(root):
    """Повертає суму всіх значень у дереві (0 для порожнього дерева).

    Рекурсивний обхід: сума = значення вузла + сума лівого + сума правого
    піддерева. Складність: O(n).
    """
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)


if __name__ == "__main__":
    keys = [10, 20, 30, 25, 28, 27, -1, 5, 42, 3]
    root = build_tree(keys)
    print("Дерево:")
    print(root)
    print("Значення:", keys)
    print("Сума всіх значень:", tree_sum(root))
    assert tree_sum(root) == sum(keys)
    assert tree_sum(None) == 0
