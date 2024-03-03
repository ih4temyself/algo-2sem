"""
03.03.24
@author: дьяконенко денис 
  ╱|、
(˚ˎ 。7  
 |、˜〵          
じしˍ,)ノ
"""


def first_n_smallest(arr, n):
    min_order_dict = {}

    for _ in range(n):
        new_min = min(arr)
        new_min_pos = arr.index(new_min)
        min_order_dict[new_min_pos] = new_min
        arr[new_min_pos] = float("inf")

    mins_list = sorted(min_order_dict.items())
    return [tup[1] for tup in mins_list]


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 1]
    print(first_n_smallest(test_list, 3))
