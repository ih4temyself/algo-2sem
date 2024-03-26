"""
25.03.24
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
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head):
    root = Node()
    root.next = head

    current = root

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        current.next = second
        first.next, second.next = second.next, first
        current = first

    return root.next
