# kruskal-s_algorithm
The code implements the Kruskal algorithm for finding the minimum spanning tree in a weighted graph and displays it on the graph.

# Мінімальне остовне дерево (Алгоритм Крускала)

Цей проект реалізує алгоритм Крускала для знаходження мінімального остовного дерева в зваженому графі і надає можливість візуалізувати результати на графіці за допомогою бібліотек `matplotlib` та `networkx`.

## Використання

1. Виберіть граф, для якого ви бажаєте знайти мінімальне остовне дерево.
2. Визначте ребра графу та їхні ваги у вигляді списку `edges`.
3. Встановіть кількість вершин графу у змінній `n`.
4. Запустіть код, і він знайде мінімальне остовне дерево та відобразить його на графі.

# Приклад визначення ребер та запуску алгоритму

edges = [(1, 2, 13), (1, 8, 5), ...]  # Список ребер, де перші два числа це номера вершин, а третє число - вага ребра між ними.
n = 14  # Кількість вершин
min_tree = kruskal_algorithm(edges, n)  # Запуск алгоритму

# Залежності

matplotlib - https://matplotlib.org/
networkx - https://networkx.org/
