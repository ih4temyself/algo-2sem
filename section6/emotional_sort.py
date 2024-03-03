"""
03.03.24
дьяконенко денис 
  ╱|、
(˚ˎ 。7  
 |、˜〵          
じしˍ,)ノ
"""
def sort_emotions(array, mode): 
    EMOTES_ORDER = {':D':0, ':)':1, ":|":2, ':(':3, 'T_T':4}
    if mode:
         return sorted(array, key=lambda x: EMOTES_ORDER[x])
    else:
        return sorted(array, key=lambda x: EMOTES_ORDER[x], reverse=True)

if __name__ == '__main__':
    arr = [':D', ':|', ':)', ':(', ':D']
    print(sort_emotions(arr, True))
