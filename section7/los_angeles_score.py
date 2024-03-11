"""
07.03.24
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
import re

def get_los_angeles_points(results):
    wins = 0
    for team, scores in results:
        if re.match(r'^Los Angeles [A-Z][a-z]+$', team):
            wins += int(scores.split(':')[0])
    return wins


if __name__ == "__main__":
    basketball_results = [
        ["Dallas Mavericks", "492:513"],
        ["Los Angeles Lakers", "641:637"],
        ["Houston Rockets", "494:458"],
        ["Los Angeles Clippers", "382:422"],
        ["New Orleans Pelicans", "433:454"],
        ["Oklahoma City Thunder", "315:318"],
        ["Golden State Warriors", "559:503"],
        ["Memphis Grizzlies", "550:511"],
        ["Portland Trail Blazers", "527:520"],
        ["Minnesota Timberwolves", "495:494"],
        ["Utah Jazz", "399:402"],
        ["Sacramento Kings", "420:431"],
        ["San Antonio Spurs", "469:460"],
        ["Phoenix Suns", "523:522"],
        ["Denver Nuggets", "646:658"],
    ]
    print(get_los_angeles_points(basketball_results))
