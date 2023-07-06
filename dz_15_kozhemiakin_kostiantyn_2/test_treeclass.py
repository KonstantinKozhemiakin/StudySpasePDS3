import treeclass
from treeclass import Tree


def test_add_element():
    test_tree = Tree(5)
    test_tree_2 = Tree(5)
    test_tree_2.right = Tree(10)
    test_tree_2.right.right = Tree(15)
    test_tree.add_elements([10, 15])
    assert test_tree_2.id_node == test_tree.id_node
    assert test_tree_2.right.id_node == test_tree.right.id_node
    assert test_tree_2.right.right.id_node == test_tree.right.right.id_node


def test_min_element():
    test_tree = Tree(5)
    test_tree.add_elements([10, 3, 1])
    assert test_tree.find_min() == 1


def test_max_element():
    test_tree = Tree(5)
    test_tree.add_elements([10, 3, 1])
    assert test_tree.find_max() == 10


def test_delete_element():
    test_tree = Tree(5)
    test_tree.add_elements([10, 3, 4, 1, 2, 9])
    test_tree.delete_node(3)
    assert test_tree.left.id_node == 4
