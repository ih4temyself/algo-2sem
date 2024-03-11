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


def get_los_angeles_points(input_lists):
    counter = 0
    for lst in input_lists:
        team_name = lst[0]
        if (
            team_name.startswith("Los Angeles ")
            and len(team_name[13:].split()) == 1
            and team_name[12:].isalpha()
            and team_name[12:].istitle()
        ):
            counter += int(lst[1].split(":")[0])
    return counter


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
