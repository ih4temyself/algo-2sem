"""
17.03.24
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


class T:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    if not node:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


# In-order traversal
def in_order(node):
    if not node:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


# Post-order traversal
def post_order(node):
    if not node:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]


if __name__ == "__main__":
    a = T(5, T(2, T(1), T(3)), T(7, None, T(9)))  # test from codewars
    print(in_order(a))
