"""
23.03.24
@author: дьяконенко денис
       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
[bug] .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rotate_right(tree):
    if tree is None or tree.left is None:
        return tree
    newTree = tree.left
    tree.left = newTree.right
    newTree.right = tree
    return newTree


def rotate_left(tree):
    if tree is None or tree.right is None:
        return tree
    newTree = tree.right
    tree.right = newTree.left
    newTree.left = tree
    return newTree


if __name__ == "__main__":
    leaf1 = Node(value=5)
    leaf2 = Node(value=8)
    child1 = Node(left=leaf1, right=leaf2, value=7)
    child2 = Node(value=11)
    tree = Node(left=child1, right=child2, value=9)
    newchild = Node(left=child1, right=None, value=9)
    correct_tree = Node(left=newchild, right=None, value=11)

    rotated_tree = rotate_left(tree)
