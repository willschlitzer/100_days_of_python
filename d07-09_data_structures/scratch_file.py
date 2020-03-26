def list_rev():
    numlist = [1, 2, 3, 4, 5]
    # Method that reverses the list
    numlist.reverse()
    print(numlist)


def string_to_list():
    string = "mystring"
    string_list = list(string)
    print(string_list)


def list_pop():
    string_list = list("mystring")
    # Removes and returns the last item from a list
    # Can take a specified index instead
    a = string_list.pop()
    print(a)
    print(string_list)


def list_insert():
    string_list = list("mystring")
    string_list.insert(4, "b")
    print(string_list)


def list_replace():
    string_list = list("mystring")
    string_list[0] = "b"
    print(string_list)


def list_delete():
    string_list = list("mystring")
    del string_list[0]
    print(string_list)


def dict_scratch():
    office = {"nate": 34, "will": 30, "sadi": 23}
    office["hoa"] = 29
    # print entire dictionary
    print(office)
    # Creates tuple of keys, values
    print(office.items())
    # Print just the keys
    # print(office.keys())
    # Print just the values
    # print(office.values())


if __name__ == "__main__":
    dict_scratch()
