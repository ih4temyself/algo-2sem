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

from time import time


def generate_permutations(digits) -> list:
    if len(digits) == 1:
        return [digits]

    perms = []
    for i in range(len(digits)):
        current = [digits[i]]
        remaining = digits[:i] + digits[i + 1 :]
        for p in generate_permutations(remaining):
            perms.append(current + p)
    return perms


def latest_clock(*digits) -> str:
    max_time = -1
    for perm in generate_permutations(list(digits)):
        hours = perm[0] * 10 + perm[1]
        minutes = perm[2] * 10 + perm[3]
        if hours < 24 and minutes < 60:
            total_minutes = hours * 60 + minutes
            if total_minutes > max_time:
                max_time = total_minutes

    if max_time == -1:
        return "Not possible"
    else:
        return f"{max_time // 60:02d}:{max_time % 60:02d}"


if __name__ == "__main__":
    start_time = time()
    print(latest_clock(1, 9, 8, 3))
    end_time = time()
    print(end_time - start_time)
