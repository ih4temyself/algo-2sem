"""
21.03.24
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


class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def list_to_array(node, array=None) -> list:
    if not array:
        array = []
    array.append(node.value)
    if node.next:
        return list_to_array(node.next, array)
    return array


if __name__ == "__main__":
    hlp = LinkedList(1, LinkedList(2, LinkedList(3)))  # test from codewars
    print(list_to_array(hlp))
