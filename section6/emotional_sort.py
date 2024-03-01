def selection_sort(array, order):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if order[array[min_index]] > order[array[j]]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
        
def sort_emotions(array, mode): 
    if mode:
        EMOTES_ORDER = {':D':0, ':)':1, ":|":2, ':(':3, 'T_T':4}
        return selection_sort(array, EMOTES_ORDER)
        
    else: 
        EMOTES_ORDER_REV = {':D':4, ':)':3, ":|":2, ':(':1, 'T_T':0}
        return selection_sort(array, EMOTES_ORDER_REV)

if __name__ == '__main__':
    arr = [':D', ':|', ':)', ':(', ':D']
    print(sort_emotions(arr, True))
