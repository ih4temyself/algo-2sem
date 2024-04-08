def only_duplicates(st):
    my_dict = {}
    for i in st:
        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for i in st:
        if my_dict[i] == 1:
            st = st.replace(i, "")
    return st


if __name__ == "__main__":
    print(only_duplicates("abccdefee"))
