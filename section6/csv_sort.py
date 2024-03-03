"""
03.03.24
дьяконенко денис 
  ╱|、
(˚ˎ 。7  
 |、˜〵          
じしˍ,)ノ
"""
def sort_csv_columns(csv_string):
    lines = csv_string.strip().split('\n')
    columns = lines[0].split(';')
    sorted_columns = sorted(columns, key=lambda ln: ln.lower())

    sorted_csv = []
    sorted_csv.append(';'.join(sorted_columns))

    for line in lines[1:]:
        values = line.split(';')
        sorted_values = [values[columns.index(col)] for col in sorted_columns]
        sorted_csv.append(';'.join(sorted_values))
    
    return '\n'.join(sorted_csv)


csv_input = 'myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n17945;10091;10088;3907;10132\n2;12;13;48;11'
sorted_csv_output = sort_csv_columns(csv_input)
print(sorted_csv_output)