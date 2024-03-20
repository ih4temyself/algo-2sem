"""
19.03.24
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
from itertools import permutations


def calc_time_counter(gen_func, a, b, c, d):
    start_time = time()
    gen_func(a, b, c, d)
    end_time = time()
    return end_time - start_time


###############################
def latest_clock(a, b, c, d):
    digits = sorted([a, b, c, d], reverse=True)

    for i in range(4):
        if digits[i] > 2:
            continue
        for j in range(4):
            if j == i or (digits[i] == 2 and digits[j] > 3):
                continue
            for k in range(4):
                if k == i or k == j or digits[k] > 5:
                    continue
                for l in range(4):
                    if l == i or l == j or l == k:
                        continue
                    return f"{digits[i]}{digits[j]}:{digits[k]}{digits[l]}"

    return "Not possible"


###############################


###############################
def latest_clock_with_import(a, b, c, d):
    digits = [a, b, c, d]
    possible_times = permutations(digits, 4)

    max_time = None
    for hours_ten, hours_unit, minutes_ten, minutes_unit in possible_times:
        hours = hours_ten * 10 + hours_unit
        minutes = minutes_ten * 10 + minutes_unit

        if 0 <= hours < 24 and 0 <= minutes < 60:
            current_time = hours * 100 + minutes
            if max_time is None or current_time > max_time:
                max_time = current_time

    if max_time is None:
        raise Exception("No valid time can be built with these digits.")
    else:
        return f"{max_time // 100:02d}:{max_time % 100:02d}"


###############################


###############################
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


def latest_clock_recursion(*digits) -> str:
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


###############################

if __name__ == "__main__":
    print(latest_clock(1, 9, 8, 3))
    print(latest_clock_with_import(1, 9, 8, 3))

    print("my own solution")
    print(calc_time_counter(latest_clock, 1, 9, 8, 3))
    print(calc_time_counter(latest_clock, 1, 9, 8, 3))
    print(calc_time_counter(latest_clock, 1, 9, 8, 3))

    print("\npermutations imported")
    print(calc_time_counter(latest_clock_with_import, 1, 9, 8, 3))
    print(calc_time_counter(latest_clock_with_import, 1, 9, 8, 3))
    print(calc_time_counter(latest_clock_with_import, 1, 9, 8, 3))

    print("\nwith recursion")
    print(calc_time_counter(latest_clock_recursion, 1, 9, 8, 3))
    print(calc_time_counter(latest_clock_recursion, 1, 9, 8, 3))
    print(calc_time_counter(latest_clock_recursion, 1, 9, 8, 3))

    ###############################
    print("\nusing tests from codewars\n\nmy own solution")
    print(calc_time_counter(latest_clock, 1, 2, 8, 9))
    print(calc_time_counter(latest_clock, 7, 2, 0, 4))
    print(calc_time_counter(latest_clock, 0, 0, 0, 0))
    print(calc_time_counter(latest_clock, 2, 4, 0, 0))

    print("\npermutations imported")
    print(calc_time_counter(latest_clock_with_import, 1, 2, 8, 9))
    print(calc_time_counter(latest_clock_with_import, 7, 2, 0, 4))
    print(calc_time_counter(latest_clock_with_import, 0, 0, 0, 0))
    print(calc_time_counter(latest_clock_with_import, 2, 4, 0, 0))

    print("\nwith recursion")
    print(calc_time_counter(latest_clock_recursion, 1, 2, 8, 9))
    print(calc_time_counter(latest_clock_recursion, 7, 2, 0, 4))
    print(calc_time_counter(latest_clock_recursion, 0, 0, 0, 0))
    print(calc_time_counter(latest_clock_recursion, 2, 4, 0, 0))
