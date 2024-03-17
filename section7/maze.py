"""
12.03.24
@author: дьяконенко денис 
              =                  
              :=                 
              ::-                
              ::=.               
              :::=               
              :::==-             
             .:-==++=-.          
             :=***++==+= :-:     
             -=##+==--=--++=:    
            :=*##*+---====+==    
           -#-+*-+==---+=*+=-.   
          .=@--:=:-----=##==-:   
          =--::.-:-:---=#+=:=    
          :-::.#*#:-----=#+-=    
          :+==+=#*----::*+-=+    
          :%+::+===++=:::-=*+    
          :+.::--==-+=---=*+     
           ::..:--=-=+==+*+      
           :..::::-====+++-      
          .::......:--==++.      
          -::.......:-==++       
         :-:..   ..:-+=-=+.      
         -=:.    .::-=--=+-      
         ---:.. ...:..:==+=      
        .:.:-:..::-:-===+**      
        ::....::=====-==+**      
        -:.......::-:--=+**=     
        -.... . .....:--+*#*     
        -:.:. .   ..::::+*#*     
        --.... ..::::::=+*#*-    
        --::....::::..-=+*#*+    
        +---:...::.:::-=+**+*    
        =-=--....::.:--++*++*    
        +-+=-.....-:-:-==+++*:   
      .*=-=+-:....--+--==+=+*=   
    :%@+=:--=:....::---==+=+*+   
   %@%#++:::=:...-:=--=+==++*+   
  %@@@#+=::.-+:.:+:-:-==-++**+   
 .%@@#++-=..:+=:=:.--=+-=++**+   
 .%%@=-===:..+*++.::-====+++**   
  #%*=*=*=-::=#*-::--=-+++==++   
      :-*++=:-%#:-----==--=---   
        -=+*+=%#=+++=:---=*+=-   
       -:=--=*#-===**=-=-        
       .::-+==--::--=:           
         ::.. .::.-+=            
                                 
                 
"""

def has_exit(maze):
    
    kate_position = None
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 'k':
                if kate_position is not None:
                    raise ValueError("must be only 1 k")
                kate_position = (row_idx, col_idx)
    
    if kate_position is None:
        raise ValueError("at least 1 k")
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = set()
    
    def escape(row, col):
        if row in [-1, len(maze)] or col in [-1, len(maze[0])]:
            return True
        if not (0 <= row < len(maze)) or not (0 <= col < len(maze[0])) or maze[row][col] == '#':
            return False
        
        if (row, col) in visited:
            return False
        visited.add((row, col))
        
        for dr, dc in directions:
            if escape(row + dr, col + dc):
                return True
        return False
    
    return escape(*kate_position)

if __name__ == "__main__":
    maze = ["########",
        "# # ####",
        "# #k#   ",
        "# # # ##",
        "# # # ##",
        "#      #",
        "########"]
    
    print(has_exit(maze))