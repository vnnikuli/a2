class Node:
    # Класс для представления узла красно-черного дерева.
    def __init__(self, value, color="red", left=None, right=None):
        # Инициализация узла.
        self.value = value
        self.color = color
        self.left = left
        self.right = right

    def __str__(self):
        # Возвращает строковое представление узла.
        res = f'значение узла: {self.value}, цвет: {self.color}'
        return res

class RedBlackTree:
    # Класс для представления красно-черного дерева.
    def __init__(self, root=None):
        # Инициализация красно-черного дерева.
        self.root = root

    def search(self, node, data):
        # Поиск узла с указанным значением в дереве, начиная с заданного узла.
        if node is None:
            return None
        if data == node.value:
            return node

        if data > node.value:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def left_rotate(self, node):
        # Производит левый малый поворот вокруг указанного узла.
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        new_node.color = node.color
        node.color = "red"
        return new_node

    def right_rotate(self, node):
        # Производит правый малый поворот вокруг указанного узла.
        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        new_node.color = node.color
        node.color = "red"
        return new_node

    def flip_colors(self, node):
        # Производит смену цветов узла и его детей.
        node.color = "red"
        node.left.color = "black"
        node.right.color = "black"

    def add_node(self, value):
        # Добавляет новый узел с указанным значением в дерево.
        if not self.root:
            self.root = Node(value, color="black")
        else:
            self.root = self._add_node(self.root, value)
            self.root.color = "black"

    def _add_node(self, node, value):
        # Рекурсивный вспомогательный метод для добавления нового узла.
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._add_node(node.left, value)
        elif value > node.value:
            node.right = self._add_node(node.right, value)

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.left_rotate(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.right_rotate(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def is_red(self, node):
        # Проверяет, является ли узел красным.
        if node is None:
            return False
        return node.color == "red"

# Создание начального узла и дерева
initial_node = Node(15, color="black")
tree = RedBlackTree(initial_node)

# Вывод информации
print(initial_node)
tree.add_node(16)
print(tree.search(tree.root, 16))
print(initial_node)
print(tree.search(tree.root, 16))
