"""
05.03.24
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


def SJF(jobs, index):
    index_value = jobs[index]
    counter = 0
    for elem in range(len(jobs)):
        if elem <= index:
            if jobs[elem] <= index_value:
                counter += jobs[elem]
        else:
            if jobs[elem] < index_value:
                counter += jobs[elem]
    return counter


if __name__ == "__main__":
    print(SJF([3, 10, 10, 20, 1, 2], 1))
